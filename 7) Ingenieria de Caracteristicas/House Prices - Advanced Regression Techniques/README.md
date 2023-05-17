# House Prices: Advanced Regression Techniques

## Actividad - Aplicar técnicas de ingeniería de características a un conjunto de datos y discutir el impacto en un modelo simple.

Apliquemos las técnicas de ingeniería de características al conjunto de datos de House Prices.

Primero hagamos pre-procesamiento de datos.

```python
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# Cargar los datos
df_train = pd.read_csv("train.csv")

# Ver las primeras filas del DataFrame
print(df_train.head())

# Llenar los valores faltantes en las columnas numéricas con la mediana de las columnas correspondientes
df_train = df_train.fillna(df_train.median(numeric_only=True))

# Para las columnas categóricas, llenamos los valores faltantes con la moda (el valor más común)
for column in df_train.select_dtypes(include=["object"]).columns:
    df_train[column] = df_train[column].fillna(df_train[column].mode()[0])
```

Ahora, vamos a crear algunas características nuevas y hacer algunas codificaciones.

```python
# Crear una nueva característica 'TotalSF' que es la suma de 'TotalBsmtSF', '1stFlrSF' y '2ndFlrSF'
df_train['TotalSF'] = df_train['TotalBsmtSF'] + df_train['1stFlrSF'] + df_train['2ndFlrSF']

# Codificación One-Hot para la característica 'MSZoning'
df_train = pd.get_dummies(df_train, columns=['MSZoning'])

# Codificación Ordinal para la característica 'LotShape'
# Aquí asumimos que la forma del lote tiene un orden de preferencia 
ordinal_encoder = OrdinalEncoder(categories=[['Reg', 'IR1', 'IR2', 'IR3']])
df_train['LotShape'] = ordinal_encoder.fit_transform(df_train[['LotShape']])

print(df_train.head())
```

1. Aquí, hemos creado una nueva característica 'TotalSF' que es la suma de las áreas de sótano, primer piso y segundo piso. Esto podría ser útil porque en lugar de considerar estas tres áreas por separado, un comprador de vivienda podría estar más interesado en el área total.

2. Además, hemos aplicado la codificación one-hot a la característica 'MSZoning'. Esto es útil porque 'MSZoning' es una variable categórica sin un orden inherente, por lo que la codificación one-hot es una buena opción aquí.

3. Finalmente, hemos aplicado la codificación ordinal a la característica 'LotShape'. Esto asume que las diferentes formas de lote tienen un orden específico, desde regular (Reg) hasta ligeramente irregular (IR1), moderadamente irregular (IR2) y muy irregular (IR3). Si este orden tiene sentido podría depender del contexto específico, pero podría ser una suposición razonable.

4. Este es solo un ejemplo de lo que podríamos hacer con la ingeniería de características en este conjunto de datos. Hay muchas otras características que podríamos crear y muchas otras formas en que podríamos codificar las características categóricas. ¡La ingeniería de características es un área muy creativa de la ciencia de datos y hay mucho espacio para experimentar!