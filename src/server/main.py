#!/usr/bin/env python

import signal
import pyuv as uv

from __future__ import print_function

def on_read(handle, ip_port, flags, data, error):
	if data is not None:
		handle.send(ip_port, data)

def signal_cb(handle, signum):
	signal_h.close()
	server.close()

from __future__ import print_function

def main():
	print("Running Main Loop!")
	
	loop = uv.loop.default_loop()
	server = pyuv.UDP(loop)
	server.bind(("0.0.0.0", 1235))
	server.start_recv(on_read)
	
	signal_h = pyuv.Signal(loop)
	signal_h.start(signal_cb, signal.SIGINT)
	
	loop.run()
	
	print("Ending main loop")


if __name__ == "__main__":
	print("Hello Server!")
	main()
	print("Goodbye Server!")
