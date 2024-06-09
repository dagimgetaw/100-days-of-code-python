print("Welcome to love calculator")
name_one = input("Enter ur name: ")
name_two = input("Enter his/her name: ")

name = name_one + name_two
name = name.lower()

count_one = name.count("t")
count_one += name.count("r")
count_one += name.count("u")
count_one += name.count("e")

count_two = name.count("l")
count_two += name.count("o")
count_two += name.count("v")
count_two += name.count("e")

result = (f"{count_one}{count_two}")


if count_one < 10 and count_one > 90:
    print(f"Ur score is {result}, u go together like coke and mentos.")
elif count_one > 40 and count_two < 50:
    print(f"Ur score if {result}, u are alright together.")
else:
    print(f"Ur score is {result}.")
