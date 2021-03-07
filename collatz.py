# collatz.py
#The program takes the user's input (positive integer) and prints the successive values after being calculated.
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
#The program ends if the value is one.
# Author: Miriam Heinlein

#User Input
positiveNumber = int(input ("Please enter a positive number: "))

#Calculate 

while answer > 1:
if (positiveNumber % 2) == 0: #even number
    answer = int(positiveNumber)/2
    print(answer1)
else: # odd numbers
    answer = int(positiveNumber)*3
    print(answer2)

