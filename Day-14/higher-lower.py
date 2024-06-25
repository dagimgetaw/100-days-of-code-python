import art
import game_data
import random
import os


def clear():
    os.system('cls')


def game():
    
    clear()
    print(art.logo)
    
    a = random.randint(0, 49)
    b = random.randint(0, 49)
    
    if a == b:
        b = random.randint(0, 49)
    
    print(f"Compare A: {game_data.data[a]['name']}, {game_data.data[a]['description']}, {game_data.data[a]['country']}.")
    print(art.vs)
    print(f"Against B: {game_data.data[b]['name']}, {game_data.data[b]['description']}, {game_data.data[b]['country']}.\n")
    
    choice = input("Who has more follower? Type 'A' or 'B': ").upper()
    score = 0
    
    if choice == "A":
        if game_data.data[a]['follower_count'] >= game_data.data[b]['follower_count']:
            status = True
            correct = a
            score += 1
        elif game_data.data[a]['follower_count'] < game_data.data[b]['follower_count']:
            status = False
            clear()
            print(art.logo)
            print(f"Sorry, that's wrong, final score: {score}.")
    else:
        if game_data.data[a]['follower_count'] <= game_data.data[b]['follower_count']:
            status = True
            correct = b
            score += 1
        elif game_data.data[a]['follower_count'] > game_data.data[b]['follower_count']:
            status = False
            clear()
            print(art.logo)
            print(f"Sorry, that's wrong, final score: {score}.")
        
    while status:
        clear()
        print(art.logo)
        print(f"U're right! current score: {score}.")
        
        a = correct
        b = random.randint(0, 49)
        
        if a == b:
            b = random.randint(0, 49)
        
        print(f"Compare A: {game_data.data[a]['name']}, {game_data.data[a]['description']}, {game_data.data[a]['country']}.")
        print(art.vs)
        print(f"Against B: {game_data.data[b]['name']}, {game_data.data[b]['description']}, {game_data.data[b]['country']}.\n")

        choice = input("Who has more follower? Type 'A' or 'B': ").upper()

        if choice == "A":
            if game_data.data[a]['follower_count'] >= game_data.data[b]['follower_count']:
                correct = a
                score += 1
            elif game_data.data[a]['follower_count'] < game_data.data[b]['follower_count']:
                status = False
                clear()
                print(art.logo)
                print(f"Sorry, that's wrong, final score: {score}.")
        else:
            if game_data.data[a]['follower_count'] <= game_data.data[b]['follower_count']:
                correct = b
                score += 1
            elif game_data.data[a]['follower_count'] > game_data.data[b]['follower_count']:
                status = False
                clear()
                print(art.logo)
                print(f"Sorry, that's wrong, final score: {score}.")
    
game()


