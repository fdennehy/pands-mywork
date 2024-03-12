# extra.py
# Variables can be of type function, and we can call those variables.
# Author: Finbar Dennehy

def fun1():
    print("this is fun1")
def fun2():
    print("this is fun2")

which_fun = fun1
which_fun()
which_fun = fun2
which_fun()