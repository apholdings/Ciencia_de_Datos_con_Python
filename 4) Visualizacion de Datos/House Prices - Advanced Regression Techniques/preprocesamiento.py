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
for column in df_train.select_dtypes(include=["object"]).columns:
    df_train[column] = df_train[column].fillna(df_train[column].mode()[0])

# Verificar si aún hay valores faltantes
print(df_train.isnull().sum())

# Mostrar las primeras filas del dataframe después de la limpieza
print(df_train.head())
