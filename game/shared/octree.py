#!/usr/bin/env python


class OctreeNode(object):

    def __init__(self, data=None, children=None, parent=None):
        if children is None:
            self.children = []
        else:
            self.children = children

        self.data = data
        self._parent = parent

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        if isinstance(value, OctreeNode):
            self._parent = value
        else:
            raise TypeError("parent must be type OctreeNode")

    @parent.deleter
    def parent(self):
        self._parent = None


class Octree(OctreeNode):

    def get_child_with_index(self, index):
        return self.children[index]

    def get_child_with_coords(self, x_coord, y_coord, z_coord):
        index = int("0o" + str(x_coord) + str(y_coord) + str(z_coord), base=8)
        return self.get_child_with_index(index)

    def get_deep_child_with_coords(self, x_coord, y_coord, z_coord):
        pass
