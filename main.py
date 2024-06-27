from os import name, system
from art import logo, vs
from game_data import data
import random

def clear():
    """Clears the console; compatible for both Windows and Linux bases systems"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def prompt_and_check_answer(a_followers, b_followers):
    """Checks the user answer for correctness and return a boolean True/False"""
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_has_more = a_followers > b_followers
    if answer == 'a' and a_has_more:
        return True
    elif answer == 'a' and not a_has_more:
        return False
    elif answer == 'b' and a_has_more:
        return False
    else: 
        return True
        

def game():
    """Initializes the game and related data"""
    score = 0
    currentRound = 0
    while True:
        clear()
        print(logo)
        if currentRound !=0: print(f"You're right! Current score: {score}")
        
        current_a = random.choice(data)
        current_b = random.choice(data)
        while current_a == current_b:
            current_b = random.choice(data)

        a_followers = current_a['follower_count']
        b_followers = current_b['follower_count']



        print(f"Compare A: {current_a['name']}, {current_a['description']}, from {current_a['country']}.")
        print(vs)    
        print(f"Compare B: {current_b['name']}, {current_b['description']}, from {current_b['country']}.\n")    

        if prompt_and_check_answer(a_followers, b_followers):
            score += 1
            currentRound += 1
            print(f"You're right! Current score: {score}")
        else: 
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    
game()
    
    
    