# squareroot.py
# This program takes a positive floating-point number as input and return the approximate square root of a number using Newtons method  
# Author: Miriam Heinlein

#sqrt function
def sqrt(n, l) : 

    # Assuming the sqrt of n and x_i 
    x = positiveNumber  
  
    # To count the number of iterations  
    count = 0 
  
    while (1) :  
        count += 1 
  
        # Calculate more closed x  
        root = (x + (positiveNumber / x))/2  
  
        # Check for closeness  
        if (abs(root - x) < l) : # if the absolute value(postive) of root minus the user's input is smaller than defined l (0.1) stop the loop and return output otherwise continue
            break 
  
        # Update root  
        x = root 
  
    return root
   
  
# User Input - positive number
positiveNumber = float(input ("Please enter a positive number: "))

#defined when to stop approximity of square root, in this case once the value goes below 0.1 return output
l = 0.10 

#Output 
print ("The square root of", positiveNumber, "is approx.", sqrt(positiveNumber,l))

#print("The square root of {} is approx. {}.".format(num, round(sqrt(num),1)))