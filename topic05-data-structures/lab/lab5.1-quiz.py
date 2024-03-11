# quiz.py
# Questions on Data Structures
# Author: Finber Demnnehy


numberOfQuestions = 5
averageAge = 23.4
debugMode = True
name = "joe"
ages = []
months = ('Jan', 'Feb', 'Mar')
book = {}
stuff = [ 12 , 'Fred', False, {}]
someone = dict(firstname = "joe")
me = {
"firstName" : "Andrew",
"teaching" : [{
"courseName" : "programming",
"semester" : 1
},{
"courseName" : "Data Representation",
"semester" : 2
}
]
}

a = type(numberOfQuestions)
print(f"type of numberOfQuestions is {a}")
b = (type(averageAge))
print(f"type of averageAge is {b}")
c = (type(debugMode))
print(f"type of debugMode is {c}")
d = (type(name))
print(f"type of name is {d}")
e = (type(ages))
print(f"type of ages is {e}")
f = (type(months))
print(f"type of months is {f}")
g = (type(months[1]))
print(f"type of months[1] is {g}")
h = (type(book))
print(f"type of book is {h}")
i = (type(stuff))
print(f"type of stuff is {i}")
j = (type(stuff[2]))
print(f"type of stuff[2] is {j}")
k = (type(someone))
print(f"type of someone is {k}")
l = (type(someone["firstname"]))
print(f"type of someone['firstname'] is {l}")
m = (type(me))
print(f"type of me is {m}")
n = (type(me["teaching"]))
print(f"type of me['teaching'] is {n}")
o = (type(me["teaching"][0]["semester"]))
print(f"type of me['teaching'][0]['semester'] is {o}")
p = (type(me["teaching"][0]["coursename"]))
print(f"type of me['teaching'][0]['coursename'] is {p}")

'''
Questions with answers
What are the variable types of the following variables in the code above
a. numberOfQuestions: int
b. averageAge: float
c. debugMode: bool
d. name: str
e. ages: list
f. months: tuple
g. months[1]: str
h. book: dict
i. stuff: list
j. stuff[2]: bool
k. someone: dict
l. someone["firstname"]: str
m. me: dict
n. me["teaching"]: list
o. me["teaching"][0]["semester"]: intenger
p is a trick question look at it carefully
p. me["teaching"][0]["coursename"]: error should be capital N courseName (which would be a str)
'''


