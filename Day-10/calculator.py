from art import logo
import os

def clear():
    # For Windows
    os.system('cls')    
    # For macOS and Linux
    # os.system('clear')

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
print(logo)
num1 = int(input("What's the first number?: "))
num2  = int(input("What's the second number?: "))

for i in operation:
    print(i)
    
operation_symbol = input("Pick an operation from the line above: ")

for i in operation:
    if i == operation_symbol:
        answer = operation[i](num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")

cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ").lower()

while cont == "y":
    clear()
    temp = answer
    print(logo)
    print(f"Current value is {temp}")
    
    for i in operation:
        print(i)
    operation_symbol = input("Pick an operation: ")
    
    num3 = int(input("What the next number?: "))
    for i in operation:
        if i == operation_symbol:
            answer = operation[i](answer, num3)
            
    print(f"{temp} {operation_symbol} {num3} = {answer}")
    cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ").lower()

