# histOfSalaries.py
# Program that plots a histogram of the salaries (from makeList.py)
# Author: Finbar Dennehy

import numpy as np
import matplotlib.pyplot as plt

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10

# ensure random generator produces same numbers each time (for comparison)
np.random.seed(1) 
salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
print(salaries)

plt.hist(salaries)
plt.show()