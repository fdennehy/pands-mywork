# round.py
# program should take in a float and output an int (rounded up or down)

numberToRound = float(input("Enter a float number:"))
roundedNumber = round(numberToRound)
print('{} rounded is {}'.format(numberToRound,roundedNumber))

# be wary of round() - it rounds to the nearest even number