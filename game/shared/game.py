#!/usr/bin/env python


class Game(object):

    def __init__(self):
        self.connections = {}

    def add_connection(self, connection):
        self.connections[repr(connection)] = connection
