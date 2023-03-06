from math import *
class Circle:
    shape_object = 'Circle'
    def __init__(self, radius =1.0):
        self.radius = radius
    def __str__(self):
        return 'This is the circle with radius of {:.2f}'.format(self.radius)
    def __repr__(self):
        return 'Circle(radius = {})'.format(self.radius)

    def get_area(self):
        return self.radius * self.radius * pi
class Cylinder(Circle):  # The cylinder is subclass of Circle
    def __init__(self, radius=1.0, height=1.0):
        super().__init__(radius)  # Invoking the interpreter
        self.radius = radius
        self.height = height

    def __str__(self):
        return 'Cylinder(radius = {}, height = {})'.format(self.radius, self.height)

    def get_volume(self):
        return self.get_area() * self.height


cy1 = Cylinder(2, 3)
print(cy1)
print(cy1.get_volume())
