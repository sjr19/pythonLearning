import math
class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        y = self.coor2[1] - self.coor1[1]
        x = self.coor2[0] - self.coor1[0]
        print(math.sqrt(y**2 + x**2))
        return math.sqrt(y**2 + x**2)

    def slope(self):
        y = self.coor2[1] - self.coor1[1]
        x = self.coor2[0] - self.coor1[0]
        print(y/x)
        return y / x


# EXAMPLE OUTPUT

coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

li.distance()
li.slope()

class Cylinder:

    pi = 3.14
    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        vol = self.pi * (self.radius ** 2) * self.height
        print("Volume: {}".format(vol))
        return vol

    def surface_area(self):
        sArea = 2 * self.pi * self.radius * self.height
        print("Surface Area: {}".format(sArea))

cy = Cylinder(li.distance())

cy.volume()
cy.surface_area()
