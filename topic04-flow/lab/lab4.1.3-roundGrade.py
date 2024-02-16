# roundGrade.py
# Program that modifies grade.py so that percentages are rounded
# Author: Finbar Dennehy

#First solution updates the elif statements to cater for .5

grade = float(input("Enter the percentage: "))

if grade<0 or grade>100:
    print("Please enter a number between 0 and 100")
elif grade<39.5:
    print("Fail")
elif grade<49.5:
    print("Pass")
elif grade<59.5:
    print("Merit 2")
elif grade<69.5:
    print("Merit 1")
else:
    print("Distinction")

# Second solution uses Decimal module and round() function and uses rounded (decimal) variable for the if/elif/else statements
# https://docs.python.org/3/library/decimal.html
# https://realpython.com/python-rounding/ 

import decimal
from decimal import Decimal

# reset the default rounding from ROUND_HALF_EVEN to ROUND_HALF_UP
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

# grade is captured and stored as a decimal, with .5 rounded upwards
grade = round(Decimal(input("Enter the percentage: ")))
print(grade)

if grade<0 or grade>100:
    print("Please enter a number between 0 and 100")
elif grade<40:
    print("Fail")
elif grade<50:
    print("Pass")
elif grade<60:
    print("Merit 2")
elif grade<70:
    print("Merit 1")
else:
    print("Distinction")