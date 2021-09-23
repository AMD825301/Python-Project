def findGCD(a, b):
    """
    This function returns the GCD of two positive Integer.
    GCD is the greatest common divisor which means the greater number that perfectly divides
    both the numbers.
    :param a: Integer
    :param b: Integer
    :return: It will return the GCD or HCF(Highest Common Factor) of two Positive Integer.
    """

    if a == 0:
        return b

    elif b == 0:
        return a

    else:
        return findGCD(b, a % b)


num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

result = findGCD(num1, num2)

print("GCD of {0} and {1} = ".format(num1, num2), result)
