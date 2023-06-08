# -*- coding: utf-8 -*-
"""
@author: Rojas Martínez Jonathan Francisco
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import seaborn as sns

# Configuración del backend de Plotly para Spider
pio.renderers.default = 'browser'

df = pd.read_csv('worlds all cities with their avg temp - Sheet1.csv')

### -------------- Exploramos el dataframe ----------------------------------
# Valores del inicio
df.head()
# Columnas del dataframe
columnas = df.columns.tolist()
# Valores únicos de las columnas 'Country' y 'City'
Paises = df[columnas[0]].unique()
Ciudades = df[columnas[1]].unique()
df.describe()
## Vemos el tipo de datos que son las columnas:
df.dtypes
## Vemos una informacion general de los datos

# Vemos que las columnas de la temperatura tienen datos de tipo string y además
## están en Celsius (primer número) y Fahrenheit (segundo número), así que primero
## separamos el primer número para usar este tipo de escala de temperatura:
for i in range(len(df)):
    for j in range(2, 15):
        df.iloc[i, j] = float(df.iloc[i, j].split('\n')[0].replace('−', '-'))
df = df.iloc[:, :-2]
print(df)

## Ahora volvemos a pedir un resumen general de las columnas:
print(df.info())

# Vemos que no hay ningún NaN en el dataframe, así que ahora vamos a ver cómo
# se ven las temperaturas de cada mes por cada país. Primero, agrupamos los datos por países, quitando las ciudades.
# Quitamos la columna de ciudades:
df_sinciudades = df.drop(columns=['City'], axis=1)
Paises_agrupados = df_sinciudades.groupby(columnas[0]).mean()
Paises_agrupados.to_csv('Paises_meses_temperatura.csv')
print(Paises_agrupados)
## Ahora hacemos la transpuesta del dataframe para poder graficar los países con respecto a la temperatura del mes:
Paises_agrupados = Paises_agrupados.T
Paises_agrupados = Paises_agrupados[1:]

print(Paises_agrupados)

fig = make_subplots(specs=[[{"secondary_y": False}]])

for pais in Paises:
    fig.add_trace(go.Scatter(x=Paises_agrupados.index, y=Paises_agrupados[pais], name=pais, mode='lines'), secondary_y=False)

fig.update_layout(autosize=False, width=900, height=600, title="Temperatura C")
fig.update_xaxes(title_text="Mes")
fig.update_yaxes(title_text="Temperatura C", secondary_y=False)

fig.show()

## Hacemos una matriz de correlaciones para ver como se relacionan las diferentes columnas entre si
m_correlaciones = Paises_agrupados.corr()
print(m_correlaciones)

# Crear un gráfico de mapa de calor (heat map)
plt.figure(figsize=(100, 100))
sns.heatmap(m_correlaciones, annot=True, cmap="coolwarm", square=True, vmin=-1, vmax=1)
plt.title('Matriz de Correlaciones')
plt.xlabel('Mes')
plt.ylabel('País')
plt.show()




