# agesAndSalaries.py
# Write a program that makes a list called ages that has, the same number random 
# values as salaries, (range:21 to 65) . Make scatter plot of this data.
# Author: Finbar Dennehy


import numpy as np
import matplotlib.pyplot as plt

minSalary= 20000
maxSalary = 80000
number_of_entries = 100

# ensure random generator produces same numbers each time (for comparison)
np.random.seed(1) 
salaries = np.random.randint(minSalary, maxSalary,number_of_entries)
print(salaries)

# I don’t like this, I prefer having absolute values set at the top
ages = np.random.randint(low=21, high =65, size=number_of_entries)
print(ages)

plt.scatter(ages, salaries ) # this will be random
plt.show()