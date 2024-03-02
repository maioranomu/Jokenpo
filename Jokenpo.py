# Pedra, Papel, Tesoura

import random

rounds = 1
victories = 0 
losses = 0 
draws = 0
choices = ["rock", "paper", "scissors"]
def get_user():
    print(f"Round {rounds}")
    user_cho = input("Choose between rock, paper, scissors: \n").lower()
    while user_cho not in choices:
        user_cho = input("Invalid answer, try choosing again between: rock, paper, scissors: \n")
    return user_cho

def get_comp():
    random_choice = random.choice(choices)
    return random_choice

def result(random_choice, user_cho):    
    if user_cho == random_choice:
        print(f"The computer has chosen {random_choice}")
        print("\nIT IS A DRAW!\n")
        return "draw"
    
    elif user_cho == "rock" and random_choice == "scissors":
        print(f"The computer has chosen {random_choice}")
        print("\nYou Won!\n")
        return "win"
    elif user_cho == "paper" and random_choice == "rock":
        print(f"The computer has chosen {random_choice}")
        print("\nYou Won!\n")
        return "win"
    elif user_cho == "scissors" and random_choice == "paper":
        print(f"The computer has chosen {random_choice}")
        print("\nYou Won!\n")
        return "win"
    else:
        print(f"The computer has chosen {random_choice}")
        print("\nYou Lost!\n")
        return "lose"
    

while True:
    user_cho = get_user()
    random_choice = get_comp()
    results = result(random_choice, user_cho)
    if results == "draw":
        draws += 1
        rounds += 1
    elif results == "lose":
        losses += 1
        rounds += 1
    elif results == "win":
        victories += 1
        rounds += 1
    willcont = input("Are you willing to continue fighting for your life (n if no)? ").lower()
    
    if willcont != "n":
        continue
    elif willcont == "n":
        print(f"Victories: {victories}")
        print(f"Draws: {draws}")
        print(f"Losses: {losses}")
    break

        


dontleavemenow = input("")
        

