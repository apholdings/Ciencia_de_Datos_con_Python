# House Prices: Advanced Regression Techniques

## Actividad - Implementación de modelos básicos de aprendizaje automático en un conjunto de datos.

Aquí hay un ejemplo de cómo podríamos aplicar un modelo de aprendizaje automático al conjunto de datos de precios de casas.

Primero, importamos las bibliotecas necesarias y cargamos los datos:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cargamos el conjunto de datos
df = pd.read_csv('house_prices.csv')

# Mostramos las primeras 5 filas del conjunto de datos
print(df.head())
```

A continuación, realizamos algunas operaciones de preprocesamiento de datos. En este caso, vamos a eliminar las columnas que no vamos a utilizar, a tratar los datos faltantes y a codificar las variables categóricas:

```python
# Eliminamos las columnas que no vamos a utilizar
df = df.drop(['Id', 'Alley', 'FireplaceQu', 'PoolQC', 'Fence', 'MiscFeature'], axis=1)

# Tratamos los datos faltantes
for column in df.columns:
    if df[column].dtype == 'object':
        df[column] = df[column].fillna(df[column].mode()[0])
    else:
        df[column] = df[column].fillna(df[column].mean())

# Codificamos las variables categóricas
df = pd.get_dummies(df, drop_first=True)
```

Después de eso, dividimos los datos en un conjunto de entrenamiento y un conjunto de prueba:

```python
# Definimos la variable objetivo y las variables predictoras
X = df.drop('SalePrice', axis=1)
y = df['SalePrice']

# Dividimos los datos en un conjunto de entrenamiento y un conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

Ahora estamos listos para entrenar nuestro modelo. En este caso, vamos a utilizar la regresión lineal:

```python
# Creamos el modelo
model = LinearRegression()

# Entrenamos el modelo
model.fit(X_train, y_train)
```

Finalmente, evaluamos el rendimiento del modelo en el conjunto de prueba:

```python
# Hacemos predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluamos el rendimiento del modelo
mse = mean_squared_error(y_test, y_pred)
print(f'MSE: {mse}')
print(f'RMSE: {mse**0.5}')
```