# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:21:05 2023
@author: Rojas Martínez Jonathan Francisco
"""

import numpy as np
import pandas as pd
import string
#funcion para que me de el alfabeto
def listAlphabet():
  return list(string.ascii_lowercase)
#Función para hacer una lista al revés
def listarevez(lista):
    revez = []
    for item in reversed(lista):
        revez.append(item)
    return revez

alfabeto = listAlphabet()

### Serie A
numeros = np.linspace(10, 9+len(alfabeto), len(alfabeto))
## Generamos la serie A
A = pd.Series(data=numeros, index=alfabeto, dtype='int')

### Serie B
letrasrevez = listarevez(alfabeto)
## Generamos la serie B
B = pd.Series(data=numeros, index=letrasrevez, dtype='int')

### Tomar los valores entre d e i (d:i)
dei = ['d', 'e', 'f', 'g', 'h', 'i']

print(A['d':'i'])
print(B[dei])





