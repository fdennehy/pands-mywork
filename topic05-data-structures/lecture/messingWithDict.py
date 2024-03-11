# Messing with dictionaires
# Author: Finbar Dennehy

car = {
"make" : "ford",
"model" : "fiesta",
"year" : 1991,
"owner" : {
    "name" : "finbar",
    "owner-driver-number" : 1123
    }
}

#attr = "make"
print(car["year"]) # could use variable here
print(car["owner"]["name"])
print(car["owner"].get("name"))