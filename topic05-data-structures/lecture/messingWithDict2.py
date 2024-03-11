# More messing with dictionaries
# Here we are looking at For Loops
# Author: Finbar Dennehy

car = {
"make" : "Fiat",
"model" : "Punto",
"price" : 5000,
"tags" : ["pre-owned", "Best Buy", "Dealer"]
    }

# print(car)

# for key in car:
#     print(key, 'has value', car[key])

for key, value in car.items():
    print(key,'has a value',value)
