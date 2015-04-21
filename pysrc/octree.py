class Address(object):
    def __init__(self, x, y, z, depth):
        self.x = x
        self.y = y
        self.z = z
        self.depth = depth
        
    def get_address_at_depth(self, depth):
        mask = 1 << depth
        x_bit = (mask & self.x) >> depth
        y_bit = (mask & self.y) >> depth
        z_bit = (mask & self.z) >> depth
        return (x, y, z)
        
    def is_parent_of(self, other):
        if other.depth > self.depth:
            pass
        else:
            return False
            
    def is_child_of(self, other):
        if other.depth < self.depth:
            pass
        else:
            return False
            
    def is_sibling_of(self, other):
        if other.depth == self.depth:
            pass
        else:
            return False


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

    def insert(self, tree):
        pass

    def pop(self, address):
        pass
        
