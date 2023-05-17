# 8) Pandas Avanzado
Pandas es una de las bibliotecas más populares y útiles en Python para la manipulación y el análisis de datos. Ya hemos cubierto algunas de las funcionalidades básicas de Pandas en las semanas anteriores, pero hay mucho más que aprender. 

En esta semana, vamos a profundizar en las capacidades de Pandas, aprendiendo técnicas más avanzadas y poderosas que te permitirán sacar aún más partido a tus datos.

1. **Manipulaciones de datos más complejas:** Ya hemos visto cómo utilizar funciones como groupby(), merge(), y concat(). Pero Pandas ofrece muchas otras herramientas para manipular datos, como apply() para aplicar funciones personalizadas a los datos, las tablas dinámicas para resumir los datos de manera similar a Excel, y el multi-index para tener múltiples niveles de índices en un DataFrame.

2. **Manipulación de datos de series temporales:** Muchos conjuntos de datos incluyen información temporal. Pandas ofrece una serie de funcionalidades para trabajar con datos de series temporales, como herramientas para el análisis de fechas (por ejemplo, extracción de mes, día de la semana, etc. de una fecha) y remuestreo (cambiando la frecuencia de los datos de tiempo).

3. **Rendimiento:** A medida que trabajas con conjuntos de datos más grandes, el rendimiento puede convertirse en un problema. Aprenderemos cómo mejorar el rendimiento de nuestros códigos de Pandas mediante el uso de operaciones vectorizadas (que son más rápidas que los bucles en Python) y reduciendo el uso de memoria.

4. **Actividad:** Para poner en práctica lo que hemos aprendido, trabajaremos con un conjunto de datos desafiante y aplicaremos nuestras nuevas habilidades de Pandas avanzado.

## Manipulaciones de datos más complejas
Las manipulaciones de datos más complejas son las operaciones que nos permiten transformar nuestros datos de maneras más sofisticadas y flexibles que las operaciones básicas. 

Estas son algunas de las manipulaciones de datos más complejas que podemos realizar con Pandas:

- **Función apply():** Esta es una de las funciones más versátiles en Pandas. Te permite aplicar una función personalizada a cada elemento de una Serie, o a cada fila o columna de un DataFrame. Por ejemplo, podrías tener una columna de fechas en un formato de cadena de texto y querrías convertirlas en objetos de fecha y hora de Python. Podrías definir una función personalizada para hacer esta conversión y luego usar apply() para aplicarla a toda la columna.
```python
# Primero, vamos a crear un dataframe de ejemplo:
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40],
    'C': [100, 200, 300, 400]
})

# Ahora, vamos a definir una función que multiplica un número por 10, y luego vamos a usar apply() para aplicar esta función a cada elemento de la columna 'A':

def multiply_by_ten(x):
    return x * 10

df['A'] = df['A'].apply(multiply_by_ten)
```

#### Cuando usar la funcion apply()
Por lo general, sabrás que necesitas usar apply() cuando necesites realizar una operación más compleja o personalizada en tus datos que no puede ser manejada por las funciones vectorizadas incorporadas en pandas.

En el ejemplo, apply() se usa para aplicar la función multiply_by_ten a cada elemento de la columna 'A'. Esto es útil cuando necesitas realizar una operación específica en una columna entera de tu DataFrame. En este caso, la función multiply_by_ten toma un solo argumento, un número, y devuelve el número multiplicado por diez. Cuando se usa apply(), esta función se aplica a cada elemento de la columna 'A'.

Además de aplicar funciones a lo largo de una columna, apply() también se puede usar para aplicar funciones a lo largo de una fila. Por ejemplo, podrías querer aplicar una función que toma como argumento toda una fila de datos y devuelve un valor basado en todos los valores de la fila. Para hacer esto, simplemente usarías apply(func, axis=1).

En resumen, la función apply() es una herramienta clave para la manipulación de datos en pandas y es especialmente útil cuando necesitas realizar operaciones personalizadas en tus datos.

- **Tablas dinámicas:** Si alguna vez has trabajado con Excel, probablemente estés familiarizado con las tablas dinámicas. Permiten resumir y agrupar los datos de formas útiles para el análisis. Por ejemplo, podrías tener un conjunto de datos de ventas y querrías resumir las ventas totales por mes y por producto. Podrías hacer esto fácilmente con una tabla dinámica.

```python
# Podemos usar el mismo dataframe para este ejemplo.
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40],
    'C': [100, 200, 300, 400]
})

# Supongamos que queremos crear una tabla dinámica que muestra la suma de las columnas 'A' y 'B' para cada valor único en la columna 'C'. Podríamos hacerlo así:

pivot = df.pivot_table(values=['A', 'B'], index='C', aggfunc='sum')

```
Las tablas dinámicas son una herramienta muy útil para resumir, agrupar y analizar datos. Proporcionan una manera flexible y fácil de manipular y reorganizar los datos, lo que puede ser muy útil para explorar tendencias y patrones.

En el ejemplo la tabla dinámica calcula la suma de las columnas 'A' y 'B' para cada valor único en la columna 'C'. Esto puede ser útil, por ejemplo, si 'A' y 'B' representan diferentes tipos de ventas (por ejemplo, ventas en línea y ventas en tienda), y 'C' representa diferentes regiones o tiendas. La tabla dinámica te permitiría ver rápidamente las ventas totales por región o tienda.

Las tablas dinámicas son especialmente útiles cuando se trabaja con datos que tienen múltiples dimensiones categóricas. Por ejemplo, podrías tener datos de ventas que incluyan información sobre el producto, la región, el canal de ventas y la fecha. Una tabla dinámica te permitiría fácilmente explorar las ventas por producto por región, las ventas por canal a lo largo del tiempo, o cualquier otra combinación de dimensiones que pudieras estar interesado en explorar.

#### Cuando deberiamos usar una tabla dinamica
Por lo general, sabrías que una tabla dinámica podría ser útil si te encuentras queriendo explorar las relaciones entre diferentes dimensiones categóricas de tus datos, o si estás interesado en resumir tus datos a lo largo de una o más dimensiones categóricas.

Finalmente, es importante señalar que las tablas dinámicas son una herramienta de análisis exploratorio de datos. No cambiarán tus datos subyacentes, sino que te proporcionarán una vista resumida de ellos que puede ser útil para la exploración y el análisis.

- **Multi-index:** En algunos casos, puede ser útil tener múltiples niveles de índices en un DataFrame. Por ejemplo, podrías tener datos de ventas para diferentes productos en diferentes tiendas, y querrías indexar los datos tanto por producto como por tienda. Los multi-índices de Pandas te permiten hacer esto.

```python
df = pd.DataFrame({
    'Store': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Product': ['X', 'Y', 'Z', 'X', 'Y', 'Z'],
    'Sales': [100, 200, 300, 150, 250, 350]
})

# Ahora, vamos a establecer un multi-index en las columnas 'Store' y 'Product':

df.set_index(['Store', 'Product'], inplace=True)
```

#### Cuando deberiamos usar un índice múltiple
Un índice múltiple (o índice jerárquico) puede ser muy útil cuando se trabaja con datos que tienen múltiples dimensiones. En este caso, hemos indexado los datos tanto por la tienda ('Store') como por el producto ('Product'). Esto significa que los datos están ordenados primero por tienda y luego por producto dentro de cada tienda.

Un índice múltiple puede facilitar el análisis de subconjuntos de los datos. Por ejemplo, si quisieras ver todas las ventas para la tienda 'A', podrías hacerlo así:
```python
df.loc['A']
```
Esto te daría un DataFrame con todas las filas para la tienda 'A', y los datos seguirían estando indexados por producto.

De manera similar, si quisieras ver las ventas del producto 'X' en la tienda 'A', podrías hacerlo así:
```python
df.loc[('A', 'X')]
```
Esto te daría una Serie con la información de ventas para el producto 'X' en la tienda 'A'.

El uso de un índice múltiple puede facilitar la organización y el análisis de los datos, especialmente cuando se trabaja con datos de alta dimensionalidad. Sin embargo, también puede hacer que algunas operaciones sean más complicadas, ya que tienes que tener en cuenta los múltiples niveles del índice. En general, es una herramienta útil para tener en tu caja de herramientas de análisis de datos.

### Ejemplo: Manipulaciones de Datos mas Complejas

Sigamos con el ejemplo de ventas de tiendas. Para esto, vamos a suponer que tenemos un DataFrame con las ventas de distintos productos en varias tiendas. El objetivo de este análisis es obtener una visión más clara de las ventas por tienda y por producto.

```python
import pandas as pd

# Creamos el DataFrame
df = pd.DataFrame({
    'Store': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B'],
    'Product': ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z'],
    'Month': ['Jan', 'Jan', 'Jan', 'Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb', 'Feb', 'Feb', 'Feb'],
    'Sales': [100, 200, 300, 150, 250, 350, 120, 210, 310, 160, 260, 370]
})

# Establecemos un multi-index en las columnas 'Store', 'Product' y 'Month'
df.set_index(['Store', 'Product', 'Month'], inplace=True)
print(df)

# Creamos una tabla dinámica para resumir las ventas totales por tienda y por producto
pivot = df.pivot_table(values='Sales', index=['Store', 'Product'], aggfunc='sum')
print("\nPivot Table:\n", pivot)

# Aplicamos la función apply para calcular el porcentaje de ventas de cada producto por tienda
pivot['Sales_Percentage'] = pivot.groupby(level=0).apply(lambda x:  100*x / x.sum())
print("\nPivot Table with Sales Percentage:\n", pivot)
```

**En este ejemplo:**

1. Primero, creamos un DataFrame que contiene información de ventas de varios productos en diferentes tiendas y meses.

2. Luego, usamos set_index para establecer un multi-index en las columnas 'Store', 'Product' y 'Month'. Esto nos permite indexar los datos por tienda, producto y mes.

3. Creamos una tabla dinámica con pivot_table para resumir las ventas totales por tienda y por producto.

4. Finalmente, usamos la función apply para calcular el porcentaje de ventas de cada producto por tienda.

A través de este análisis, podemos obtener una visión detallada de las ventas por tienda y por producto. Esto podría ser útil para tomar decisiones sobre estrategias de ventas, inventario y más.