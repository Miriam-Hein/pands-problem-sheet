# es.py
# This program reads in a text file and outputs the number of e's it contains.
# Author: Miriam Heinlein


#f = open("moby-dick.txt", "r")
#print(f.read(5))


# explit function to return the letter count 
def letterFrequency(fileName, letter): 
    
    file = open("moby-dick.txt", 'r') # open file in read mode 
  
    
    text = file.read() # store content of the file in a variable 
  
    
    return text.count(letter) # using count() 
  
  
# call the function and display the letetr count 
print(letterFrequency('moby-dick.txt', 'e')) 