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


