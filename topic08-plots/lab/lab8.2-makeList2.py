# makeList2.py
# Modify the makeLIst program so that the “random” salaries are the same each time the program is run, 
# to make the program easier to test, ie “seed” the random number generator.
# Author: Finbar Dennehy

import numpy as np
# it is a good idea to have your absolute values set into variables at the beginning of your program
minSalary= 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # ensure random generator produces same numbers each time (for comparison)
salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
print (salaries)
