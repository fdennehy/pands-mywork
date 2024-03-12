# doAdd.py
# program that allows a user to create new students and to view students. Break into smaller parts.
# part 3:  Write the doAdd() function:
# a. Read in the student’s name
# b. Read in the module names and grades (this is a bit more complicated so let’s put this in separate function and think about it by itself, see 5 below)
# c. Test this function, it creates a student dict, we can print that out.
# d. We should add the student dict to list (pass this list in)
# e. Test this
# Author: Finbar Dennehy

students = []
def readModules():
    return[]

def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

#test
    
doAdd(students)
doAdd(students)
print(students)
    