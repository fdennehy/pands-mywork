# Q 1A: Look at the program below, if the file test-a.txt does not exist. What will 
# happen when the program runs?

# the with statement will automatically close the file
# when it is finished with it

with open("test-a.txt") as f:
 data = f.read()
 print (data)

# the old way of doing this is
# f = open ("test1.txt")
# data = f.read()
# print(data)
# f.close()
 
# A 1A: An error will be thrown if the file does not exist
# FileNotFoundError: [Errno 2] No such file or directory: 'test-a.txt'

# Q 1B Look at the program below, if the file test-b.txt does not exist, what will be 
# outputted to the console when this program is run?
# Q 1C What will the contents of the file test-b.txt be when this program is run?

# the with statement will automatically close the file
# when it is finished with it

with open("test-b.txt", "w") as f:
  data = f.write("test b\n") # returns the number of chars written
  print (data)

with open("test-b.txt", "w") as f2: # open file again
  data = f2.write("another line\n") 
  print (data)

# A 1B: Following is the output:
# 7
# 13 (second write overwrites the first line)

# A 1C: 
# another line

# Q 1D: Look at the modified program below, what will the contents of the file be 
# after this program is run?

# The with statement will automatically close the file
# when it is finished with it

with open("test-d.txt", "w") as f:
 data = f.write("test d\n") # returns the number of chars written
 print (data)

with open("test-d.txt", "a") as f2: # open file again
 data = f2.write("another line\n") 
 print (data)

 #A 1D: will include both lines of text because the second is appended