import unittest
from game.shared.game import Game
from game.shared.connection import Connection

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_add_connection(self):
        connection = Connection()
        self.game.add_connection(connection)

        self.assertIn(connection, self.game.connections.values())
