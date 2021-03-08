# collatz.py
#The program takes the user's input (positive integer) and prints the successive values after being calculated.
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
#The program ends if the value is one.
# Author: Miriam Heinlein

#Calculate 
def collatz(number): #beginning of function
    
        if (number % 2) == 0: #even number (even numbers are dividable by 2 without any remainder, so if remainder it proceeds to else)
            answer = int(number/2) #calculation after being defined as even number
            print(answer, end=" ")
            return answer #Statement to return value (answer) back to user
        else: # odd numbers
            answer = int((number*3) + 1) #calculation after being defined as odd number
            print(answer, end=" ")
            return answer

#User Input
positiveNumber = int(input ("Please enter a positive number: ")) 

# 
while positiveNumber != 1:
        positiveNumber = collatz(int(positiveNumber))
