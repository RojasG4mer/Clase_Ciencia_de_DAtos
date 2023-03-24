# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:16:14 2023

@author: Jonathan Francisco Rojas Martinez
"""

#--librerias
import numpy as np

### Creamos la matriz del ejercicio anterior:
a = np.zeros((8, 8))
n = 1
for i in range(0, len(a[0])):
  for j in range(0, len(a[0])):
    a[i][j] = n
    n += 1
# Creamos la matriz propuesta:
d = np.linspace(0.4, 0.79, 40)
d = d.reshape(8, 5)
# Parte 2
# Concatenar d y a
concatenaDAs = np.concatenate((a, d), axis=1)
# Parte 3
# Agregar una fila al final con el promedio de cada columna
promcolu = np.mean(concatenaDAs, axis = 0) 
con_prom = np.concatenate((concatenaDAs.reshape(8, 13), promcolu.reshape(1, 13)), axis = 0)
# Parte 4 
# Maximos de cada fila
maxis = np.max(con_prom, axis = 1)
con_max = np.concatenate((con_prom.reshape(9, 13), maxis.reshape(9, 1)), axis = 1)
print(con_max)
# Parte 5
# Guardar en un archivo:
np.savetxt('datos.csv', con_max, delimiter=',', fmt='%.3f', header="Col1,Col2,Col3,Col4,Col5,Col6,Col7,Col8,Col9,Col10,Col11,Col12,Col13,Col14")
