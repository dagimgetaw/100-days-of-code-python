num = input("Enter two digit number: ")
first = int(num[0])
second = int(num[1])

sum = first + second

print(str(first) + " + " + str(second) + " = " + str(sum))

print("\n\n")

# BMI calculator code challenge  
height = float(input("Enter ur height in m: "))
weight = float(input("Enter ur weight in kg: "))

bmi = int(weight / (height ** 2))
print(bmi)

print("\n\n")

# Age calculator that calculate how many days, weeks and month are left if we live until age 90

ninthy_day = 32850
ninthy_week = 4680
ninthy_month = 1080

age = int(input("What is ur age? "))

current_day = age * 365
current_week = age * 52
current_month = age * 12

day_left = ninthy_day - current_day
week_left = ninthy_week - current_week
month_left = ninthy_month - current_month

print(f"U have {day_left} days, {week_left} Weeks, and {month_left} months left.")

# Day two project
# bill split 

print("Welcome to te tip calculator.")
total_bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split he bill? "))

num = round(total_bill * (12/100), 2)
total = total_bill +  num
result = round(total / number_of_people, 2)
print(f"Each person should pay? ${result}")
            
