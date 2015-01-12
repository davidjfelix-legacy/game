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
        self.world.add_entity(entity1)

        def add_entity2():
            self.world.add_entity(entity2)

        self.assertRaises(EntityExistsError, add_entity2)

    def test_tick_count(self):
        first_tick = self.world.tick_count
        self.world.tick()
        second_tick = self.world.tick_count

        self.assertEqual(first_tick + 1, second_tick)

    def test_tick_time(self):
        first_tick_time = self.world.last_tick_time
        self.world.tick()
        second_tick_time = self.world.last_tick_time

        self.assertGreater(second_tick_time, first_tick_time)


if __name__ == "__main__":
    unittest.main()
