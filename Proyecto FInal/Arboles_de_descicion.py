import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
# Leer el DataFrame
df = pd.read_csv('Paises_meses_temperatura.csv')

# Seleccionar las columnas relevantes
meses = df.columns.tolist()
meses = meses[1:]  # Excluir la columna del país

# Dividir el DataFrame en características (X) y variable objetivo (y)
X = df[meses[:-1]]
y = df[meses[0]]  # Primer mes (enero)

# Normalizar los datos de las características
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)


# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.2, random_state=0)

# Crear una instancia del modelo de árboles de decisión
arbol = DecisionTreeRegressor()

# Entrenar el modelo con los datos de entrenamiento
arbol.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = arbol.predict(X_test)

# Evaluar el rendimiento del modelo
score = arbol.score(X_test, y_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('Coeficiente de determinación (R^2):', score)
print('Error cuadrático medio (MSE): {:.2f}'.format(mse))
print('r2: {:.2f}'.format(r2))
# Graficar los datos originales y la línea de la predicción
plt.scatter(X_test[:, 0], y_test, color='blue', label='Datos Originales')
plt.plot(X_test[:, 0], y_pred, color='orange', label='Predicción')
plt.xlabel('Temperatura de Diciembre')
plt.ylabel('Temperatura predicha para Enero')
plt.legend()
plt.show()
