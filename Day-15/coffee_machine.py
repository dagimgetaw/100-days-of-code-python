import coffee_data
import sys

espresso = coffee_data.menu['espresso']
latte = coffee_data.menu['latte']
cappuccino = coffee_data.menu['cappuccino']


def intro():

    print("What would u like to drink?")
    print("A, espresso\nB, latte\nC, cappuccino\nD, report\n")
    choice = input("Enter ur choice: ").upper()

    coffee_machine(choice=choice)


amount = [300, 200, 100, 0]


def coffee_machine(choice):
    global coffee_type

    if choice == "A":
        coffee_type = "espresso"
        if amount[0] < coffee_data.menu[coffee_type]['ingredients']['water']:
            print("The coffee machine doesn't have sufficient water!")
            print("Wait 2 - 5 minute")
            sys.exit()
        elif amount[2] < coffee_data.menu[coffee_type]['ingredients']['coffee']:
            print("The coffee machine doesn't have sufficient coffee!")
            print("Wait 2 - 5 minute")
            sys.exit()
        coin(amount)
    elif choice == "B":
        coffee_type = "latte"
        if amount[0] < coffee_data.menu[coffee_type]['ingredients']['water']:
            print("The coffee machine doesn't have sufficient water!")
            print("Wait 2 - 5 minute")
            sys.exit()
        elif amount[1] < coffee_data.menu[coffee_type]['ingredients']['milk']:
            print("The coffee machine doesn't have sufficient milk!")
            print("Wait 2 - 5 minute")
            sys.exit()
        elif amount[2] < coffee_data.menu[coffee_type]['ingredients']['coffee']:
            print("The coffee machine doesn't have sufficient coffee!")
            print("Wait 2 - 5 minute")
            sys.exit()
        coin(amount)
    elif choice == "C":
        coffee_type = "cappuccino"
        if amount[0] < coffee_data.menu[coffee_type]['ingredients']['water']:
            print("The coffee machine doesn't have sufficient water!")
            print("Wait 2 - 5 minute")
            sys.exit()
        elif amount[1] < coffee_data.menu[coffee_type]['ingredients']['milk']:
            print("The coffee machine doesn't have sufficient milk!")
            print("Wait 2 - 5 minute")
            sys.exit()
        elif amount[2] < coffee_data.menu[coffee_type]['ingredients']['coffee']:
            print("The coffee machine doesn't have sufficient coffee!")
            print("Wait 2 - 5 minute")
            sys.exit()
        coin(amount)
    else:
        print(f"Water: {amount[0]} ml")
        print(f"Milk: {amount[1]} ml")
        print(f"Coffee: {amount[2]} ml")
        print(f"Money: {amount[3]}$")
        intro()

    return coffee_type


def coin(amount):
    total_coin = 0

    print("please insert coin.")
    quarter = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickle = int(input("How many nickle?: "))
    pennies = int(input("How many pennies?: "))

    quarter = (quarter * 25) / 100
    dimes = (dimes * 10) / 100
    nickle = (nickle * 5) / 100
    pennies = (pennies * 1) / 100

    total_coin += quarter + dimes + nickle + pennies
    price = coffee_data.menu[coffee_type]['cost']
    change = round(total_coin - price, 2)

    if coffee_type == 'espresso':
        amount[0] -= coffee_data.menu['espresso']['ingredients']['water']
        amount[2] -= coffee_data.menu['espresso']['ingredients']['coffee']
        amount[3] += price
    else:
        amount[0] -= coffee_data.menu[coffee_type]['ingredients']['water']
        amount[1] -= coffee_data.menu[coffee_type]['ingredients']['milk']
        amount[2] -= coffee_data.menu[coffee_type]['ingredients']['coffee']
        amount[3] += price

    if total_coin < price:
        print("\nSorry that's not enough money. Money refunded.")
        intro()
    else:
        print(f"\nHere is ${change} in change.")
        cont = input("Do u want to order another drink 'y' or 'n': ")

        if cont == "y":
            intro()


intro()
