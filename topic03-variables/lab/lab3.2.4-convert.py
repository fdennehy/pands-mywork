# convert.py
# takes in a float amount of dollars and returns that absolute amount in cent
# Author: Finbar Dennehy

# Solution 1 using round() function 

# Take in floating number
number_to_convert = float(input("Enter a float number:"))

# Convert cent to dollar (*100), limiting to two decimal places using the round() function, remove negative sign with abs()function, and store as an integer
converted_number = int(abs(round(number_to_convert*100,2)))
print("That amount in cent is {}".format(converted_number))


# Solution 2 using decimal module: 
# https://docs.python.org/3/library/decimal.html

import decimal
from decimal import Decimal

# Take in decimal number
number_to_convert = Decimal(input("Please enter an amount:"))

# Convert cent to dollar (*100), remove negative sign with abs()function, and store as an integer
converted_number = int(abs(number_to_convert)*100)
print("That amount in cent is {}".format(converted_number))