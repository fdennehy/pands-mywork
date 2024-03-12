# More messingh with functions
# Anonymous functions
# Author: Finbar Dennehy


# x = anonymous function
x = lambda arg1:arg1**2

answer = x(4)

print(answer)



#calculate simple VAT rate: comment out whichever businesstype is not appicable.

businesstype = "standard"
#businesstype= "reduced"

vatcalc = lambda amount: amount * 0.23

if businesstype == "reduced":
    vatcalc = lambda amount: amount * 0.135

cash = 10

print(vatcalc(cash))


# sort a list
numbers = [2, 33, 55, 1, 4]
sortednum = sorted(numbers)

print(sortednum)


# sortinga  dictionary is more difficult. Let's take a look

#sort dictionary:
data = [{'first': 'Guido', 'last':'Van Rossum', 'YOB': 1956},
        {'first': 'Grace', 'last':'Hopper',     'YOB': 1906},
        {'first': 'Alan', 'last':'Turing',      'YOB': 1912}]

#passing a function into another function, sort by YOB. returns sorted array of dicts
sorteddata = sorted(data, key = lambda x: x["YOB"])

for item in sorteddata:
    print(item)