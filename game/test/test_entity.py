import unittest
from game.shared.entity import Entity
from datetime import timedelta

class TestEntity(unittest.TestCase):

    def setUp(self):
        self.entity = Entity()


    def test_invalid_uuid(self):
        invalid_uuid = "elderberries"
        
        def make_entity():
            Entity(uuid=invalid_uuid)

        self.assertRaises(ValueError, make_entity)      
    
        
    def test_tick(self):
        self.entity.velocity = (1.0, 1.0, 1.0)
        self.entity.location = (0.0, 0.0, 0.0)
        self.entity.tick(timedelta(seconds=1))

        self.assertEqual(self.entity.location, (1.0, 1.0, 1.0))


if __name__ == "__main__":
    unittest.main()
