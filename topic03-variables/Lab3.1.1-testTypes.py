# testTypes.py
# create 5 variables and use type() function to confirm variable type
# Author: Finbar Dennehy

i = 3
fl = 3.5
isa = True
memo = 'how now Brown Cow'
lots = []


'''
# attempt without lab solution
print(f"variable i is of type {type(i)} and value:" + str(i))
print(f"variable fl is of type {type(fl)} and value:" + str(fl))
print(f"variable isa is of type {type(isa)} and value:" + str(isa))
print(f"variable memo is of type {type(memo)} and value:" + memo)
print(f"variable lots is of type {type(lots)} and value:" + str(lots))
'''

# attempt following lab formatting
print('variable {} is of type: {} and value {}'.format('i', type(i), i))
print('variable {} is of type: {} and value {}'.format('fl', type(fl), fl))
print('variable {} is of type: {} and value {}'.format('isa', type(isa), isa))
print('variable {} is of type: {} and value {}'.format('memo', type(memo), memo))
print('variable {} is of type: {} and value {}'.format('lots', type(lots), lots))