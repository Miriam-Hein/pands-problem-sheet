# bmi.py
# This program calculates somebody's Body Mass Index (BMI)
# Author: Miriam Heinlein

height = float (input ("Enter your height in meters:"))
weight = float (input ("Enter your weight in kg:"))

bmi = weight/(height**2) # ** is the power of operator ie height*height

print ("Your calculated BMI is", bmi )

# Different approach - enter height in cm and convert cm to meters 

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
BMI = weight / (height/100)**2 #height/100 converts cm in meters

print(f"You calculated BMI is {BMI}") #enclose your variable within the {} to display it's value in the output (string formatting)