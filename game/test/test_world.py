import unittest
from uuid import uuid4
from game.shared.world import World, PlayerExistsError
from game.shared.player import Player

class TestWorld(unittest.TestCase):
	
	def setUp(self):
		self.world = World()

	def test_add_player(self):
		player = Player()
		self.world.add_player(player)
		self.assertTrue(repr(player) in self.world.players)

		player_key = self.world.players.get(repr(player))
		self.assertEqual(player_key, player)

	def test_player_exists(self):
		uuid = uuid4()
		player1 = Player(str(uuid))
		player2 = Player(str(uuid))
		self.world.add_player(player1)

		def add_player2():
			self.world.add_player(player2)

		self.assertRaises(PlayerExistsError, add_player2)


if __name__ == "__main__":
	unittest.main()

