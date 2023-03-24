# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 14:45:07 2023

@author: Rojas Martínez Jonathan Francisco
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import gaussian_filter
# Importamo las imagen de la luna: 
imagen = Image.open('dunkleosteus.jfif')
## imagen
# Hacemos un array a la Imagen
im_datos = np.array(imagen)
"""
print(np.max(im_datos[234][567]))
print(im_datos.shape[0])
print(len(im_datos[1]))
"""
im_datos.shape
for i in range(0, im_datos.shape[0]):
    for j in range(0, im_datos.shape[1]):
        maximus = np.max(im_datos[i][j])
        im_datos[i][j] = np.array([maximus, maximus, maximus])

smooth = gaussian_filter(im_datos, 20, order=0, mode='nearest')

fig,ax = plt.subplots(figsize=(6,6))
ax.imshow(smooth)
ax.set_xticks([])
ax.set_yticks([]);

fig, ax = plt.subplots(figsize=(6,6))
plt.axis("off") # Quitar los ejes de la imagen
ax.imshow(im_datos)
plt.show()