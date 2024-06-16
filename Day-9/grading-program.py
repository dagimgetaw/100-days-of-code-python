student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Herminoe": 99,
    "Draco": 74,
    "Neville": 62,
}
for i in student_scores:
    if student_scores[i] > 90:
        grade = "Outstanding"
    elif student_scores[i] > 80:
        grade = "Exceeds Expectations"
    elif student_scores[i] > 70:
        grade = "Acceptable"
    else:
        grade = "Fails"
    print(f"{i} => {grade}") 