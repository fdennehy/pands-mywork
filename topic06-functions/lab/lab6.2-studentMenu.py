# studentMenu.py
# program that allows a user to create new students and to view students. Break into smaller parts.
# part 1: Write a function that prints out a menu of commands we can perform, ie add, view and quit.
# The function should return what the user chose. Test the function.
# Author: Finbar Dennehy

def displayMenu():
    print("What would you like to do?")
    print("\t Add new student")
    print("\t View students")
    print("\t Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice
#reset the function
choice = displayMenu()
print(f"you chose {choice}")