# makeList3.py
# Modify the makeList2.py program, to make another array of numbers that has the salaries plus 
# 5000 (numpy is great for matrix operations)
# Author: Finbar Dennehy

import numpy as np
# it is a good idea to have your absolute values set into variables at the beginning of your program
minSalary= 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # ensure random generator produces same numbers each time (for comparison)
salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
print (salaries)

salaries_plus = salaries + 5000 # this will add 5000 to each value
print (salaries_plus)