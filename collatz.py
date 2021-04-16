# collatz.py
# The program takes the user's input (positive integer) and prints the successive values after being calculated.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# The program ends if the value is one.
# Author: Miriam Heinlein

#User Input saved in variable positiveNumber
positiveNumber = int(input ("Please enter a positive number: ")) 

#Calculate using a while loop and if/else statements
def collatz(positiveNumber): #Beginning of function
    
    while positiveNumber != 1: #Continue function until positiveNumber equals 1
        if (positiveNumber % 2) == 0: #even number (even numbers are dividable by 2 without any remainder, so if remainders it proceeds to else otherwise it ends the function)
            positiveNumber = positiveNumber//2 #calculation after being defined as even number
            
            #Output to user in horizontal line with spaces between the caculated values
            print(" ", int(positiveNumber), end="")
            
        else: # odd numbers
            positiveNumber = (positiveNumber*3) + 1 #calculation after being defined as odd number
            
             #Output to user in horizontal line with spaces between the caculated values
            print(" ", int(positiveNumber), end="")

# Calling the fuction
collatz(positiveNumber)
