print("Welcome to Treasure Island")
first = input("U are at a cross road. Where do u want to go? Type 'left' or 'right': ")
first = first.lower()

if first == 'left':
    second = input("U come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ")
    second = second.lower()
    if second == 'wait':
        third = input("U arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do u choose? ")
        third = third.lower()
        if third == 'yellow':
            print("You Won!")
        elif third == 'red':
            print("Game Over")
        elif third == 'blue':
            print("Game Over")
    elif second == 'swim':
        print("Game Over")
elif first == 'right':
    print("Game Over")