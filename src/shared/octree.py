#!/usr/bin/env python

class OctreeNode(object):

	def __init__(self, data=None, children=[], parent=None):
		self.data = data
		self.children = children
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


def Octree(OctreeNode):
	
	def get_child_with_index(self, index):
		return children[index]
		
	def get_child_with_coords(self, x, y, z):
		index = int("0o" + str(x) + str(y) + str(z), base=8)
		return self.get_child_with_index(index)
		
	def get_deep_child_with_coords(self, x, y, z):
		pass
