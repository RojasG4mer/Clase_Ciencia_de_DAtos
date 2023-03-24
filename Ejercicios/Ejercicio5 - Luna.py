# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 14:26:15 2023

@author: Rojas Martinez Jonathan Francisco
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
# Importamo las imagen de la luna: 
imagen = Image.open('lunauwu.jpg')
## imagen
# Hacemos un array a la Imagen
im_datos = np.array(imagen)

x=np.linspace(250, 1250, 10)
"""
fig,ax = plt.subplots(figsize=(6,6))
ax.imshow(im_datos)
ax.plot(x,x, color='r', ls=':', lw=3)
plt.show()
"""
for i in range(0, len(im_datos[1])):
    for j in range(0, len(im_datos[0])):
        if (np.array_equal(im_datos[i][j], np.array([0, 0, 0]), equal_nan=False) ):
            im_datos[i][j] = np.array([153, 255, 153])

fig,ax = plt.subplots(figsize=(6,6))
ax.imshow(im_datos)
## ax.plot(x,x, color='r', ls=':', lw=3)
plt.show()

#print(im_datos[1000][456])
