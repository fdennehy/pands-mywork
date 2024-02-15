# div.py
# Reads in two numbers and divides the first one by the second and give the integer result and the remainer
# Author: Finbar Dennehy

x = int(input("Enter first number: "))
y = int(input("Enter the mumber you want to divide by: "))
int_answer = x//y
remainder = x%y
print("{} divided by {} is {} with remainder {} ".format(x,y, int_answer, remainder))