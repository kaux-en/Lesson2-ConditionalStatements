#Leap Year Explorer

#Task 1: Leap Year Checker
year = int(input("Enter a year"))


leap_year = True if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else False
print(leap_year)


