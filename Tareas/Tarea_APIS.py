# -*- coding: utf-8 -*-
"""
Created on Tue May  9 10:41:09 2023

@author: jonat
"""

import requests
import pandas as pd

# URL base de la API de Wikipedia
WIKI_API_URL = 'https://es.wikipedia.org/w/api.php'

# Parámetros para la consulta
params = {
    'action': 'query',
    'format': 'json',
    'list': 'search',
    'srsearch': 'astro',
    'srprop': 'snippet',
    'srlimit': '20',
}

# Realizamos la consulta
response = requests.get(WIKI_API_URL, params=params)

# Extraemos los resúmenes y creamos el dataframe
data = []
for result in response.json()['query']['search']:
    pageid = result['pageid']
    title = result['title']
    summary = result['snippet']
    contains_word = 1 if 'física' in summary or 'ciencia' in summary else 0
    data.append((pageid, title, summary, contains_word))

df = pd.DataFrame(data, columns=['pageid', 'titulo', 'resumen', 'contiene_palabra'])

# Mostramos el dataframe
print(df.head())
