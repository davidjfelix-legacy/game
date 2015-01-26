import asyncio
import redis
import uuid

redis = redis.StrictRedis(host="localhost", port="6379")
pid = uuid.uuid4()

@asyncio.coroutine
def heartbeat(redis, uuid):
    while True:
        yield from asyncio.sleep(2)
        redis.set("heartbeat-" + str(uuid), "localhost", ex=5)


@asyncio.coroutine
def readbeats(redis):
    while True:
        yield from asyncio.sleep(1)
        pass

@asyncio.coroutine
def simple_server(reader, writer):
    data = yield from reader.read(1024)
    writer.write("Hello World".encode())
    yield from writer.drain()


loop = asyncio.get_event_loop()
tasks = [
    asyncio.start_server(simple_server, '127.0.0.1', 41537, loop=loop),
    asyncio.async(heartbeat(redis, pid)),
    asyncio.async(readbeats(""))
]
try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt:
    pass

loop.close()

