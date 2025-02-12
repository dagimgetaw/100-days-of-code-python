numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

name = "Python"
new_name = [letter for letter in name]

arr = [n * 2 for n in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
new_names = [n for n in names if len(n) < 5]

capital_name = [n.upper() for n in names if len(n) < 5]
print(capital_name)

import random

stud_score = {student: random.randint(1, 100) for student in names}
print(stud_score)
passed_stud = {student: score for (student, score) in stud_score.items() if score > 60}
print(passed_stud)
