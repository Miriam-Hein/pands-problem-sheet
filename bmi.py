# bmi.py
# This program calculates somebody's Body Mass Index (BMI) using the users inputted height in cm or meters and weight in kg
# Author: Miriam Heinlein

# Assigning value to variable inputted by the user
height = float (input ("Enter your height in meters: ")) #float format as real numbers used with decimal points used ie 1.60 
weight = float (input ("Enter your weight in kg: "))

# BMI calculation 
bmi = weight/(height**2) # ** is the power of operator ie height*height

# Program output visible by the user
print ("You calculated BMI is {:.2f}".format(bmi))


# Different approach - enter height in cm and convert cm to meters 

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

# BMI calculation
BMI = weight / (height/100)**2 #height/100 converts cm in meters

# Program output visible by the user
print("You calculated BMI is {:.2f}".format(BMI)) #BMI result shown with 2 decimal digits