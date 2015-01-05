import unittest
from game.world import World
from game.player import Player

class TestWorld(unittest.TestCase):
	
	def setUp(self):
		self.world = World()

	def test_add_player(self):
		player = Player()
		self.world.add_player(player)
		assertTrue(player in self.world.players)
