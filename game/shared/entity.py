#!/usr/bin/env python
from uuid import UUID, uuid4, uuid5


class Entity(object):
	
	def __init__(self, uuid=None):
		if uuid:
			self.uuid = UUID(str(uuid))
		else:
			self.uuid = uuid4()

		self.display_name = ""
		self.location = (0.0, 0.0, 0.0)
		self.velocity = (0.0, 0.0, 0.0)
		self.orientation = (0.0, 0.0, 0.0)
		self.address = ""
		self.is_name_visible = ""
		self.scale = 0

	
	def __repr__(self):
		return str(self.uuid)
	

	def __str__(self):
		return str(self.display_name)


	def tick(self, time_delta):
		t_delta = self.timedelta_to_seconds(time_delta)
		x_delta = self.velocity[0] * t_delta
		y_delta = self.velocity[1] * t_delta
		z_delta = self.velocity[2] * t_delta
		self.location = (
			self.location[0] + x_delta,
			self.location[1] + y_delta,
			self.location[2] + z_delta
		)

	def timedelta_to_seconds(self, time_delta):
		days = time_delta.days
		seconds = time_delta.seconds
		microseconds = time_delta.microseconds
		
		return (days * 86400) + (seconds) + (microseconds * 0.000001)

