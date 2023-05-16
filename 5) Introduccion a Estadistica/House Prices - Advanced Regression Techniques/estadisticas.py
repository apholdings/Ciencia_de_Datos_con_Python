import pandas as pd
import numpy as np

# Cargar los datos
df_train = pd.read_csv("train.csv")

# Llenar los valores faltantes en las columnas numéricas con la mediana de las columnas correspondientes
df_train = df_train.fillna(df_train.median(numeric_only=True))

# Para las columnas categóricas, llenamos los valores faltantes con la moda (el valor más común)
for column in df_train.select_dtypes(include=["object"]).columns:
    df_train[column] = df_train[column].fillna(df_train[column].mode()[0])

# Media
mean_price = df_train["SalePrice"].mean()
print(f"Media del precio de venta: {mean_price}")

# Mediana
median_price = df_train["SalePrice"].median()
print(f"Mediana del precio de venta: {median_price}")

# Moda
mode_price = df_train["SalePrice"].mode()[0]
print(f"Moda del precio de venta: {mode_price}")

# Rango
range_price = df_train["SalePrice"].max() - df_train["SalePrice"].min()
print(f"Rango del precio de venta: {range_price}")

# Varianza
variance_price = df_train["SalePrice"].var()
print(f"Varianza del precio de venta: {variance_price}")

# Desviación estándar
std_price = df_train["SalePrice"].std()
print(f"Desviación estándar del precio de venta: {std_price}")

# Cuartiles
quartiles_price = df_train["SalePrice"].quantile([0.25, 0.5, 0.75])
print(f"Cuartiles del precio de venta:\n{quartiles_price}")

# Repetir los mismos pasos para las columnas "LotArea", "YearBuilt" y "OverallQual"
