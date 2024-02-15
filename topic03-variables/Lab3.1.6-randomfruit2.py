# randomfruit2.py
# program that prints out a random fruit, using a tuple of fruits
# Author: Finbar Dennehy

import random

fruits = ('Apple', 'Orange', 'Banana', 'Pear')

index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print("A Random Fruit:{}".format(fruit))