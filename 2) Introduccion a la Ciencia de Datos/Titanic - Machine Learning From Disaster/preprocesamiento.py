"""
Para comenzar, es necesario importar las bibliotecas necesarias y cargar los datos. 
Vamos a utilizar Pandas para manipular los datos y Matplotlib para la visualización de datos.

Aquí está el código inicial para hacer esto:
"""

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df_train = pd.read_csv("train.csv")

# Mostrar las primeras filas del dataframe
print(df_train.head())

"""
Este script cargará los datos de entrenamiento del archivo 'train.csv' y mostrará las 
primeras filas del dataframe. Esto nos dará una idea inicial de cómo se ven nuestros datos.

Luego, podemos comenzar a explorar y limpiar los datos. Por ejemplo, podríamos querer ver si
hay valores faltantes en nuestros datos y tratar con ellos de alguna manera. 

Aquí está el código para hacer esto:
"""
# Verificar si hay valores faltantes
print(df_train.isnull().sum())

# Llenar los valores faltantes en la columna 'Age' con la mediana de las edades
df_train["Age"].fillna(df_train["Age"].median(), inplace=True)

# Eliminar la columna 'Cabin' debido a la gran cantidad de valores faltantes
df_train = df_train.drop(["Cabin"], axis=1)

# Mostrar las primeras filas del dataframe después de la limpieza
print(df_train.head())

"""
Este script verificará si hay valores faltantes en cada columna del dataframe, 
llenará los valores faltantes en la columna 'Age' con la mediana de las edades, y eliminará 
la columna 'Cabin' debido a la gran cantidad de valores faltantes. 
Luego, mostrará las primeras filas del dataframe después de la limpieza.

"""
