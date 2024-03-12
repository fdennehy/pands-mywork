# studentMenu4.py
# program that allows a user to create new students and to view students. Break into smaller parts.
# part 6:  Write the doView() function approaching it in the same way we did doAdd():
# 1. print out all the student names first
# 2. make a function called displayModules() and 
# 3. call that after to print each name
# Author: Finbar Dennehy

#functions
def displayMenu():
    print("What would you like to do?")
    print("\t Add new student")
    print("\t View students")
    print("\t Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

# replace placeholder with doAdd() and readModule() functions
def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\Enter the first Module name (blank to quit):").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        # not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit):").strip()

    return modules

# replace placeholder with displayModules() and doView() functions
def displayModules(modules):
    print("\tName \t\tGrade")
    for module in modules:
        print(f"\t{module['name']}   \t{module['grade']}")

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])

#main program
students = []
choice = displayMenu()
while(choice != 'q'):
    # we could do this with lamda function
    # keeping this basic for now
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice != 'q':
        print("\n\nplease select either a, v or q")
    choice = displayMenu()

print(students)