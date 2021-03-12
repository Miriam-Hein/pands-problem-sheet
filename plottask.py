# plottask.py
# The program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author: Miriam Heinlein

#import libraries 
import matplotlib.pyplot as plt 
import numpy as np

# the function, which is (x)=x, g(x)=x2 and h(x)=x3 here
x = np.array(range(0,5))
g = x**2
h = x**3

# plot the functions 
plt.plot(x, x, linestyle = "solid", color = "red", label="f(x)=x")
plt.plot(x, g, linestyle = "dashed",color = "purple", label="g(x)=x^2")
plt.plot(x,h, linestyle = "dotted", color = "green", label="h(x)=x^3")

# show the plot with title, labels and legend
plt.title("Functions f(x), g(x) & h(x)")
plt.xlabel("x-Axis")
plt.ylabel("y-Axis")
plt.legend()
plt.show()
