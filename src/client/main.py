#!/usr/bin/env python

import signal
import pyuv as uv

from __future__ import print_function

def on_read(handle, ip_port, flags, data, error):
	if data is not None:
		handle.send(ip_port, data)

def signal_cb(handle, signum):
	signal_h.close()
	responder.close()


def main():
	print("Running main loop")
	
	loop = uv.loop.default_loop()
	responder = pyuv.UDP(loop)
	responder.bind(("0.0.0.0", 1234))
	responder.start_recv(on_read)
	
	signal_h = pyuv.Signal(loop)
	signal_h.start(signal_cb, signal.SIGINT)
	
	loop.run()
	
	print("Ending main loop")


if __name__ == "__main__":
	print("Hello Client!")
	main()
	print("Goodbye Client!")
