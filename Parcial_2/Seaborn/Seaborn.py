# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:39:36 2023

@author: jonat
"""

import seaborn as sns
df = sns.load_dataset('diamonds')

# Grafico general de la distribucion de cada columna:
for i in df.columns:
    sns.displot(df[i])

# Gráfica de comparando color y price
sns.set_theme(style="white", palette="pastel")

sns.displot(df, x="price", 
            col="color", 
            row="clarity", 
            facet_kws=dict(margin_titles=True));