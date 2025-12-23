import random

def get_user_choice():
    choice = input("Enter rock, paper, or scissors: ")
    while choice != "rock" and choice != "paper" and choice != "scissors":
        print("Invalid choice.")
        choice = input("Enter rock, paper, or scissors: ")
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "user"
    elif user_choice == "paper" and computer_choice == "rock":
        return "user"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    play_again = "yes"

    while play_again == "yes":
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("User chose:", user_choice)
        print("Computer chose:", computer_choice)

        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            print("User wins!")
            user_score = user_score + 1
        elif winner == "computer":
            print("Computer wins!")
            computer_score = computer_score + 1
        else:
            print("It's a tie!")
