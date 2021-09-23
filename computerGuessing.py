start = 1
end = 100

print("Think a number between {} and {}\nDon't Disclose the number.".format(start, end))
input("Press ENTER to start")

guesses = 0

while True:

    high_low = start + (end - start) // 2

    guesses += 1

    myGuess = input("Well my guess is {}. Am I correct?\n"
                    "1. Press 'h' if I have to guess a higher number\n"
                    "2. Press 's' if I have to guess a smaller number\n"
                    "3. Press 'c' if my guess was correct.\n".format(high_low)).casefold()

    if myGuess == 'c':
        print("Oh! I have guessed it correctly in {} guesses.".format(guesses))
        break

    elif myGuess == 'h':
        start = high_low + 1

    elif myGuess == 's':
        end = high_low - 1

    else:
        print("Please enter a valid input.")
