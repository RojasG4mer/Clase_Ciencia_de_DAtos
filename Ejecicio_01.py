# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 18:42:49 2023

@author: Jonathan Francisco Rojas Martínez
"""
# Librerias necesarias para los archivos csv
import csv
f = []
with open("lista_correos.csv", newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        f.append(str(row))
#print(f)
#f = ["carrillocl2019@licifug.ugto.mx", "veronicamc1223@gmail.com", 
     #"alvarezcu2019@licifug.ugto.mx","uridedomjua@gmail.com", 
     #"hernandeztj2019@licifug.ugto.mx", "serart_98@hotmail.com"]
n = []
# Separamos por el @ que tienen todos los correos:
for i in range(0, len(f)):
    n.append(f[i].split("@"))
#print(n)

# Separamos la parte que contiene "."
for i in range(0, len(f)):
    #n[i][i].split(".")
        n[i][1] = n[i][1].split(".")
#print(n)

#Creamos un set con todos los dominios que hayan:
dom = {0}
for i in range(0, len(f)):
    dom.add(n[i][1][0])
#print(dom)
dom.discard(0)
hl = list(dom)
print("Dominios de los correos: ", hl)
# Leer vocales:
#for i in range(0, len(f)):
    #print((n[i][0]+"".join(n[i][1])).count("a"))
#print("".join(n[0][1])+n[0][0])

#Creación del nuevo documento con usuario y los valores de las letras:

cols = ['Usuario', 'Letras "a"','Letras "e"','Letras "i"', 'Letras "o"', 'Letras "u"']
rows = []
for i in range(len(f)):
  #Debemos crear las listas de usuario y de los valores de las letras al mismo tiempo:
  aux = []
  #ver al usuario:
  aux.append(n[i][0])
  #Letras:
  aux.append((n[i][0]+"".join(n[i][1])).count("a"))
  aux.append((n[i][0]+"".join(n[i][1])).count("e"))
  aux.append((n[i][0]+"".join(n[i][1])).count("i"))
  aux.append((n[i][0]+"".join(n[i][1])).count("o"))
  aux.append((n[i][0]+"".join(n[i][1])).count("u"))
  #aux.append(hl[i])
  rows.append(aux)
  

print(rows)
with open("pruebas.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(cols)
    csvwriter.writerows(rows)


