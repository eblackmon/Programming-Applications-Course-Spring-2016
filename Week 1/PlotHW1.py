#import numpy and matlibplots module

import numpy as np
import matplotlib.pyplot as plt

#generate array of x values from 0 to 6pi

pi = 3.14159
myX = np.linspace(0, 6*pi, num = 100)

#calculate y values for sin wave

ySin = np.sin(myX)

#calculate y values for cosine wave

yCos = np.cos(myX)

#plot x and y values for both functions
#set dashed line for sine wave and solid line for cosine wave

line1, = plt.plot(myX,ySin, label = "sin(x)", linestyle = '--')
line2, = plt.plot(myX,yCos, label = "cos(x)", linewidth = 4)

#add legend
plt.title('Homework 1')
first_legend = plt.legend(handles=[line1], loc=1)
ax = plt.gca().add_artist(first_legend)
second_legend = plt.legend(handles=[line2], loc=4)
plt.xlabel('x')
plt.ylabel('sin(x) and cos(x)')
plt.show()

#Name: Elise Blackmon
#Date: 1/21/16:

