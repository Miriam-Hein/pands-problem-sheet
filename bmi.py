# bmi.py
# This program calculates somebody's Body Mass Index (BMI)
# Author: Miriam Heinlein

height = float (input ("Enter your height in meters:"))
weight = float (input ("Enter your weight in kg:"))

bmi = weight/(height**2) # ** is the power of operator ie height*height

print ("Your calculated BMI is", bmi )