# es.py
# This program reads in a text file and outputs the number of e's it contains.
# Author: Miriam Heinlein

# Import library (System-specific parameters and functions)
import sys


# Function to read letter e in the file from  an arugment in the command line
def readText(): 
    with open(sys.argv[1], "r") as f: #sys.argv reads the textfile from the command line whereby argv [1] refers to file names passed as argument to the function in index 1
         text = f.read() # store content of the file in a variable 
         totalEs = text.count('e') #counts the e's in the textfile and stores them in the variable totalEs
# Display the number of e's counted 
    print(totalEs) 
  
# Calling function
readText()