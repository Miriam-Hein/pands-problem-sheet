# plottask.py
# The program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author: Miriam Heinlein

#import libraries 
import matplotlib.pyplot as plt 
import numpy as np

# 100 linearly spaced numbers
x = np.arange(0,5,1)

# the function, which is (x)=x, g(x)=x2 and h(x)=x3 here
f = x
g = x**2
h = x**3

# setting the axes at the centre
fig = plt.figure(1)
ax = fig.add_subplot(1, 1, 1)
ax.spines['bottom'].set_position('zero')
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,g, 'r')

# show the plot
plt.show()