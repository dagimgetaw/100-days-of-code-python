score = input("Input a list of students scores: ")
score_list = score.split()

length = len(score_list)
max = 0

for i in score_list:
    i = int(i)
    if i >= max:
        max = i
print(f"The highest score in the class is: {max}")