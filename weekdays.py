# weekdays.py
# This program outputs whether or not today is a weekday. 
# Author: Miriam Heinlein

# import Python's datetime module

import datetime

# Todays date and time
# code for testing: 
# x = datetime.datetime.now()
# currentWeekday = x.strftime("%A")
#print(currentWeekday)

#Output if today is weekday or weekend
weekNo = datetime.datetime.now().weekday()

if weekNo < 5:
    print("Yes, unfortunately today is a weekday.")
else:  # 5 Sat, 6 Sun
    print("It is the weekend, yay!")

