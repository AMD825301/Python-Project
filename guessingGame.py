import random

print("-" * 50)
print("WELCOME TO GUESSING GAME")
print("-" * 50)

user = int(input("Press 1 to Continue \n"
                 "Press 2 to Exit \n"))

if user == 1:

    start = eval(input("Start :- "))
    end = eval(input("End :- "))

    user_choice = eval(
        input("Guess a number between {} and {}\n".format(start, end)))

    randomNumber = random.randint(start, end)

    while True:

        if user_choice == randomNumber:
            print("Oh! You have guessed it correctly!")
            print("Number was ", randomNumber)
            break

        elif user_choice > randomNumber:
            print("Guess a smaller number.")
            user_choice = eval(input())

        else:
            print("Guess a higher number.")
            user_choice = eval(input())

elif user == 2:
    print("Exiting!")

else:
    pass
