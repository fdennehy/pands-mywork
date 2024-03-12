# Messing with functions
# to demonstrate the defining and using functions
# Author: Finbar Dennehy

'''
x, y, z = (1, 2, 3)
#print(x, y, z, sep="", end="")
#print(f"{x} {y} {z}")
#print("{} {} {}".format(x, y, z))

def cube(number):
    #print(number)
    return number ** 3

#ans = cube(23)
#print(f"we got {ans}")

num = 45
print(f"and {num} is {cube(num)}")

#print(cube(2))
'''


#set default power to 3
def topower(number, power=3):
    return number ** power

num = 45

#add power argument will overwrite the default
print(f"and {num} is {topower(num,2)}")

