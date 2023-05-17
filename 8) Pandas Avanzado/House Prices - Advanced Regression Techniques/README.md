# House Prices: Advanced Regression Techniques

## Actividad - Practicar habilidades avanzadas de pandas en un conjunto de datos desafiante.

#### Manipulaciones de datos más complejas: apply(), tablas dinámicas, multi-index.

Primero, leamos el conjunto de datos y veamos sus primeras filas:

```python
import pandas as pd

# Cargar los datos
df_train = pd.read_csv("train.csv")

# Ver las primeras filas del DataFrame
print(df_train.head())
```

- **Función apply():** Podemos usar la función apply() para crear una nueva columna que clasifique las casas por su tamaño total ('TotalSF') que es la suma de '1stFlrSF', '2ndFlrSF' y 'TotalBsmtSF'.
```python
def size_category(size):
    if size < 1000:
        return 'Small'
    elif size < 2000:
        return 'Medium'
    else:
        return 'Large'

df['TotalSF'] = df['1stFlrSF'] + df['2ndFlrSF'] + df['TotalBsmtSF']
df['SizeCategory'] = df['TotalSF'].apply(size_category)
print(df[['TotalSF', 'SizeCategory']].head())
```

- **Tablas dinámicas:** Podemos usar una tabla dinámica para resumir el precio promedio de venta por categoría de tamaño y calidad general.
```python
pivot = df.pivot_table(values='SalePrice', index='SizeCategory', columns='OverallQual', aggfunc='mean')
print(pivot)
```

- **Multi-index:** Podemos establecer un multi-index en las columnas 'SizeCategory' y 'OverallQual' para analizar los precios de venta de diferentes grupos.
```python
df.set_index(['SizeCategory', 'OverallQual'], inplace=True)
print(df.head())
```

#### Rendimiento: Uso de operaciones vectorizadas, reducción del uso de memoria.

- **Uso de operaciones vectorizadas:** En lugar de usar un bucle for para iterar sobre las filas del DataFrame y calcular el precio promedio de venta para cada categoría de tamaño, podemos usar operaciones vectorizadas para hacerlo de manera más eficiente.
```python
avg_price = df.groupby('SizeCategory')['SalePrice'].mean()
print(avg_price)
```

- **Reducción del uso de memoria:** Podemos cambiar el tipo de datos de algunas columnas para reducir el uso de memoria.
```python
print(df.memory_usage(deep=True))

df['MSSubClass'] = df['MSSubClass'].astype('int8')
df['OverallQual'] = df['OverallQual'].astype('int8')

print(df.memory_usage(deep=True))
```