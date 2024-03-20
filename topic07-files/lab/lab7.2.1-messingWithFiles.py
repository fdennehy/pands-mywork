# MessingWithFiles.py
# Write a program that counts how many times it was run.
# For this exercise will have to store data outside of memory, and that is accessible 
# each time the program is run, (persistent data). We would normally use a 
# database for something like this, but we can use a file: count.txt
# Author: Finbar Dennehy

# Function that reads in a number from a file that already exists 
# (count.txt). Test the program by calling the function and outputting the 
# number

#create constant / global variable FILENAME 
FILENAME = "count.txt"
def readNumber():
   with open(FILENAME) as f:
     number = int(f.read())
     return number
# test it
# num = readNumber()
# print (num)

# Function that takes in a number and overwrites a file with that 
# number (count.txt). test it and check that the file has been changed

def writeNumber(number):
   with open(FILENAME, "wt") as f:
      # write takes a string so we need to convert
      f.write(str(number)) 

# test it
# writeNumber(3)

# Write a program that, uses these two functions, to count how many times 
# the program has been run. Test it, check to see that the number goes up 
# each time.
      
# main
num = readNumber()
num += 1
print(f"we have run this program {num} times")
writeNumber(num)