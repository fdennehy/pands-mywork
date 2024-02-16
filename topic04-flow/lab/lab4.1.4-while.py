# while.py
# Program that modifies isEven.py so that it keeps prompting the user for a number until the user enters -1
# Author: Finbar Dennehy

number = int(input("enter an integer (-1 to quit)"))
while number != -1:
    if (number % 2) == 0: # no remainder => even number
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number") # else has 1 remainder => odd number
    number=int(input("-1 to quit ")) # prompts another input, and will continue doing so until -1 (int) is entered 

print("quit successful") # sanity check to ensure we have exited the while loop