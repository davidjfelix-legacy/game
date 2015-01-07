import unittest
from game.shared.world import World
from game.shared.player import Player

class TestWorld(unittest.TestCase):
	
	def setUp(self):
		self.world = World()

	def test_add_player(self):
		player = Player()
		self.world.add_player(player)
		self.assertTrue(str(player) in self.world.players)

		player_key = self.world.players.get(str(player))
		self.assertEquals(player_key, player)


if __name__ == "__main__":
	unittest.main()

