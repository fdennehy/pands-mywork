# messing with files
# Author: Finbar Dennehy

# putting in capitals to label mas a constant we don't want to change
FILENAME= "data.txt"


# read in the whole file
'''
with open(FILENAME, 'r') as f:
    data = f.read()
    print(data)

# read in one line at a time, instead of reading ion the whole file, is in case we hit buffer sizes.    
with open(FILENAME, 'r') as f:
    for data in f:
        #print(data, end="")
        print(data.strip()) #strips out some characters from the file
        #print(data[:-4])

#data2 does not exist yet. Below will create data2.    
with open("data2.txt", "wt") as f:
    f.write("how now\n")
    f.write("brown cow\n")

print("done")

# this will append
with open("data2.txt", "a") as f:
    f.write("what the hell\n")
    f.write("brown cow\n")
'''

# this will overwrite the file
with open("data2.txt", "w+") as f:
    f.write("what the hell\n")
    f.write("brown cow\n")
    # file pointer is here when the above is written. so to print out, need to offset
    f.seek(0) #repoint to beginning of file
    data = f.read()
    print(data)

print("done")