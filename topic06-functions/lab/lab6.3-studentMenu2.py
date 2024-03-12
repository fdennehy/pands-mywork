# studentMenu2.py
# program that allows a user to create new students and to view students. Break into smaller parts.
# part 2:  Create a program that keeps displaying the menu until the user picks q. 
# if the user chooses a then call a function called doAdd() 
# if the user chooses v then call a function called doView()
# Write a function that prints out a menu of commands we can perform, ie add, view and quit.
# Author: Finbar Dennehy

#functions
def displayMenu():
    print("What would you like to do?")
    print("\t Add new student")
    print("\t View students")
    print("\t Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

def doAdd():
    #we will fill this in later
    print("in adding")

def doView():
    #we will fill this in later
    print("in viewing")

#main program
choice = displayMenu()
while(choice != 'q'):
    # we could do this with lamda function
    # keeping this basic for now
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice != 'q':
        print("\n\nplease select either a, v or q")
    choice = displayMenu()