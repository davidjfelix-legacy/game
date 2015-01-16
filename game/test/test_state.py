#!/usr/bin/env python

import unittest
from game.shared.state import PartialState


class TestPartialState(unittest.TestCase):

    def test_eq(self):
        state1 = PartialState()
        state2 = PartialState()
        self.assertTrue(state1 == state2)
        self.assertFalse(state1 is state2)  
