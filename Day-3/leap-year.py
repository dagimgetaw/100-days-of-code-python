# calculate if the year is leap year or not leap year means which have 365 day
year = int(input("Which year do u want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not leap year")
    else:
            print("not leap year")
else:
            print("not leap year")