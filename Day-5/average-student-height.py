student_height = input("Enter the students height: ")
student_height_list = student_height.split()

length = 0
total = 0

for i in student_height_list:
    length += 1
    total += int(i)

average_student_height = round(total / length)
print(f"The average height of the student is {average_student_height}")