# menuitem.py
# add menu item called save to student program previously created
# Author: Finbar Dennehy

#functions
def displayMenu():
    print("What would you like to do?")
    print("\t Add new student")
    print("\t View students")
    print("\t (s) Save students") # additional line of code
    print("\t Quit")
    choice = input("Type one letter (a/v/s/q):").strip() # additional option s

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


def doSave(students):
 #you will put the call to save dict here
 print("in save")

 
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
    elif choice == 's': # extra line
        doSave(students) # extra line
    elif choice != 'q':
        print("\n\nplease select either a, v or q")
    choice = displayMenu()

print(students)