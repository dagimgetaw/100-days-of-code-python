print("Welcome to python pizza delivery!")
size = input("What size of pizza do u want? S, M, or L: ")
pepperoni = input("Do u want pepperoni? Y or N: ")
extra_cheese = input("Do u want extra cheese? Y or N: ")

if size == 'S':
    price = 15
    if pepperoni == 'Y':
        price += 2
        if extra_cheese == 'Y':
            price += 1
    elif pepperoni == 'N':
        if extra_cheese == 'Y':
            price += 1
elif size == 'M':
    price = 20
    if pepperoni == 'Y':
        price += 3
        if extra_cheese == 'Y':
            price += 1
    elif pepperoni == 'N':
        if extra_cheese == 'Y':
            price += 1
else:
    price = 25
    if pepperoni == 'Y':
        price += 3
        if extra_cheese == 'Y':
            price += 1
    elif pepperoni == 'N':
        if extra_cheese == 'Y':
            price += 1

print(f"Ur final bill is ${price}")
