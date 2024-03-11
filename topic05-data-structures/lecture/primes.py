# generate primes
# Author: Finbar Dennehy

'''
primes = []

for candidate in range(2, 101):
    #print(candidate)
    isPrime = True
    for divisor in range (2,candidate):
        if (candidate % divisor == 0):
            isPrime = False
            break #breaks out of For Loop

    if isPrime:    
        primes.append(candidate)

print(primes)
'''

''' 
Let's make more efficient. 
Above runs through more numbers than neccessary.
'''

primes = []
upto = 10001

# swap out upper limit with variable to give some flexibility
for candidate in range(2, upto):
    #print(candidate)
    isPrime = True
    # only need to check if divisable by prime
    for divisor in primes:
        # if divisable by an int it is not a prime number
        if (candidate % divisor == 0):
            isPrime = False
            # so there is no reason to keep checking
            break #breaks out of For Loop

    if isPrime:    
        primes.append(candidate)

print(primes)

'''
Other ways to make even more efficient:
- Really only have to check up to the square root
- Sieving: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
'''