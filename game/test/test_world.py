import unittest
from uuid import uuid4
from game.shared.world import World, EntityExistsError
from game.shared.entity import Entity

class TestWorld(unittest.TestCase):
	
	def setUp(self):
		self.world = World()


	def test_add_entity(self):
		entity = Entity()
		self.world.add_entity(entity)
		self.assertTrue(repr(entity) in self.world.entities)

		entity_key = self.world.entities.get(repr(entity))
		self.assertEqual(entity_key, entity)


	def test_entity_already_exists(self):
		uuid = uuid4()
		entity1 = Entity(str(uuid))
		entity2 = Entity(str(uuid))
		self.world.add_entity(player1)

		def add_entity2():
			self.world.add_entity(entity2)

		self.assertRaises(EntityExistsError, add_entity2)


if __name__ == "__main__":
	unittest.main()

