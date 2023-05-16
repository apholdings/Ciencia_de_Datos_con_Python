# Titanic - Machine Learning From Disaster

## Actividad - Analizar datos utilizando estadísticas descriptivas e inferenciales.

Para esta actividad podemos utilizar la biblioteca pandas para cargar y analizar los datos. También utilizaremos numpy y scipy para realizar algunos cálculos estadísticos.

Primero, necesitamos cargar los datos. Asegúrate de tener el archivo 'train.csv' en el mismo directorio que tu script de Python o Jupyter notebook. De lo contrario, tendrás que proporcionar la ruta completa al archivo.

```python
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
```

**Media de la edad:** Es el promedio de todas las edades en el conjunto de datos. Suma todas las edades y las divide por el número de edades. En tu caso, la media de la edad es alrededor de 29.36 años. Esto indica que la edad promedio de los pasajeros en el Titanic era de aproximadamente 29 años.

```python
mean_age = df['Age'].mean()
print(f"Media de la edad: {mean_age}")
```

**Mediana de la edad:** La mediana es el valor que separa la mitad superior de las edades de la mitad inferior. En tu caso, la mediana de la edad es 28.0 años. Esto significa que la mitad de los pasajeros tenía menos de 28 años y la otra mitad tenía más de 28 años.
```python
median_age = df['Age'].median()
print(f"Mediana de la edad: {median_age}")
```

**Moda de la edad:** La moda es el valor que aparece con mayor frecuencia en un conjunto de datos. En tu caso, la moda de la edad es 28.0 años. Esto indica que había más pasajeros de 28 años que de cualquier otra edad en el Titanic.
```python
mode_age = df['Age'].mode()[0]
print(f"Moda de la edad: {mode_age}")
```

**Rango de la edad:** El rango es la diferencia entre el valor máximo y mínimo en un conjunto de datos. En tu caso, el rango de la edad es 79.58 años. Esto significa que la diferencia de edad entre el pasajero más joven y el más viejo en el Titanic era de casi 80 años.
```python
range_age = df['Age'].max() - df['Age'].min()
print(f"Rango de la edad: {range_age}")
```

**Varianza de la edad:** La varianza mide cuánto varían las edades respecto de la media de la edad. Una varianza más alta indica una mayor dispersión de las edades. En tu caso, la varianza de la edad es alrededor de 169.51. Esto indica que las edades de los pasajeros del Titanic varían bastante alrededor de la media.
```python
variance_age = df['Age'].var()
print(f"Varianza de la edad: {variance_age}")
```

**Desviación estándar de la edad:** La desviación estándar es la raíz cuadrada de la varianza. También mide la dispersión de los datos, pero a diferencia de la varianza, la desviación estándar está en las mismas unidades que los datos, lo que la hace más fácil de interpretar. En tu caso, la desviación estándar de la edad es alrededor de 13.02 años. Esto indica que la mayoría de las edades de los pasajeros del Titanic se encontraban dentro de un rango de aproximadamente 13 años por encima o por debajo de la media.
```python
std_age = df['Age'].std()
print(f"Desviación estándar de la edad: {std_age}")
```

**Cuartiles de la edad:** Los cuartiles dividen un conjunto de datos en cuatro partes iguales. El primer cuartil (Q1) es el valor por debajo del cual se encuentra el 25% de las edades. El segundo cuartil (Q2) es la mediana. El tercer cuartil (Q3) es el valor por debajo del cual se encuentra el 75% de las edades. En tu caso, Q1 es 22.0 años, Q2 es 28.0 años, y Q3 es 35.0 años. Esto indica que el 25% de los pasajeros tenía menos de 22 años, el 50% tenía menos de 28 años, y el 75% tenía menos de 35 años.
```python
quartiles_age = df['Age'].quantile([0.25, 0.5, 0.75])
print(f"Cuartiles de la edad:\n{quartiles_age}")
```