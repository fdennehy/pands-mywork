# floor.py
# takes in a float and outputs an int rounded down using math module and math.floor
# Author: Finbar Dennehy

import math

numberToFloor = float(input("Enter a float number:"))
flooredNumber = math.floor(numberToFloor)
print("{} floored is {}".format (numberToFloor, flooredNumber))
