import random

def get_user_choice():
    choice = input("Enter rock, paper, or scissors: ")
    while choice != "rock" and choice != "paper" and choice != "scissors":
        print("Invalid choice.")
        choice = input("Enter rock, paper, or scissors: ")
    return choice

