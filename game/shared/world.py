from .octree import OctreeNode

class PlayerExistsError(LookupError):
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
		self.players = {}

	def add_player(self, player):
		if str(player) in self.players:
			raise PlayerExistsError()

		self.players[str(player)] = player


class Flatland(World):

	def generate_flatland(self):
		pass

	def start_entity_on_flatland(self, coords=None):
		pass

	def get_view_for_entity(self, entity_id):
		return (("[ ]" * 10) + "\n") * 10


if __name__ == "__main__":
	world = Flatland()
	entity_id = world.start_entity_on_flatland(coords=(0,0))
	print(world.get_view_for_entity(entity_id))
