# normalise.py
# program that reads in a string and (1) strips any leading or trailing spaces,  (2) converts the string to lower case, and (3) outputs the length of the input and output strings.
# Author: Finbar Dennehy
# https://www.w3schools.com/python/python_strings_methods.asp

input_string = input("Please enter a string:")
length_of_input_string = len(input_string)

output_string = input_string.strip().lower()
length_of_output_string = len(output_string)
print(f"The String normalised is: {output_string}")
print(f"we reduced the input string from {length_of_input_string} to {length_of_output_string} characters")
