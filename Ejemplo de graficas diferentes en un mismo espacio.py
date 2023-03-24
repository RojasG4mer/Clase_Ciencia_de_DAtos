# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:39:58 2023

@author: jonat
"""
"""
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (5,3)

fig = plt.figure()
fig.add_subplot(241)
fig.add_subplot(242)
ax = fig.add_subplot(223)
ax.set_title("subplots")

fig.add_axes([0.77,.3,.2,.6])
ax2 =fig.add_axes([0.67,.5,.2,.3])
fig.add_axes([0.6,.1,.35,.3])
ax2.set_title("random axes")

plt.tight_layout()
plt.show()
"""
import matplotlib.pyplot as plt
import numpy as np
"""
# Create figure() objects
# This acts as a container
# for the different plots
fig = plt.figure()
  
# Generate line graph
x = np.arange(0, 1.414*2, 0.05)
y1 = np.sin(x)
y2 = np.cos(x)
  
# Creating two axes
# add_axes([xmin,ymin,dx,dy])
axes1 = fig.add_axes([0, 1, 1, 1])
axes1.plot(x, y1)
axes2 = fig.add_axes([1, 1, 1, 1])
axes2.plot(x, y2)
  
# Show plot
plt.show()
"""




