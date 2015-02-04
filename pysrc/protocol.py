from functools import partial
import pulsar
from pulsar import coroutine_return, Pool, task, Connection, AbstractClient
from pulsar.apps.socket import SocketServer

class ControlProtocol(pulsar.ProtocolConsumer):
    separator = b'\r\n\r\n'
    buffer = b''

    def data_received(self, data):
        idx = data.find(self.separator)
        if idx >= 0: # we have a full message
            idx += len(self.separator)
            data, rest = data[:idx], data[idx:]
            self.buffer = self.response(self.buffer+data)
            self.finished()
            return rest
        else:
            self.buffer = self.buffer + data

    def start_request(self):
        self.transport.write(self._request + self.separator)

    def response(self, data):
        return data[:-len(self.separator)]

class ControlServerProtocol(ControlProtocol):
    def response(self, data):
        self.transport.write(data)
        data = data[:-len(self.seperator)]
        if data == b'QUIT':
            self.transport.close()
        return data

class Control(AbstractClient):
    protocol_factory = partial(Connection, ControlProtocol)
    
    def __init__(self, address, full_response=False, pool_size=10, loop=None):
        super(Control, self).__init__(loop)
        self.address = address
        self.full_response = full_response
        self.pool = Pool(self.connect, pool_size, self._loop)

    def connect(self):
        return self.create_connection(self.address)
    
    @task
    def __call__(self, message):
        connection = yield self.pool.connect()
        with connection:
            consumer = connection.current_consumer()
            consumer.start(message)
            result = yield consumer.on_finished
            coroutine_return(result)
