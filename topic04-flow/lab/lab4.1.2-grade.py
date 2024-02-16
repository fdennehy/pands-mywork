# grade.py
# Program that reads in a student's percentage mark and prints out the corresponding grade, and checks that the percentage is valid)
# Author: Finbar Dennehy

grade = float(input("Enter the percentage: "))

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