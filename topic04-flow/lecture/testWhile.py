# testWhile.py
# first program using While loop
# Author: Finbar Dennehy

# initialise variable
count = 0
while count < 10:
    print("count is ", count)
# running code to this point puts us in an infinite loop. ctrl + c to exit.
# need to change condition to avoid infinite loop
    count = count + 1 # can also be written as count +=1
    
print("at the end count is ", count) # count is up to 10 by the time it exits while loop

count = 10
while count >=0:
    print("countdown ", count)
    count = count - 1
print("blast off")

# sentinal controlled loop

val = input("type something (q to quit): ")
while val != 'q':
    print("hi Mum")
    val=input("q to quit:") # prompts another input, and will continue doing so until q is entered 

print("all done") # sanity check