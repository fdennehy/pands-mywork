# guess2.py
# Program that prompts the user to guess a number and keeps prompting the user to guess the number until the user guesses correctly
# The program tells the user if their guess is too high or too low each time they guess
# Author: Finbar Dennehy

number_to_guess = 30

guess = int(input("Please guess the number: "))

while guess != number_to_guess:
    if guess < number_to_guess:
        print("too low")
    else: print("too high")
    guess = int(input("Please guess again: "))

print ("Well done! Yes the number was", number_to_guess)