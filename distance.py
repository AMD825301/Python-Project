class Distance:

    def __init__(self, meter, centimeter):
        self.__meter = meter
        self.__centimeter = centimeter

    def display(self):
        print(self.__meter, "m and", self.__centimeter, "cms.")

    def __str__(self):
        return str(self.__meter) + 'm ' + str(self.__centimeter) + 'cm.'

    def __add__(self, obj):
        mtr = self.__meter + obj.__meter
        cms = self.__centimeter + obj.__centimeter

        if cms >= 100:
            mtr += 1
            cms -= 100

        return Distance(mtr, cms)


x = eval(input("Enter meters: "))
y = eval(input("Enter centimeters: "))

distance1 = Distance(10, 55)
distance2 = Distance(x, y)
add = distance1 + distance2
print(add)
