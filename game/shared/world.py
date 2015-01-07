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

	def add_entity(self, entity):
		if repr(entity) in self.entities:
			raise EntityExistsError()

		self.entities[repr(entity)] = entity


