# dataRead.py
# A program that reads in multiple students' names (until the user enters a blank student name), and keeps reading in their modules and grades (until the user enters a blank module name)
# Author: Finbar Dennehy

'''
# Data Strucute from lab 5.4:

student = {
    "name":"Mary",
    "modules": [
        {
            "courseName":"Programming",
            "grade":45
        },
        {
            "courseName":"History",
            "grade":99
        }
    ]   
}
print("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))


    '''

student = {}
names = {}
modules = {}

while True:
    name = input("Enter Student Name or press Enter to quit ")
    if name == "":
        break
    names["name"] = name

print(names)

'''
    for name in names:
            course_name = input("Enter course name or press Enter to quit ")
            if course_name == "":
                break
            course_grade = int(input("Enter course grade "))
            modules[course_name] = course_grade

student["names"] = names
student["modules"] = modules

print(student)
'''

'''
student = {}
names = {}
modules = {}

while True:
    name = input("Enter Student Name or press Enter to quit ")
    if name == "":
        break
    names["name"] = name
    for name in names:
        while True:
            course_name = input("Enter course name or press Enter to quit ")
            if course_name == "":
                break
            course_grade = int(input("Enter course grade "))
            modules[course_name] = course_grade
            student["names"] = names
            student["modules"] = modules

#student["names"] = names
#student["modules"] = modules

print(student)


student = {}
names = []
modules = {}

while True:
    name = input("Enter Student Name or press Enter to quit ")
    if name == "":
        break
    names.append(name)
    for name in names:
            course_name = input("Enter course name or press Enter to quit ")
            if course_name == "":
                break
            course_grade = int(input("Enter course grade "))
            modules[course_name] = course_grade

student["names"] = names
student["modules"] = modules

print(student)
'''