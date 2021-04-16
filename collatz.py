# collatz.py
# The program takes the user's input (positive integer) and prints the successive values after being calculated.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# The program ends if the value is one.
# Author: Miriam Heinlein

#User Input
positiveNumber = int(input ("Please enter a positive number: ")) 

#Calculate 
def collatz(positiveNumber): #beginning of function
    while positiveNumber != 1: #Continue until positiveNumber equals 1
        if (positiveNumber % 2) == 0: #even number (even numbers are dividable by 2 without any remainder, so if remainder it proceeds to else otherwise it ends the program)
            positiveNumber = positiveNumber//2 #calculation after being defined as even number
            print(" ", int(positiveNumber), end="")
            #return answer #Statement to return value (answer) back to user
        else: # odd numbers
            positiveNumber = (positiveNumber*3) + 1 #calculation after being defined as odd number
            print(" ", int(positiveNumber), end="")
            #return answer

collatz(positiveNumber)
