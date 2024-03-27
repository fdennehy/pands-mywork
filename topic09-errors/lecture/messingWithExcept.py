# messingWithExcept.py
# This program is to show you how you can use try except
# Author: Finbar Dennehy

#filename = 'data.txt'
import sys

# sys.argv is a list which contains program name + arguments
# print(sys.argv)

#Error handling
try:
    filename = sys.argv[1]
    print(filename)
    with open(filename) as fp:
        print(fp.read())

# catch particular index error
except IndexError as ie:
    print("please enter the filename as an argument")
    # print(ie) # 'list index out of range thrown'
except FileNotFoundError:
    print(f"file {filename} not found, please enter a filename that exists")