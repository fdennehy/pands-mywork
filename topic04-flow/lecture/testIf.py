# testif.py
# messing with If statements
# Author: Finbar Dennehy

b=1
if True:
    # anything indented will be executed provided the statement is True. 
    # If False, indented code is skipped.
    print("we are in the if statement")
    b=22

c=1
if c==1:
    print("c is one")
else:
    print("c is not one")

d=2
# check if d is an int and is assigned the value 2.
if isinstance(d, int) and d==2:
    print("d is two")
else:
    print("d is not two")

# demonstrate elif statement
e=3
if e<0:
    print("e is negative")
elif e>10:
    print("e is greater than 10")
else:
    print("e is between 0 and 9 (inclusive)")

print("santiy ", b)