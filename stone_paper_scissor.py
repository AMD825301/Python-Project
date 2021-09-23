import random

user_choice = int(input("Choose any one: \n"
                        "1. Rock \n"
                        "2. Paper \n"
                        "3. Scissor \n"))

lst = ["Rock", "Paper", "Scissor"]
computer_choice = random.choice(lst)

print("You choose = ", lst[user_choice-1])
print("Computer choose = ", computer_choice)

if user_choice == 1:
    if computer_choice == 'Paper':
        print("You loose!")

    elif computer_choice == 'Rock':
        print("Tie!")

    else:
        print("You won!")

elif user_choice == 2:
    if computer_choice == 'Scissor':
        print("You loose!")

    elif computer_choice == 'Paper':
        print("Tie!")

    else:
        print("You won!")

else:
    if computer_choice == 'Rock':
        print("You loose!")

    elif computer_choice == 'Scissor':
        print("Tie!")

    else:
        print("You won!")
