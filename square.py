import math

class Square:

    def __init__(self, radius=1.0):
        self.radius = radius


    def getCircumference(self):
        return 2 * math.pi * self.radius


    def getArea(self):
        return math.pi * self.radius * self.radius



ob1 = Square() #default value
ob2 = Square(10)

print("For Object 1: ")
print("Circumference = {} units.".format(ob1.getCircumference))
print("Area = {} sq. units.".format(ob1.getArea))
print()
print("For Object 2: ")
print("Circumference = {} units.".format(ob2.getCircumference))
print("Area = {} sq. units.".format(ob2.getArea))

