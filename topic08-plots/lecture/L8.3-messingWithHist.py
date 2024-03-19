# messing with histograms
# Author: Finbar Dennehy

import numpy as np
import matplotlib.pyplot as plt
'''
np.random.seed(1) # ensure random generator produces same numbers each time (for comparison)
norm_data = np.random.normal(size=10000)

plt.hist(norm_data)
plt.show()
'''

# pie chart
fruit = np.array(['Apples', 'Orange', 'Banana'])
numbers = np.array([23,77,500])

plt.pie(numbers, labels = fruit)
plt.legend()
plt.show()