import unittest
from game.shared.entity import Entity

class TestEntity(unittest.TestCase):

	def setUp(self):
		pass

	def test_invalid_uuid(self):
		invalid_uuid = "elderberries"
		
		def make_entity():
			Entity(uuid=invalid_uuid)

		self.assertRaises(ValueError, make_entity)


if __name__ == "__main__":
	unittest.main()
