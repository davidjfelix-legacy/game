from datetime import datetime
from .octree import OctreeNode

class EntityExistsError(LookupError):
	pass

class WorldChunk(object):
	def __init__(self, is_summary, address, value):
		self.is_summary = is_summary
		self.address = address
		self.value = value
		self.entities = {}


class World(object):

	def __init__(self):
		self.data = OctreeNode()
		self.entities = {}
		self.tick_count = 0
		self.last_tick_time = datetime.now()

	def add_entity(self, entity):
		if repr(entity) in self.entities:
			raise EntityExistsError()

		self.entities[repr(entity)] = entity

	def tick(self):
		new_tick_time = datetime.now()
		if self.tick_count != 0:
			tick_delta = new_tick_time - self.last_tick_time
			for entity in entities.values():
				entity.tick(tick_delta)
			#notify children

		self.tick_count += 1
		self.last_tick_time = new_tick_time
			
