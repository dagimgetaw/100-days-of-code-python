import os
import random
import sys

def clear():
    os.system('cls')
        
def guess_the_number(): 

    clear()
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    global number 
    number = random.randint(1, 100)
    
    if difficulty == "easy":
        easy_mode()
    else:
        hard_mode()
  
def easy_mode():
    
    clear()
    easy = 10

    for i in range(easy):
        print(f"U have {easy} attempt remaining to guess the number.")
        guessed_number = int(input("make a guess: "))
        if guessed_number > number:
            print("too high")
            easy -= 1
        elif guessed_number < number:
            print("too low")
            easy -= 1
        elif guessed_number == number:
            print("you guessed the number.")
            cont = input("Do u want to continue to play 'y' or 'n': ")
            if cont == "y":
                guess_the_number()
            else:
                sys.exit()
    print("you lose")
    cont = input("Do u want to continue to play 'y' or 'n': ")
    if cont == "y":
        guess_the_number()
    else:
        sys.exit() 
        
def hard_mode():
    
    clear()
    hard = 5
    
    for i in range(hard):
        print(f"U have {hard} attempt remaining to guess the number.")
        guessed_number = int(input("make a guess: "))
        if guessed_number > number:
            print("too high")
            hard -= 1
        elif guessed_number < number:
            print("too low")
            hard -= 1
        elif guessed_number == number:
            print("you guessed the number.")
            cont = input("Do u want to continue to play 'y' or 'n': ")
            if cont == "y":
                guess_the_number()
            else:
                sys.exit()
    print("you lose")
    cont = input("Do u want to continue to play 'y' or 'n': ")
    if cont == "y":
        guess_the_number()
    else:
        sys.exit() 
guess_the_number()