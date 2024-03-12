# More messing with functions
# flexible arguments
# Author: Finbar Dennehy

print(1,2,3, end="\t", sep="")
# to highlight the tab that as been inserted:
print("hi")

# passing in unnamed arguments (as tuples)
# doesn't expect us to be using this too much

def fun1(*args):
    #show it's a tuple
    print(type(args))
    for val in args:
        print(val)

#fun1("a", "b", "c")


# passing in keyword arguments as dict with **

def fun2(**kwargs):
    #show it's a dict
    print(type(kwargs))
    print(kwargs)
    #for val in args:
    #    print(val)

#fun2(name="joe", age=21, gender="Male")

# sample code
def ave(*values):
    number_of_values = len(values)
    sum=0
    for value in values:
        sum+= value

    average = sum / number_of_values
    return average, sum

#showing that what is returned from within the function (average, sum)
#has nothing to do with the variables outside (av1, sum_of_numbers)
#can minimise the function so that all we care about is what we are passing in
#and what we are returning whichis a tuple of the average and the sum.

av1, sum_of_numbers = (ave(1,2,3,4,5,6))

print(f"{av1} and sum is {sum_of_numbers}")
