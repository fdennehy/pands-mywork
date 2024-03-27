# Demonstrate raising an exception.
# This program prompts the user for an amount and withdraws it from an account
# Author: Finbar Dennehy

balance = 100

def withdraw(amount):
    global balance
    if amount < 0:
        raise ValueError("amount should always be greater than 0")
    balance = balance - amount
    return balance

amount = int(input("amount to withdraw: "))

print (withdraw(amount))

# if the user enters a string, a ValueError will be thrown
# and we may want to capture this by creating our own exception.
# But if a user enters a negative number, the balance will increase with no error thrown.
# we need to check for the amount by adding If statement 
# another example is if someone withdraws more than the balance.