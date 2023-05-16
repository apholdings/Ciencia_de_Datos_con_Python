# House Prices: Advanced Regression Techniques

## Actividad - Limpieza y Transformación de Datos
Este conjunto de datos, ["House Prices: Advanced Regression Techniques"](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data), es más avanzado en comparación con el conjunto de datos del Titanic. Incluye una serie de características diferentes que describen aspectos de las casas residenciales, y el objetivo es predecir el precio final de cada casa.

```python
import pandas as pd
import numpy as np

# Cargar los datos
df_train = pd.read_csv("train.csv")

# Mostrar las primeras filas del dataframe
print(df_train.head())

# Verificar si hay valores faltantes
print(df_train.isnull().sum())

# Llenar los valores faltantes en las columnas numéricas con la mediana de las columnas correspondientes
df_train = df_train.fillna(df_train.median(numeric_only=True))

# Para las columnas categóricas, llenamos los valores faltantes con la moda (el valor más común)
for column in df_train.select_dtypes(include=['object']).columns:
    df_train[column] = df_train[column].fillna(df_train[column].mode()[0])

# Verificar si aún hay valores faltantes
print(df_train.isnull().sum())

# Mostrar las primeras filas del dataframe después de la limpieza
print(df_train.head())
```

Este código se encarga de cargar los datos, mostrar las primeras filas, y verificar si hay valores faltantes. Luego, llena los valores faltantes en las columnas numéricas con la mediana de las columnas correspondientes y, en el caso de las columnas categóricas, con la moda (el valor más común). Finalmente, verifica nuevamente si hay valores faltantes y muestra las primeras filas del dataframe limpio.


### Visualizacion de Datos
Podemos visualizar varias características del conjunto de datos para tener una mejor idea de la distribución de los datos y las posibles relaciones entre las características y el objetivo (el precio de la vivienda).

Aquí hay algunos ejemplos de cómo podríamos hacerlo usando Matplotlib y Seaborn:
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df_train = pd.read_csv("train.csv")

# Llenar los valores faltantes en las columnas numéricas con la mediana de las columnas correspondientes
df_train = df_train.fillna(df_train.median(numeric_only=True))

# Para las columnas categóricas, llenamos los valores faltantes con la moda (el valor más común)
for column in df_train.select_dtypes(include=['object']).columns:
    df_train[column] = df_train[column].fillna(df_train[column].mode()[0])

# Histograma de los precios de las casas
plt.figure(figsize=(10, 6))
plt.title("Distribución de los precios de las casas")
sns.histplot(df_train["SalePrice"], kde=False, bins=30)
plt.show()

# Gráfico de barras de la calidad general de las casas
plt.figure(figsize=(10, 6))
plt.title("Calidad general de las casas")
sns.countplot(x="OverallQual", data=df_train)
plt.show()

# Gráfico de dispersión de la superficie de la casa vs precio de venta
plt.figure(figsize=(10, 6))
plt.title("Superficie de la casa vs Precio de venta")
sns.scatterplot(x="GrLivArea", y="SalePrice", data=df_train)
plt.show()

# Gráfico de dispersión de la superficie del lote vs precio de venta
plt.figure(figsize=(10, 6))
plt.title("Superficie del lote vs Precio de venta")
sns.scatterplot(x="LotArea", y="SalePrice", data=df_train)
plt.show()

# Gráfico de dispersión de la superficie del sótano vs precio de venta
plt.figure(figsize=(10, 6))
plt.title("Superficie del sótano vs Precio de venta")
sns.scatterplot(x="TotalBsmtSF", y="SalePrice", data=df_train)
plt.show()
```

Estos gráficos nos proporcionan información útil sobre los datos, como la distribución de los precios de las viviendas, la calidad general de las casas, y cómo varias características de las casas (como la superficie de la casa, el tamaño del lote y la superficie del sótano) se relacionan con el precio de la vivienda.