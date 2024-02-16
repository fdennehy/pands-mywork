# testFor.py
# first programs using For Loop
# Author: Finbar Dennehy

boats = ['Sigma', 'x yacht', 'Swan']

# note boat is a different variable to boats but this is a common pattern
for boat in boats: 
    #sep removes seperator, end="" prints everything to same line, end="\n\n" spaces on new lines.
    print("I'd rather be out in a ", boat, sep="", end="\n\n")  
    # Refer to built in functions documentation for print()

for i in range(1,10):
    print (i)

print("all done i is now", i) #sanity check and return i at the end
# range goes up to but not including - i finishes with an assigned value of 9 from this loop

if "Swan" in boats: 
    print("that is a boat")
# will discuss if and in next week during Lists lecture