class Address(object):
    def __init__(self, x, y, z, depth):
        self.x = x
        self.y = y
        self.z = z
        self.depth = depth
        
    def get_address_at_depth(depth):
        mask = 1 << depth
        x_bit = (mask & self.x) >> depth
        y_bit = (mask & self.y) >> depth
        z_bit = (mask & self.z) >> depth
        return (x, y, z)


class Octree(object):
    def __init__(self, address, data):
        self.parent = None
        self.children = [
            [
                [None, None],
                [None, None]
            ],
            [
                [None, None],
                [None, None]
            ]
        ]
        self.address = address
        self.data = data

    def insert(self, node):
        pass

    def pop(self, address):
        pass
        
