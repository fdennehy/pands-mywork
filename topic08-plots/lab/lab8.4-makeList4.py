# makeList4.py
# Modify the program so that it increases all the salaries by 5% (store in another array)
# Author: Finbar Dennehy

import numpy as np
# it is a good idea to have your absolute values set into variables at the beginning of your program
minSalary= 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # ensure random generator produces same numbers each time (for comparison)
salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
print (salaries)

# this will add 5000 to each value
salaries_plus = salaries + 5000 
print (salaries_plus)

# this will add 5% to each value
salaries_lift = salaries_plus*1.05 
print (salaries_lift)

# This is a float array, here I convert it to an int array (it does a floor)
newSalaries = salaries_lift.astype(int)
print(newSalaries)