# es.py
# This program reads in a text file and outputs the number of e's it contains.
# Author: Miriam Heinlein


# explicit function to return the letter count 
def letterFrequency(fileName, letter): 
    
    f = open("moby-dick.txt", 'r') #open file in read mode 
  
    
    text = f.read() # store content of the file in a variable 
  
    
    return text.count(letter) # using count() 
  
  
# call the function and display the letter count 
print(letterFrequency('moby-dick.txt', 'e')) 