import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi * self.radius**2
        return area


my_circle = Circle(5)

print(my_circle.get_area())