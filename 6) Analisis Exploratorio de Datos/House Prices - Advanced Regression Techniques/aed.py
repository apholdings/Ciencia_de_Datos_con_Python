import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df_train = pd.read_csv("train.csv")

# Llenar los valores faltantes en las columnas numéricas con la mediana de las columnas correspondientes
df_train = df_train.fillna(df_train.median(numeric_only=True))

# Para las columnas categóricas, llenamos los valores faltantes con la moda (el valor más común)
for column in df_train.select_dtypes(include=["object"]).columns:
    df_train[column] = df_train[column].fillna(df_train[column].mode()[0])


# Estadísticas descriptivas
print(df_train.describe())

# Histograma de precios de venta
plt.hist(df_train["SalePrice"], bins=10, edgecolor="black")
plt.title("Distribución de los Precios de Venta")
plt.xlabel("Precio de Venta")
plt.ylabel("Frecuencia")
plt.show()

# Histograma de calidad general
plt.hist(df_train["OverallQual"], bins=10, edgecolor="black")
plt.title("Distribución de la Calidad General")
plt.xlabel("Calidad General")
plt.ylabel("Frecuencia")
plt.show()

# Histograma de año de construcción
plt.hist(df_train["YearBuilt"], bins=10, edgecolor="black")
plt.title("Distribución del Año de Construcción")
plt.xlabel("Año de Construcción")
plt.ylabel("Frecuencia")
plt.show()
