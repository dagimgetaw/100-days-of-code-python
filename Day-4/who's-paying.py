import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names = input("Give me everybody's name and separate them with comma ',' : " )
list_name = names.split(", ") # it split the str in to the list
length = len(list_name) # get the length of the list
pay = random.randint(0, length - 1) # generate random number between 0 and last index

print(list_name[pay] + " is going to pay the meal today.")
