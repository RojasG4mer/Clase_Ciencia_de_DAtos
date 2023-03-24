# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:19:01 2023

@author: Jonathan Francisco Rojas Martinez
"""
import numpy as np
import matplotlib.pyplot as plt


x_1 = np.linspace(5, 15, 10)
x_2 = np.linspace(0, 21, 2)
x_3 = np.linspace(5, 15, 2)
x_4 = np.linspace(5, 15, 5)
x_5 = np.linspace(5, 15, 100)

y_1 = 4 * x_1**2
y_2 = x_2 * (np.random.randint(0,10,len(x_2))) + 100
y_3 = x_3**(np.random.randint(0, 10, len(x_3)))
y_4 = np.cos(x_4)
y_5 = np.sin(x_5)




fig = plt.figure()


axes1 = fig.add_axes([0, 2, 3, 2])
axes1.plot(x_1, y_1)
axes2 = fig.add_axes([0, 1, 2, 1])
axes2.plot(x_2, y_2)
axes3 = fig.add_axes([0, 0, 1, 1])
axes3.plot(x_3, y_3)
axes4 = fig.add_axes([1, 0, 1, 1])
axes4.plot(x_4, y_4)
axes5 = fig.add_axes([2, 0, 1, 2])
axes5.plot(x_5, y_5)

# Show plot
plt.show()


"""
plt.plot(x_1, y_1)
plt.plot(x_2, y_2)
plt.plot(x_3, y_3)
plt.plot(x_4, y_4)
plt.plot(x_5, y_5)
plt.grid()
plt.show()
"""
""" -------------------------------------------
UN BIN ES EL NUMERO DE CLASES PARA UNA GRÁFICA 
------------------------------------------- """ 





