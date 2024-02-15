# extras.py
# debug code snippet
# Author: Finbar Dennehy

'''
message = 'I have eaten ' + 99 + 'burritos.'
print (message)
'''

# 99 needs to be converted to a string to concatenate

message = 'I have eaten ' + str(99) + ' burritos.'
print (message)

# Q7: Why is eggs a valid variable name while 100 is invalid?
# A7: integers cannot be used as variables

# Q8: What three functions can be used to get the integer, floating-point number, or string version of a value?
# A8: int(), fl(), str()