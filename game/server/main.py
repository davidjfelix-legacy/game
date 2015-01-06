#!/usr/bin/env python

import signal
import pyuv as uv

from __future__ import print_function

class Server(object):

	def __init__(self, loop):
		self.udp_server = pyuv.UDP(loop)
		self.udp_server.bind(("0.0.0.0", 1235))
		self.udp_server.start_recv(self.on_read)
		
		self.signal_h = pyuv.Signal(loop)
		self.signal_h.start(self.signal_cb, signal.SIGINT)

	def on_read(handle, ip_port, flags, data, error):
		if data is not None:
			handle.send(ip_port, data)

	def signal_cb(handle, signum):
		signal_h.close()
		server.close()


def main():
	print("Running Main Loop!")
	
	loop = uv.loop.default_loop()
	server = Server(loop)
	loop.run()
	
	print("Ending main loop")


if __name__ == "__main__":
	print("Hello Server!")
	main()
	print("Goodbye Server!")
