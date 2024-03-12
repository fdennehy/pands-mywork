# Read in two numbers and multiply them
# Author: Finbar Dennehy

# add error handling, to be covered in lecture 9 or 10 in more detail

'''
num1 = False
while (num1 == False):
    try:
        num1 = int(input("Enter a number "))
    except ValueError:
        print("that was not a number ", end="")

num2 = False
while (num2 == False):
    try:
        num2 = int(input("Enter a another number "))
    except ValueError:
        print("that was not a number ", end="")

answer = num1 * num2
print(f"answer is {answer}")
'''

#problem with the above is that both blocks of code are repetitive. 
#Perfect scenario for writing a function


def readNum(message = "enter a number: "):
    num = False
    while (not num): # equivalent to num == False)
        try:
            num = int(input(message))
        except ValueError:
            print("that was not a number, ", end="")
    return num

num1=readNum()
num2=readNum("enter num2: ")

answer = num1 * num2
print(f"answer is {answer}")