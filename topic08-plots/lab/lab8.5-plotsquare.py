# plotsquare.py
# Write a program that plots the function y = x2
# Author: Finbar Dennehy

# import pyplot and numpy
import matplotlib.pyplot as plt
import numpy as np

# Set x-points 1 to 100
xpoints = np.array(range(1,101))

#multiply each entry by itself
ypoints = xpoints * xpoints 
plt.plot(xpoints, ypoints)
plt.show()