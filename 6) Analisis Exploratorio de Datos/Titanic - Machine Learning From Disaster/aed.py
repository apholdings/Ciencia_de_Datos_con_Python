import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df_train = pd.read_csv("train.csv")

# Ver las primeras filas del DataFrame
print(df_train.head())

# Llenar los valores faltantes en la columna 'Age' con la mediana de las edades
df_train["Age"].fillna(df_train["Age"].median(), inplace=True)

# Eliminar la columna 'Cabin' debido a la gran cantidad de valores faltantes
df_train = df_train.drop(["Cabin"], axis=1)

# Estadísticas descriptivas
print(df_train.describe())

# Histograma de edades
plt.hist(df_train["Age"], bins=10, edgecolor="black")
plt.title("Distribución de las Edades")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()

# Histograma de tarifas
plt.hist(df_train["Fare"], bins=10, edgecolor="black")
plt.title("Distribución de las Tarifas")
plt.xlabel("Tarifa")
plt.ylabel("Frecuencia")
plt.show()

# Histograma de supervivencia
plt.hist(df_train["Survived"], bins=3, edgecolor="black")
plt.title("Distribución de la Supervivencia")
plt.xlabel("Supervivencia")
plt.ylabel("Frecuencia")
plt.show()
