# dataRead.py
# A program that reads in one student's name, and keeps reading in their modules and grades (until the user enters a blank module name)
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

student =  {}

name = input("Enter Student Name ")

student["name"] = name

modules = {}

while True:
    course_name = input("Enter course name or press Enter to quit ")
    if course_name == "":
        break
    course_grade = int(input("Enter course grade "))
    modules[course_name] = course_grade

student["modules"] = modules

print(student)