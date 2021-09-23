number = int(input("Please Enter a 3 digit number: "))
temp = number
reverse = 0

while number > 0:
    last_Digit = number % 10
    reverse = reverse * 10 + last_Digit
    number //= 10

if temp == reverse:
    print("{0} is Palindrome.".format(temp))
else:
    print("{0} is not Palindrome.".format(temp))
