import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df_train = pd.read_csv("train.csv")

# Llenar los valores faltantes en las columnas numéricas con la mediana de las columnas correspondientes
df_train = df_train.fillna(df_train.median(numeric_only=True))

# Para las columnas categóricas, llenamos los valores faltantes con la moda (el valor más común)
for column in df_train.select_dtypes(include=["object"]).columns:
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

# Gráfico de línea del año de construcción y el precio de venta
plt.figure(figsize=(12, 6))
df_train.groupby("YearBuilt")["SalePrice"].median().plot()
plt.title("Relación entre el año de construcción y el precio de venta")
plt.show()

# Gráfico de barras del precio de venta por zona
plt.figure(figsize=(12, 6))
sns.barplot(x="MSZoning", y="SalePrice", data=df_train)
plt.title("Distribución de los precios de venta por zona")
plt.show()

# Gráfico de dispersión del tamaño del primer piso y el precio de venta
plt.figure(figsize=(12, 6))
sns.scatterplot(x="1stFlrSF", y="SalePrice", data=df_train)
plt.title("Relación entre el tamaño del primer piso y el precio de venta")
plt.show()
