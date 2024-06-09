# BMI calculator with message
height = float(input("Enter ur height in m: "))
weight = float(input("Enter ur weight in kg: "))

bmi = int(weight / (height ** 2))

if bmi < 18.5:
    print(f"Ur BMI  is {bmi}, You are underweight")
elif bmi < 25:
    print(f"Ur BMI  is {bmi}, You are have normal weight")
elif bmi < 30:
    print(f"Ur BMI  is {bmi}, You are overweight")
elif bmi < 35:
    print(f"Ur BMI  is {bmi}, You are obese")
else
    print(f"Ur BMI  is {bmi}, You are clinically obese")