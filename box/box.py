class Cuboid(object):

    # Create a class that represents a cuboid:
    # It should take its three dimensions as constructor parameters (numbers)
    # It should have a method called `get_surface` that returns the cuboid's surface
    # It should have a method called `get_volume` that returns the cuboid's volume
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def get_surface(self):
        surface = 2*(self.n1*self.n2+self.n1*self.n3+self.n2*self.n3)
        return surface

    def get_volume(self):
        volume = self.n1*self.n2*self.n3
        return volume


box = Cuboid(10, 20, 30)
print(box.get_surface()) # should print 2200
print(box.get_volume()) # should print 6000
