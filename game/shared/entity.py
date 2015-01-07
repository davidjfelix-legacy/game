#!/usr/bin/env python
from uuid import UUID, uuid4, uuid5


class Entity(object):
	
	def __init__(self, uuid=None):
		if uuid:
			self.uuid = UUID(str(uuid))
		else:
			self.uuid = uuid4()

		self.display_name = ""
		self.location = ""
		self.is_name_visible = ""
		self.scale = 0

	
	def __repr__(self):
		return str(self.uuid)
	

	def __str__(self):
		return str(self.display_name)

