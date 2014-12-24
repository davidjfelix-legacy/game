#!/usr/bin/env python

import signal
import pyuv as uv

from __future__ import print_function

def on_read(handle, ip_port, flags, data, error):
	if data is not None:
		handle.send(ip_port, data)

def signal_cb():
	pass

from __future__ import print_function

def main():
	print("Running Main Loop!")

if __name__ == "__main__":
	print("Hello Server!")
	main()
	print("Goodbye Server!")
