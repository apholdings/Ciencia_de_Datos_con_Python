# House Prices: Advanced Regression Techniques

## Actividad - Realizar EDA en un conjunto de datos del mundo real y presentar los resultados.

Comencemos con el preprocesamiento de los datos. Recuerda, este conjunto de datos es más grande y más complejo, por lo que podría haber más pasos de preprocesamiento necesarios.

```python
# Preprocesamiento de datos
import pandas as pd

# Cargar los datos
df_train = pd.read_csv("train.csv")

# Llenar los valores faltantes en las columnas numéricas con la mediana de las columnas correspondientes
df_train = df_train.fillna(df_train.median(numeric_only=True))

# Para las columnas categóricas, llenamos los valores faltantes con la moda (el valor más común)
for column in df_train.select_dtypes(include=["object"]).columns:
    df_train[column] = df_train[column].fillna(df_train[column].mode()[0])
```

Una vez que hemos preprocesado los datos, podemos comenzar con el análisis exploratorio. Aquí están algunos pasos que podríamos seguir:

#### Estadísticas Descriptivas
```python
# Estadísticas descriptivas
print(df_train.describe())
```

#### Distribuciones de las Variables
Podríamos visualizar las distribuciones de algunas variables, como 'SalePrice', 'OverallQual' y 'YearBuilt'.
```python
# Histograma de precios de venta
plt.hist(df_train['SalePrice'], bins=10, edgecolor='black')
plt.title('Distribución de los Precios de Venta')
plt.xlabel('Precio de Venta')
plt.ylabel('Frecuencia')
plt.show()

# Histograma de calidad general
plt.hist(df_train['OverallQual'], bins=10, edgecolor='black')
plt.title('Distribución de la Calidad General')
plt.xlabel('Calidad General')
plt.ylabel('Frecuencia')
plt.show()

# Histograma de año de construcción
plt.hist(df_train['YearBuilt'], bins=10, edgecolor='black')
plt.title('Distribución del Año de Construcción')
plt.xlabel('Año de Construcción')
plt.ylabel('Frecuencia')
plt.show()
```

#### Relaciones entre Variables
Podríamos explorar las relaciones entre algunas variables, como 'SalePrice' y 'OverallQual', y 'SalePrice' y 'YearBuilt'.
```python
# Boxplot del precio de venta por calidad general
df_train.boxplot(column='SalePrice', by='OverallQual')
plt.title('Precio de Venta por Calidad General')
plt.suptitle('') # Eliminar el título automático
plt.xlabel('Calidad General')
plt.ylabel('Precio de Venta')
plt.show()

# Scatter plot del precio de venta por año de construcción
plt.scatter(df_train['YearBuilt'], df_train['SalePrice'])
plt.title('Precio de Venta por Año de Construcción')
plt.xlabel('Año de Construcción')
plt.ylabel('Precio de Venta')
plt.show()
```