from math import ceil

def number_of_cans_need(height, width, cover):
    value = (height * width) / cover
    value = ceil(value)
    print(f"U'll need {value} cans of paint.")

h = int(input("Height of the wall: "))
w = int(input("Width of the wall: "))
c = 5
number_of_cans_need(height=h, width=w, cover=c)