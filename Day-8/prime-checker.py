def prime_number_checker(number):
    if number == 1:
        print("It's not a prime number.")
    elif number == 2 or number == 3 or number == 5 or number == 7:
        print("It's a prime number.")
    elif number %2 == 0 or number %3 ==0 or number %5 == 0 or number %7 == 0:
        print("It's not a prime number.")
    elif number %1 == 0 and number % number == 0:
        print("It's a prime number.")
            

n = int(input("Enter the number to check: "))
prime_number_checker(number=n)