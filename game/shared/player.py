#!/usr/bin/env python

class Player(object):
	
	def __init__(self, uuid=0):
		self.uuid = uuid

	def __str__(self):
		return str(self.uuid)
