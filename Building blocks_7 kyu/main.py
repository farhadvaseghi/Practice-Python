import math
class Block:
    def __init__(self, dimension):
        self.dimension = dimension
    def get_width(self):
        return self.dimension[0]
    def get_length(self):
        return self.dimension[1]
    def get_height(self):
        return self.dimension[2]
    def get_volume(self):
        return math.prod(self.dimension)
    def get_surface_area(self):
        return 2*(self.dimension[0]*self.dimension[1] + self.dimension[0]*self.dimension[2] + self.dimension[1]*self.dimension[2]) 
