# more messing with functions
# variable scope
# Author: Finbar Dennehy

# Try not to have global variables: 
# you may change variables inside a function inadvertently

# this variable x is outside the function
x = 999

# if you want the value 99 in your function, then pass in the value, e.g. using num
def fun1(num):
    print(num)

fun1(x)
print(f"after fun1 x is {x}")


# to show how value of x changes within function and then reverts outside of function
# could name the variable in the below function x2 to show 
# it is a different variable to our global variable
def fun2(x):
    print(f"In fun2 x is {x}")
    x=21
    print(f"In fun2 x is {x}")

fun2(x)
print(f"after fun2 x is {x}")