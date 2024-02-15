# randomGenerator.py
# Prints out a random number between 1 and 10
# Author: Finbar Dennehy

''''
import random

number = random.randint(1,10)
print("here is a random number {}".format(number))
'''

# modify the program so that the user inputs the range

import random

lowerrange = int(input("Enter lower limit of your desired range: "))
upperrange = int(input("Enter upper limit of your desired range: "))

number = random.randint(lowerrange,upperrange)
print("here is a random number between {} and {}: {}".format(lowerrange, upperrange, number))