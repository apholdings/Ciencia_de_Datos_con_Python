# House Prices: Advanced Regression Techniques

## Actividad - Analizar datos utilizando estadísticas descriptivas e inferenciales.
Este conjunto de datos, ["House Prices: Advanced Regression Techniques"](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data), es más avanzado en comparación con el conjunto de datos del Titanic. Incluye una serie de características diferentes que describen aspectos de las casas residenciales, y el objetivo es predecir el precio final de cada casa.

Empezamos preparando nuestros datos:
```python
import pandas as pd
import numpy as np

# Cargar los datos
df_train = pd.read_csv("train.csv")

# Llenar los valores faltantes en las columnas numéricas con la mediana de las columnas correspondientes
df_train = df_train.fillna(df_train.median(numeric_only=True))

# Para las columnas categóricas, llenamos los valores faltantes con la moda (el valor más común)
for column in df_train.select_dtypes(include=["object"]).columns:
    df_train[column] = df_train[column].fillna(df_train[column].mode()[0])
```

Ahora, calculemos algunas estadísticas descriptivas para algunas de las columnas numéricas. Por ejemplo, podemos examinar las columnas "SalePrice", "LotArea", "YearBuilt" y "OverallQual". Estas estadísticas incluirán la media, mediana, moda, rango, varianza, desviación estándar y cuartiles.

``` python
# Media
mean_price = df_train['SalePrice'].mean()
print(f"Media del precio de venta: {mean_price}")

# Mediana
median_price = df_train['SalePrice'].median()
print(f"Mediana del precio de venta: {median_price}")

# Moda
mode_price = df_train['SalePrice'].mode()[0]
print(f"Moda del precio de venta: {mode_price}")

# Rango
range_price = df_train['SalePrice'].max() - df_train['SalePrice'].min()
print(f"Rango del precio de venta: {range_price}")

# Varianza
variance_price = df_train['SalePrice'].var()
print(f"Varianza del precio de venta: {variance_price}")

# Desviación estándar
std_price = df_train['SalePrice'].std()
print(f"Desviación estándar del precio de venta: {std_price}")

# Cuartiles
quartiles_price = df_train['SalePrice'].quantile([0.25, 0.5, 0.75])
print(f"Cuartiles del precio de venta:\n{quartiles_price}")

# Repetir los mismos pasos para las columnas "LotArea", "YearBuilt" y "OverallQual"
```

Luego de calcular estas estadísticas, podrás obtener una visión detallada de la distribución de los precios de venta, el tamaño del lote, el año de construcción y la calidad general de las viviendas. 

Estas estadísticas te permitirán entender mejor tus datos y te ayudarán a tomar decisiones informadas a la hora de seleccionar y aplicar algoritmos de aprendizaje automático.