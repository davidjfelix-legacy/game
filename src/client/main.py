#!/usr/bin/env python

import signal
import pyuv as uv

from __future__ import print_function

class Client(object):
	
	def __init__(self, loop):
		self.udp_responder = pyuv.UDP(loop)
		self.udp_responder.bind(("0.0.0.0", 1234))
		self.udp_responder.start_recv(self.on_read)
		self.signal_h = pyuv.Signal(loop)
		self.signal_h.start(self.signal_cb, signal.SIGINT)
		
	def on_read(handle, ip_port, flags, data, error):
		if data is not None:
			handle.send(ip_port, data)

	def signal_cb(handle, signum):
		self.signal_h.close()
		self.udp_responder.close()


def main():
	print("Running main loop")
	
	loop = uv.loop.default_loop()
	client = Client(loop)
	loop.run()
	
	print("Ending main loop")


if __name__ == "__main__":
	print("Hello Client!")
	main()
	print("Goodbye Client!")
