import unittest
from game.shared.player import Player

class TestPlayer(unittest.TestCase):

	def setUp(self):
		pass

	def test_invalid_uuid(self):
		invalid_uuid = "elderberries"
		
		def make_player():
			Player(uuid=invalid_uuid)

		self.assertRaises(ValueError, make_player)


if __name__ == "__main__":
	unittest.main()
