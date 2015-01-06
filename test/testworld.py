import unittest
from game.shared.world import World
from game.shared.player import Player

class TestWorld(unittest.TestCase):
	
	def setUp(self):
		self.world = World()

	def test_add_player(self):
		player = Player()
		self.world.add_player(player)
		assertTrue(player in self.world.players)

if __name__ == "__main__":
	unittest.main()

