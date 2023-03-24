# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 16:08:54 2023

@author: Rojas Martinez Jonathan Francisco
"""
# Librerias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## Leemos el archivo:
df = pd.read_csv('GCB2022v27_percapita_flat.csv')
## -------Explorar el dataset:----------------------------------------------
# Explorar nombres de columnas
columnas = df.columns
# Tipo de datos de las columnas
tipos_datos = df.dtypes
# Distribucion de NANS
info_nans = df.info()
# Datos_gen = df.describe()
no_nans = df.isna().sum(axis = 0)

# ¿De cuántos países diferentes hay fotos?
data_general = df.describe()

# Graficar los valores globales y los de Mexico para: 'Total', 'Coal', 'Oil', 'Gas', 'Cement', 'Flaring', 'Per Capita'.
Data_mx = df[df[columnas[0]] == 'Mexico']
## Escogemos los valores de Mexico para eliminarlos
##### filas_mex = df[df['Country'] == 'Mexico'].index
### Data_global = df.drop(df[df['Country'] == 'Mexico'].index) ## Datos sin méxico
Data_global = df.loc[df['Country'] == 'Global']
#uwu = Data_global['Country'].unique()
# Promedio de los datos de cada día a nivel mundial
fechas = df['Year'].unique()
paises = df['Country'].unique()
#prom_globales = []
# A = Data_global[(Data_global['Year'] == fechas[0]) & (Data_global[columnas[0]])]
# A = Data_global[Data_global['Year'] == fechas[0]]

## Graficas

fig = plt.figure(figsize = (25, 20))
fig.tight_layout()

for i in range(1, 7):
    ax = plt.subplot(3, 3, i)
    ax.scatter(fechas, Data_mx[columnas[i+2]], color = 'blue', label = 'México', s=5)
    ax.scatter(fechas, Data_global[columnas[i+2]], color = 'red', label = 'Globa', s=5)
    ax.set_xlabel('Años')
    ax.set_ylabel(columnas[i+2])
    ax.set_title('México vs World ' + '"' + columnas[i+2] + '"')
    ax.legend()

ax = plt.subplot(3, 3, 9)
ax.scatter(fechas, Data_mx[columnas[9]], color = 'blue', label = 'México', s=5)
ax.scatter(fechas, Data_global[columnas[9]], color = 'red', label = 'Global', s=5)
ax.set_xlabel('Años')
ax.set_ylabel(columnas[7])
ax.set_title('México vs World ' + '"' + columnas[9] + '"')
ax.legend()

"""    
for i in range(3, len(columnas)):
    plt.xlabel('Años') 
    plt.ylabel(columnas[i])
    plt.scatter(fechas, Data_mx[columnas[i]], color = 'blue', label = 'México', s=5)
    plt.scatter(fechas, Data_global[columnas[i]], color = 'red', label = 'Global', s=5)
    plt.title('México vs World ' + '"' + columnas[i] + '"')
    plt.legend()
"""

"""
Extraer datos de los países pertenecientes al G20 y graficar las columnas del punto anterior.
- Cuales son los 3 países que más contaminan en cada uno de los casos?
- Considerando solo la emisión de los paises del G20, con que porcentaje contribuye México al Total y Per Capita?
"""

G_20_paises = ['Germany', 'Saudi Arabia', 'Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'USA', 'France', 'India', 'Indonesia', 'Italy', 'Japan', 'United Kingdom', 'South Korea', 'Mexico', 'Russia', 'South Africa', 'Turkey', 'Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden']
len(G_20_paises)
#Datos_g20 = df[df[columnas[0]] == G_20_paises[0]]
Datos_g20 = df[df[columnas[0]] == G_20_paises[0]]
## Funcion para darme los máximos de cada columnas necesaria
columna_req = ['Total', 'Coal', 'Oil', 'Gas', 'Cement', 'Flaring', 'Other']
def max_columns(df, list_columns):
    maxis = []
    posiciones_max = []
    for col in list_columns:
        columnas_usada = df[col]
        sorted_col_indices = columnas_usada.argsort()[::-1][:3]
        maxis.append([columnas_usada.idxmax(), col])
        posiciones_max.append(sorted_col_indices)
    return maxis
maximos = max_columns(Datos_g20, columna_req)
Datos_g = df[df[columnas[0]] == G_20_paises[1]]
maximose = max_columns(Datos_g, columna_req)
un = maximos + maximose
#Datos_g20[maximos[0]]
#Datos_g20.max(Datos_g20)
print(maximos)
# maxis me regresa una lista y quisiera agregar elemento por elemento
for i in range(1, len(G_20_paises)):
    aux = max_columns(df[df[columnas[0]] == G_20_paises[i-22]], columna_req)
    maximos += aux
    Datos_g20 = pd.concat([Datos_g20, df[df[columnas[0]] == G_20_paises[i]]])
Datos_g20.drop_duplicates(inplace=True) #Elimnamos filas duplicadas
# Paises que contaminan más de cada columna-----------------------------------
maxis = []
nums = []
for j in range(0, 7):
    aux = []
    for i in range(j, 167, 7):
        aux.append([Datos_g20.loc[maximos[i][0], maximos[i][1]], maximos[i]])
    aux = sorted(aux, key=lambda x: x[0], reverse=True)
    maxis.append([aux[0], aux[1], aux[2]])
aux = []   
for i in range(0, 7):
    for j in range(0, 3):
        nums.append([maxis[i][j][0]])
        aux.append(Datos_g20.loc[maxis[i][j][1][0], 'Country'])
## maxis es la lista donde están los pasises que contaminaron más de cada columna

## Crear un dataframe donde estén colocados los máximos con su país correspondiente y valor de la columna
indices = np.reshape(['Primero', 'Segundo', 'Tercero'], (3, 1))

nums = np.reshape(nums, (7,3)).T
aux = np.reshape(aux, (7, 3)).T
Diccionario = {'Indices' : ['Primero', 'Segundo', 'Tercero']}
maxis = []
for i in range(0, 7):
    maxis = []
    for j in range(0, 3):
        maxis.append([nums[j][i], aux[j][i]])
    for k in range(0, 3):
        Diccionario[columna_req[i]] = maxis
     
maximos_df = pd.DataFrame(Diccionario) 
maximos_df = maximos_df.set_index('Indices') ## DF que tiene países que más contaminan

#xdddd = Datos_g20[columnas[2] == Datos_g20[G_20_paises[0]]]
xddd = Datos_g20.loc[Datos_g20['Country'] == G_20_paises[0], columnas[3] ]

# --------- GRAFICAS G20 ----------------------------------------------------
fig = plt.figure(figsize = (25, 20))
fig.tight_layout()

for i in range(1, 7):
    ax = plt.subplot(3, 3, i)
    for j in range(0, 46):
        ax.scatter(fechas, Datos_g20.loc[Datos_g20['Country'] == G_20_paises[j], columnas[i+2]], label = G_20_paises[j], s=5)
    #ax.scatter(fechas, Data_global[columnas[i+2]], color = 'red', label = 'Globa', s=5)
        ax.set_xlabel('Años')
        ax.set_ylabel(columnas[i+2])
        ax.set_title('México vs World ' + '"' + columnas[i+2] + '"')
        ax.legend()

ax = plt.subplot(3, 3, 9)
ax.scatter(fechas, Data_mx[columnas[9]], color = 'blue', label = 'México', s=5)
ax.scatter(fechas, Data_global[columnas[9]], color = 'red', label = 'Global', s=5)
ax.set_xlabel('Años')
ax.set_ylabel(columnas[7])
ax.set_title('México vs World ' + '"' + columnas[9] + '"')
ax.legend()



# Unir los DataFrames
# df_union = pd.concat([Datos_g20, df[df[columnas[0]] == G_20_paises[1]]])

# Eliminar NaNs.

# Aplicar merge, groupby





