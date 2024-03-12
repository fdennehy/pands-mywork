# Messing with modules
# anaconda has installed a lot of modules already on our machines
# Author: Finbar Dennehy

# Three ways to use cos function built into math module:
# 1. import the math module

import math

var = math.cos(3.14) #3.14 radians is 180

print(var)

# 2. import module as m, to use shorthand going forward

import math as m
var = m.cos(3.14) #3.14 radians is 180
print(var)

# 3. from math import cos

from math import cos

var = cos(3.14)

print(var)

# pip install on command line: pip install python-constraint

# constraint module is a module for Artificial Intelligence
from constraint import *