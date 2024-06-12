import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

list_letters = []
list_symbols = []
list_numbers = []

for i in range(0, nr_letters):
    random_letters = random.randint(0, len(letters) - 1)
    value = letters[random_letters]
    list_letters.append(value)
for i in range(0, nr_symbols):
    random_symbols = random.randint(0, len(symbols) - 1)
    value = symbols[random_symbols]
    list_symbols.append(value)
for i in range(0, nr_numbers):
    random_numbers = random.randint(0, len(numbers) - 1)
    value = numbers[random_numbers]
    list_numbers.append(value)

password = list_letters + list_symbols + list_numbers
for i in range(0, len(password)):
    print(password[i], end="")
    
print("\n\n")

random_shuffled_password = random.sample(password, len(password))
for i in range(0, len(password)):
    print(random_shuffled_password[i], end="")
