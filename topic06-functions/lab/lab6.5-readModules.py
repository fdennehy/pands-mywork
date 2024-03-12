# readmodules.py
# program that allows a user to create new students and to view students. Break into smaller parts.
# part 4:  Write the readModule() function:
#  We want to keep reading modules until the user enters a module name of blank.
# Author: Finbar Dennehy

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
        moduleName = input("\tEnter next module name (bnlank to quit):").strip()

    return modules

def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

#test
students = []   
doAdd(students)
doAdd(students)
print(students)