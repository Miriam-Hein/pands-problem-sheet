# secondstring.py
# This program asks a user to input a string and outputs every second letter in reverse order.
# Author: Miriam Heinlein

#User input
sentenceInput = input ("Please enter sentence: ")

#Reverse user input

reverseSentence = sentenceInput[::-1]

# Print user input (for testing)
# print (reverseSentence)

#Funktion for outputing every second letter 

print(reverseSentence[::2])