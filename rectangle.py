class Rectangle:

    def __init__(self, length=2.0, width=1.0):
        self.length = length
        self.width = width

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def getArea(self):
        area = self.length * self.width

        print("Area = ", area)

    def getPerimeter(self):
        perimeter = 2 * (self.length + self.width)

        print("Perimeter = ", perimeter)


obj1 = Rectangle(40, 4)
obj2 = Rectangle(35.7, 3.5)
obj3 = Rectangle()  # It will take Default Values

obj1.getArea()
obj1.getPerimeter()
print("-"*50)

obj2.getArea()
obj2.getPerimeter()
print("-"*50)

obj3.getArea()
obj3.getPerimeter()
