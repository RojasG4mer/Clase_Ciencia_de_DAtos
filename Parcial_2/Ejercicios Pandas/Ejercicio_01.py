# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 15:20:43 2023

@author: jonat
"""

import pandas as pd
import numpy as np


## Leemos el archivo:

df = pd.read_csv('GCB2022v27_percapita_flat.csv')

## Explorando el data set:
# Datos generales
Datos_gen = df.describe()
print(Datos_gen)
# Columnas del df
columnas = df.columns
print(columnas)

## Buscamos los datos sobre México (de la columnas country queremos los datos 
### de México)
Data_mx = df[df[columnas[0]] == 'Mexico']
Datos_gen_mx = Data_mx.describe()
Indices_data_gen = Datos_gen_mx.index
colum_da_ge = Datos_gen_mx.columns
## Comparando con el mundo
# promedio de consumo de oil del mundo:
print(Datos_gen['Oil'].loc['mean'])
print(Datos_gen_mx['Oil'].loc['mean'])
tempy = []
general = []

for i in Indices_data_gen:
    tempy.clear()
    for j in colum_da_ge:
        print('La diferencia de ' + str(i) + "es de :" + str(Datos_gen[j].loc[i] - Datos_gen_mx[j].loc[i]))
        tempy.append(Datos_gen[j].loc[i] - Datos_gen_mx[j].loc[i])
    #print(tempy)
    general.append(tempy)
print(general)
diferencias = pd.DataFrame(data = general, index = Indices_data_gen, columns = colum_da_ge)
print(diferencias)
