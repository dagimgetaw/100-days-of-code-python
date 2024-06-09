name = input("Enter ur name: ") # ask the user to input his/her name
print(len(name)) # calculate the length of the name

print("\n\n")

# switch the value of a and b
first = input("a: ")
second = input("b: ")

temp = first # create a temporary value to store tha value of first
first = second
second = temp

print("a: " + first)
print("b: " + second)

print("\n\n")

# Day one project
print("Welcome to the Band Name Generator.")
city = input("What's name of the city u grew up in? ")
pet = input("What's ur pet's name? ")
print("Ur band name could be " + city + " " + pet)
