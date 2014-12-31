from .octree import OctreeNode

class WorldChunk(object):
	def __init__(self, is_summary, address, value):
		self.is_summary = is_summary
		self.address = address
		self.value = value

class World(object):

	def __init__(self):
		self.data = OctreeNode()


class Flatland(World):

	def generate_flatland(self):
		pass

	def start_entity_on_flatland(self, coords=None):
		pass

if __name__ == "__main__":
	world = Flatland()
	entity_id = world.start_entity_on_flatland(coords=(0,0))
	print(world.get_view_for_entity(entity_id))