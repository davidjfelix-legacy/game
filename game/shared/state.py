#!/usr/bin/env python

class PartialState(object):

    def __init__(self):
        self.address = ""
        self.summary = "air"
        self.children = [[
            [None, None],
            [None, None]
        ], [
            [None, None],
            [None, None]
        ]]

    def __eq__(self, other):
        if not isinstance(other, PartialState):
            return False

        if self.address != other.address:
            return False

        if self.summary != other.summary:
            return False

        for x in range(2):
            for y in range(2):
                for z in range(2):
                    if self.children[x][y][z] != other.children[x][y][z]:
                        return False

        return True 
