# studentMenu5.py
# an alternative way of dealing with users choicem
# Author: Finbar Dennehy



#functions
def displayMenu():
    print("What would you like to do?")
    print("\t Add new student")
    print("\t View students")
    print("\t Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

def doAdd(students):
    print("do add")
def doView(students):
    print("do view")
def doNothing(dumby):
    pass

# the dict that maps a letter to function
choice_map = {
    'a': doAdd,
    'v': doView,
    'q': doNothing # q is a valid choice
}

#main program
students = []
choice = displayMenu()
while(choice != 'q'):
    if choice in choice_map:
        # run the function
        choice_map[choice](students)
    else: # user did not enter something valid
        print("\n\nplease select either a, v or q")

    choice=displayMenu()

print(students)