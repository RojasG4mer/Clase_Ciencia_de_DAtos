import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
# Leer el DataFrame
df = pd.read_csv('Paises_meses_temperatura.csv')
df
## Columnas del df
meses = df.columns.tolist()
meses = meses[1:]
# Seleccionar las columnas relevantes, incluyendo los meses anteriores y el mes objetivo
# Dividir el DataFrame en características (X) y variable objetivo (y)
X = df[meses[0]]
X = np.reshape(X.values, (-1, 1))
X = pd.DataFrame(X.squeeze())
y = df[meses[-1]]
y = np.reshape(y.values, (-1, 1))
y = pd.DataFrame(y.squeeze())
# Normalizar los datos de las características
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.2, random_state=0)

# Crear una instancia del modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el rendimiento del modelo
score = model.score(X_test, y_test)
print('Coeficiente de determinación (R^2):', score)

# Calcular el error cuadrático medio (MSE) de las predicciones
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
# Imprimir el MSE
print('Error cuadrático medio (MSE): {:.2f}'.format(mse))
print('r2: {:.2f}'.format(r2))
print('coeficiente:', model.coef_)
print('intercepto:', model.intercept_)

m = model.coef_
b = model.intercept_
z = np.linspace(X.min(), X.max(), 100)

fig, ax = plt.subplots(figsize=(6,6))
ax.plot(X, y, 'ob', alpha=0.3)
ax.plot(z, m*z + b, ls='--', color='orange', lw=2)
plt.plot(X_test, y_pred, '^', color='orange', ms=8)
ax.set_xlabel('BMI')
ax.set_ylabel('disease progression')
plt.show()
