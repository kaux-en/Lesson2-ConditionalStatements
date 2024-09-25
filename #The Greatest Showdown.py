#The Greatest Showdown

#Task 1: Identify the Greatest
number_1 = int(input("Enter first number"))
number_2 = int(input("Enter second number"))
number_3 = int(input("Enter third number"))

#Task 2: Identify the Smallest

if number_1 >= number_2 and number_1 >= number_3:
    print(f"{number_1} is the Greatest!")
elif number_2 >= number_1 and number_2 >= number_3:
    print(f"{number_2} is the Greatest!")
elif number_3 >= number_1 and number_3 >= number_2:
    print(f"{number_3} is the Greatest!")

if number_1 <= number_2 and number_1 <= number_3:
    print(f"{number_1} is the Smallest!")
elif number_2 <= number_1 and number_2 <= number_3:
    print(f"{number_2} is the Smallest!")
elif number_3 <= number_1 and number_3 <= number_2:
    print(f"{number_3} is the Smallest!")