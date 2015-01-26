import asyncio
import datetime
import redis
import uuid

redis = redis.StrictRedis(host="localhost", port="6379")
pid = uuid.uuid4()

@asyncio.coroutine
def heartbeat(redis, uuid, work):
    while True:
        yield from asyncio.sleep(2)
        time = datetime.datetime.utcnow().isoformat()
        pipe = redis.pipeline()
        pipe.set("server-" + str(uuid), "ip-localhost", ex=5)
        pipe.set("chunk-" + work, "server-" + str(uuid), ex=5) 
        pipe.hset("servertimes", "servertime-" + str(uuid), "time-" + time)
        pipe.hset("serverchunks", "serverchunk-" + str(uuid), "chunk-" + work)
        pipe.execute()


@asyncio.coroutine
def readbeats(redis):
    while True:
        yield from asyncio.sleep(1)
        now = datetime.datetime.utcnow()
        pipe = redis.pipeline()
        pipe.hgetall("servertimes")
        pipe.hgetall("serverchunks")
        servertimes, serverchunks = pipe.execute() #FIXME: this is binary return
        print(str(servertimes))
        print(str(serverchunks))

@asyncio.coroutine
def simple_server(reader, writer):
    data = yield from reader.read(1024)
    writer.write("Hello World".encode())
    yield from writer.drain()


loop = asyncio.get_event_loop()
tasks = [
    asyncio.start_server(simple_server, '127.0.0.1', 41537, loop=loop),
    asyncio.async(heartbeat(redis, pid, "misc")),
    asyncio.async(readbeats(redis))
]
try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt:
    pass

loop.close()

