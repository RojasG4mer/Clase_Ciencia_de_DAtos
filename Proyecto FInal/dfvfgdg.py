import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Leer el DataFrame de temperaturas por país y mes
df = pd.read_csv('Paises_meses_temperatura.csv')

# Obtener las columnas correspondientes a los meses
meses = df.columns[1:]

# Seleccionar las columnas relevantes para X y y
X = df[meses[0]].values.reshape(-1, 1)
y = df[meses[1]].values.reshape(-1, 1)

# Aplicar transformación polinómica a la variable X
poly_features = PolynomialFeatures(degree=2)
X_poly = poly_features.fit_transform(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=0)

# Crear una instancia del modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el rendimiento del modelo
score = model.score(X_test, y_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Imprimir las métricas de evaluación
print('Coeficiente de determinación (R^2):', score)
print('Error cuadrático medio (MSE): {:.2f}'.format(mse))

# Graficar los datos originales y la línea de regresión
plt.scatter(X, y, color='blue', label='Datos Originales')
plt.plot(X_test[:, 1], y_pred, color='red', label='Línea de Regresión')
plt.xlabel('Temperatura del Mes Anterior')
plt.ylabel('Temperatura del Mes Actual')
plt.title('Regresión Polinómica')
plt.legend()
plt.show()
