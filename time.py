"""
Design a class 'Time' with members hour, min and sec.
 Write a program to add and subtract two Time objects using '+' and '-' operators
"""


class Time:

    def __init__(self, h=0, m=0, s=0):
        self.__h = h
        self.__m = m
        self.__s = s

    def display(self):
        print(self.__h, ":", self.__m, ":", self.__s)

    def __str__(self):
        return str(self.__h) + ':' + str(self.__m) + ':' + str(self.__s)

    def __add__(self, obj):
        hour = self.__h + obj.__h
        minute = self.__m + obj.__m
        second = self.__s + obj.__s

        if second >= 60:
            second = second % 60
            minute = minute + 1

        if minute >= 60:
            minute = minute % 60
            hour = hour + 1

        return Time(hour, minute, second)

    def __sub__(self, obj):
        hour = self.__h - obj.__h
        minute = self.__m - obj.__m
        second = self.__s - obj.__s

        if second >= 60:
            second = second % 60
            minute = minute + 1

        if minute >= 60:
            minute = minute % 60
            hour = hour + 1

        return Time(hour, minute, second)


h = int(input("Enter hour: "))
m = int(input("Enter minute: "))
s = int(input("Enter second: "))

time1 = Time(h, m, s)
time2 = Time(23, 59, 29)
add = time1 + time2
sub = time1 - time2
print("After Addition: ", add)
print("After Subtraction: ", sub)
