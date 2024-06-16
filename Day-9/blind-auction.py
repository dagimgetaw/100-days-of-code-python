import os
import art

def clear():
    # For Windows
    os.system('cls')    
    # For macOS and Linux
    # os.system('clear')
    
auction_list = {}

print(art.logo)
print("Welcome to secret auction program.")

name = input("What is ur name?: ")
bid = int(input("what's ur bid?: $"))

cont = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
auction_list[name] = bid

if cont == 'no':
    clear()
    print(f"The winner is {name} with a bid of ${bid}")
else:
    while cont == 'yes':
        clear()
        name = input("What is ur name?: ")
        bid = int(input("what's ur bid?: $"))
        cont = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        auction_list[name] = bid
        
    clear()
    bids = auction_list.values()
    highest_bid = max(bids)
    for key, value in auction_list.items():
        if value == highest_bid:
            winner = key 
    print(f"The winner is {winner} with a bid of ${highest_bid}")
