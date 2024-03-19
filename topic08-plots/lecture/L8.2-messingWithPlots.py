# messing with matplotlib
# Author: Finbar Dennehy

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints,ypoints, label = "xsquared")
plt.plot(xpoints, xpoints, label="straight", color = "red")
plt.legend() # adds legend to the plot
# save file: plt.savefig('lecture8.png') 
# Note the 'straight' plot looks like a flat line due to y scale. Might be better using log scale.

#add scatterplot
randompoints = np.random.randint(1,1000,100)
plt.scatter(xpoints,randompoints, label = "random", color = "purple")

plt.show() # display the plot