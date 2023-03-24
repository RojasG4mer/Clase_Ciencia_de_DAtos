# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 14:38:53 2023

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
roj0 = np.array(imagen)
az0l = np.array(imagen)
verd0 = np.array(imagen)

x=np.linspace(250, 1250, 10)

for i in range(0, len(im_datos[1])):
    for j in range(0, len(im_datos[0])):
        roj0[i][j][0] = 0

for i in range(0, len(im_datos[1])):
    for j in range(0, len(im_datos[0])):
        az0l[i][j][1] = 0

for i in range(0, len(im_datos[1])):
    for j in range(0, len(im_datos[0])):
        verd0[i][j][2] = 0


fig,ax = plt.subplots(figsize=(6,6))
ax.imshow(roj0)
plt.show()
fig,ax = plt.subplots(figsize=(6,6))
ax.imshow(az0l)
plt.show()
fig,ax = plt.subplots(figsize=(6,6))
ax.imshow(verd0)
plt.show()
