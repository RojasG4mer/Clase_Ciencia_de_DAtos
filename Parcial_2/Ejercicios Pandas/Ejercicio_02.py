# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:16:04 2023

@author: Rojas Martinez Jonathan Francisco
"""
# librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

n = 100
a = np.random.randn(n,2)*300 + 1000
b = nums = np.random.randint(100, 3000, (n, 2))
c = np.append(a, b, axis=1)

#nums = np.random.randint(100, 3000, (20, 4))
nums = np.random.randn(n,4)
letters = np.reshape(list("abcd")*int(n/4), (n,1))
values = np.append(c, letters, axis = 1)
fecha = pd.date_range("20230915", periods=n)

df = pd.DataFrame(values, index=fecha, columns=list("VWXYZ"))
types_dict = {}
for i in df.columns[0:-1]:
    types_dict.update({i : 'float64'})

df = df.astype(types_dict)

df.head()


uwu = df.groupby('Z').sum()

ono = df.groupby('Z').sum().T # Invertir un dataframe
efer = df.groupby('Z').sum().T.plot.bar(stacked = True)
