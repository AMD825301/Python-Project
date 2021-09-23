def checkPalindrome(string):
    return string[::1].casefold() == string[::-1].casefold()


test = input("Enter any String: ")

if checkPalindrome(test):
    print("{0} is Palindrome.".format(test))
else:
    print("{0} is not Palindrome.".format(test))
