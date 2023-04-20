# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 15:52:29 2023

@author: Rojas Martínez Jonathan Francisco
"""
### Mapa de mexico

"""
Ejercicio:
    - Cambiar mapa de color
    - Aplicar log a la escala de colores

"""

#### Código sirviendo
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
import seaborn as sns



## CSV con los datos de México
df = pd.read_csv('Motalidad_final.csv', encoding='latin1')
df.info()

ono = pd.read_csv('Mortalidad_anios.csv')
ono.info()

#### Usando Seaborn para gráficas generales

## Comparando las distribuciones de las 3 columnas
"""
sns.boxplot(data=ono, x="Entidad federativa", y="2018", palette='rainbow')
sns.jointplot(data = ono, x = "2018", y = "2019", kind="kde")
sns.displot(ono['2020'])
sns.pairplot(ono)
sns.violinplot(data=df, x="Entidad federativa", y="Total", palette='plasma')
"""
### GeJSON de México
countries_geo = f'mexicoHigh.json'

data_map = df[['Entidad federativa', 'Total']].copy()

data_map = pd.DataFrame(data_map).reset_index()
data_map.head()

m = folium.Map(location=[22, -50], zoom_start=2, width='100%', height='100%',position='bottomLeft')

folium.Choropleth(
    geo_data=countries_geo,
    name='choropleth',
    data=data_map,
    locations='Entidad federativa',
    #featureidkey='properties.name',
    key_on='feature.properties.name', # Decimos como encontrar el nombre del estado/país/etc.
    columns=['Entidad federativa', 'Total'], ## Debemos poner la columna de el nombre del pais y luego la del valor
    fill_color='YlGnBu', #'BuPu',
    fill_opacity=0.9,
    line_opacity=0.2,
    nan_fill_color='white',
    line_color="purple", 
    line_weight=1,
    legend_name='Tasa de Mortalidad 2018',
).add_to(m)

folium.LayerControl().add_to(m)

m.save("onichan.html")



