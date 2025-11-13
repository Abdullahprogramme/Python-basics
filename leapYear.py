# Conditions:
# 1. A year is a leap year if it is divisible by 4.
# 2. However, if the year is divisible by 100, it is NOT a a leap year, unless:
# 3. The year is also divisible by 400, then it is a leap year.


for i in range(5):
    year = int(input("Enter a year: "))
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        else:
            print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")