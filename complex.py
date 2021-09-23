class Complex:

    def __init__(self, real, imaginary):
        self.__real = real
        self.__imaginary = imaginary

    def __str__(self):
        return str(self.__real) + '+' + str(self.__imaginary) + 'i'

    def __add__(self, obj):
        r = self.__real + obj.__real
        i = self.__real + obj.__imaginary

        return Complex(r, i)

    def __sub__(self, obj):
        r = self.__real - obj.__real
        i = self.__real - obj.__imaginary

        return Complex(r, i)


x = int(input("Enter the real part: "))
y = int(input("Enter the imaginary part: "))
ins1 = Complex(3, 5)
ins2 = Complex(x, y)
add = ins1 + ins2
print(add)
