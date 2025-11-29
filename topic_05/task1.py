import random

options = ["rock", "scissor", "paper"]
user_choice = input("Введіть rock, scissor або paper: ").lower()

if user_choice not in options:
    print("Невірне значення!")
else:
    computer_choice = random.choice(options)
    print(f"Комп'ютер обрав: {computer_choice}")

    if user_choice == computer_choice:
        print("Нічия!")
    elif (
        (user_choice == "rock" and computer_choice == "scissor") or
        (user_choice == "scissor" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("Ви перемогли!")
    else:
        print("Комп'ютер переміг!")
