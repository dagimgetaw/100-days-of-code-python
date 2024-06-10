import random

user = int(input("What do u choose? Type 0 for Rock, 1 for Paper and 2 for Scissor: "))
    
computer = random.randint(0,2)

item = ["Rock", "Paper", "Scissor"]

if user == computer:
    print(f"You choose {item[user]} and the computer choose {item[computer]} too and the result is Draw")
elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 3 and computer == 2):
    print(f"You choose {item[user]} and the computer choose {item[computer]} you Won")
else:
    print(f"You choose {item[user]} and the computer choose {item[computer]} you Lose ")