#!/usr/bin/env python
from uuid import UUID, uuid4, uuid5


class Player(object):
	
	def __init__(self, uuid=None):
		if uuid:
			self.uuid = UUID(str(uuid))
		else:
			self.uuid = uuid4()

	def __str__(self):
		return str(self.uuid)
