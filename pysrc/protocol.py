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
