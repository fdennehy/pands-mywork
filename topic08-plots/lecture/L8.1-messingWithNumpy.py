# Messing with numpy
# Author Finbar Dennehy

import numpy as np

list_of_numbers = [1,2,3,"asdf"]
print("list", list_of_numbers)

#Mathematical Operations
numbers = np.array([1,2,3,4])
numbers = numbers + 3 

print("array", numbers) 
# commas are not printed out here.
# if a float, or string is included as one of the values, 
# all other numbers are converted to this type.


rando = np.random.randint(100,200,30)
print(rando)
normalrando = np.random.normal(size=100)
print(normalrando)