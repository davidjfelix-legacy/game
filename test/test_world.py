import unittest
from game.shared.world import World, PlayerExistsError
from game.shared.player import Player

class TestWorld(unittest.TestCase):
	
	def setUp(self):
		self.world = World()

	def test_add_player(self):
		player = Player()
		self.world.add_player(player)
		self.assertTrue(str(player) in self.world.players)

		player_key = self.world.players.get(str(player))
		self.assertEqual(player_key, player)

	def test_player_exists(self):
		player1 = Player()
		player2 = Player()
		self.world.add_player(player1)

		def add_player2():
			self.world.add_player(player2)

		self.assertRaises(PlayerExistsError, add_player2)


if __name__ == "__main__":
	unittest.main()

