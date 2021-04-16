# squareroot.py
# This program takes a positive floating-point number as input and return the approximate square root of a number using Newtons method  
# Author: Miriam Heinlein

# User Input - positive number with decimal point using the float format
n = float(input ("Please enter a positive number: "))

#sqrt function to cacluate the approx. square root of n (user input (positive number))
def newtonSqrt(n): 

    # Setting variables
    approx = 0.5 * n # for example n = 10 --> 5
    root = 0.5 * (approx+(n/approx)) # root with n=10 is 3.5
  
    while root !=approx: # Executes the while loop until the approximation is equal to the root 
        
        approx = root # every time approx will be changed to root, in example to 3.5 until finally the values align --> return
        root =  (approx +(n/approx))/2  # 0.5 * or /2 is the same 
    return approx

# Output returning approx. square root with one decimal digit
print ("The square root of", n, "is approx. {:.1f}".format(float(newtonSqrt(n)))) 