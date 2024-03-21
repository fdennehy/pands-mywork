# twoOnPlot3.py
# Save twoOnPlot to a file called “prettier-plot.py”
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

plt.scatter(ages, salaries) # this will be random

# add x squared
xpoints = np.array(range(1, 101))
#multiply each entry by itself
ypoints = xpoints * xpoints 
plt.plot(xpoints, ypoints, color= 'red', label="x squared")
plt.title("random plot")
plt.xlabel("age")
plt.ylabel("salaries")
plt.legend()
# plt.show() # see how the axis have change

#add this line to the end and you can comment out the show()
plt.savefig('prettier-plot.png')