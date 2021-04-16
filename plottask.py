# plottask.py
# The program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author: Miriam Heinlein

#imported libraries 
import matplotlib.pyplot as plt 
import numpy as np
import sys 

# the function, which is f(x)=x, g(x)=x^2 and h(x)=x^3 here
x = np.array(range(0,5,1))
g = x**2
h = x**3

# plot the functions 
plt.plot(x, x, linestyle = "solid", color = "red", marker = "o", label="f(x)=x")
plt.plot(x, g, linestyle = "solid",color = "purple",marker = "o", label="g(x)=x^2")
plt.plot(x,h, linestyle = "solid", color = "green", marker = "o", label="h(x)=x^3")

# show the plot with title, labels and legend
plt.title("Functions f(x), g(x) & h(x)")
plt.xlabel("x-Axis")
plt.ylabel("y-Axis")
plt.legend(loc = "upper left")
plt.grid()

# Save this plot as a file  
plt.savefig('plottask.png') 
plt.show ()