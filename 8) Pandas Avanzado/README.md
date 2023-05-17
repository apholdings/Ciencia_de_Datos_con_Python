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


## Manipulación de datos de series temporales
Trabajar con series temporales es una tarea común en muchas aplicaciones de análisis de datos. Pandas proporciona una serie de herramientas para trabajar con fechas, horas y series temporales.

Aquí están algunos de los conceptos clave en la manipulación de series temporales con Pandas:
Conversión de cadenas a fechas: Si tus datos están en formato de cadena, puedes usar la función pd.to_datetime() para convertirlos en un objeto de fecha y hora de Python.

- **Conversión de cadenas a fechas:** Si tienes un conjunto de datos con cadenas de texto que representan el tiempo, podemos hacer uso de la funcion to_datetime() para convertir las cadenas de texto a fechas.
```python
import pandas as pd

# Crear un DataFrame de ejemplo
df = pd.DataFrame({
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
    'value': [1, 2, 3, 4]
})

# Convertir la columna de fecha a datetime
df['date'] = pd.to_datetime(df['date'])

print(df)
print(df.dtypes)
```

- **Resampling:** Si tienes una serie temporal y quieres cambiar la frecuencia de los datos, puedes usar la función resample(). Por ejemplo, si tienes datos diarios y quieres resumirlos en datos mensuales, puedes hacerlo con resample().
```python
# Crear un DataFrame con fechas diarias
rng = pd.date_range('2023-01-01', periods=100, freq='D')
df = pd.DataFrame({'value': range(100)}, index=rng)

# Resample a datos mensuales, sumando los valores de cada mes
df_monthly = df.resample('M').sum()

print(df_monthly)
```
#### Veamos cómo se podría usar el Resampling / Remuestreo en un escenario del mundo real.

Imagina que trabajas para una empresa de ventas al por menor y tienes datos de ventas diarias para diferentes productos en diferentes tiendas. Tienes una serie de tiempo con las ventas diarias para un producto en particular en una tienda en particular.

Sin embargo, estás interesado en analizar las tendencias a nivel de mes en lugar de día a día, ya que las fluctuaciones diarias pueden ser muy volátiles y pueden dificultar la identificación de las tendencias subyacentes. Por tanto, quieres resumir tus datos diarios en datos mensuales.

Podrías hacerlo con el remuestreo de la siguiente manera:
```python
import pandas as pd

# Supongamos que este es tu DataFrame de ventas diarias
df_daily_sales = pd.DataFrame({
    'date': pd.date_range(start='2023-01-01', end='2023-12-31'),
    'sales': pd.np.random.randint(1, 100, size=365)
})

# Convertir la columna de fecha a datetime y establecerla como índice
df_daily_sales['date'] = pd.to_datetime(df_daily_sales['date'])
df_daily_sales.set_index('date', inplace=True)

# Remuestrear a ventas mensuales
df_monthly_sales = df_daily_sales.resample('M').sum()

print(df_monthly_sales)
```
Ahora, en lugar de tener 365 puntos de datos para el año, tienes 12 puntos de datos que representan las ventas totales para cada mes. Esto podría facilitarte la identificación de las tendencias a lo largo del año, como cuáles son los meses más fuertes para las ventas.

- **Desplazamiento de datos:** Si necesitas desplazar tus datos en el tiempo, puedes usar la función shift(). Esto puede ser útil para calcular cambios en el tiempo (por ejemplo, la diferencia de ventas entre este mes y el mes pasado).
```python
# Desplazar los datos un lugar hacia abajo
df_shifted = df.shift(1)

print(df_shifted.head())
```

#### Desplazamiento de datos en un escenario del mundo real.
Supongamos que eres un analista financiero y estás trabajando con datos de ingresos mensuales de una empresa. Quieres calcular el cambio porcentual en los ingresos mes a mes, lo que te permitirá identificar tendencias de crecimiento o disminución en los ingresos.

Podrías hacer esto utilizando la función shift() para desplazar los datos y luego calcular la diferencia porcentual:

```python
import pandas as pd

# Supongamos que este es tu DataFrame de ingresos mensuales
df_monthly_revenue = pd.DataFrame({
    'date': pd.date_range(start='2023-01-01', end='2023-12-31', freq='M'),
    'revenue': pd.np.random.randint(10000, 50000, size=12)
})

# Convertir la columna de fecha a datetime y establecerla como índice
df_monthly_revenue['date'] = pd.to_datetime(df_monthly_revenue['date'])
df_monthly_revenue.set_index('date', inplace=True)

# Desplazar los ingresos un lugar hacia abajo
df_shifted = df_monthly_revenue.shift(1)

# Calcular el cambio porcentual en los ingresos
df_monthly_revenue['percentage_change'] = (df_monthly_revenue['revenue'] - df_shifted['revenue']) / df_shifted['revenue'] * 100

print(df_monthly_revenue)
```
Ahora, tendrás una nueva columna en tu DataFrame que muestra el cambio porcentual en los ingresos mes a mes. Con esta información, podrás analizar tendencias y patrones en los ingresos de la empresa a lo largo del tiempo y proporcionar información valiosa para la toma de decisiones.

- **Ventanas móviles:** Si necesitas calcular estadísticas móviles (como un promedio móvil), puedes usar la función rolling().
```python
# Calcular un promedio móvil de 7 días
df_rolling = df.rolling(window=7).mean()

print(df_rolling.head(10))
```

Las ventanas móviles son especialmente útiles cuando trabajas con series de tiempo y quieres suavizar las fluctuaciones a corto plazo y destacar tendencias a largo plazo. Un promedio móvil es un ejemplo común de esto.

#### Ventanas móviles en un escenario del mundo real.
Supongamos que estás analizando las acciones de una compañía y tienes datos diarios del precio de cierre de la acción durante el último año. Quieres calcular un promedio móvil de 30 días del precio de cierre para ayudarte a ver la tendencia general en el precio de la acción sin las fluctuaciones diarias.
```python
import pandas as pd
import numpy as np

# Crear un DataFrame con 365 días de precios de cierre (valores aleatorios para este ejemplo)
df = pd.DataFrame({
    'date': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
    'close': np.random.rand(365) * 100
})

# Convertir la columna de fecha a datetime y establecerla como índice
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Calcular un promedio móvil de 30 días del precio de cierre
df['30_day_rolling_avg'] = df['close'].rolling(window=30).mean()

print(df.head(35))
```
En este DataFrame, la nueva columna '30_day_rolling_avg' es el promedio móvil de 30 días del precio de cierre de la acción. Esta es una forma común de suavizar los datos de series de tiempo para ver tendencias a largo plazo.

- **Diferenciación:** Si necesitas calcular la diferencia entre el valor actual y el valor anterior en una serie temporal, puedes usar la función diff().
```python
# Calcular la diferencia día a día
df_diff = df.diff()

print(df_diff.head())
```
La diferenciación es una técnica común en el análisis de series de tiempo, especialmente cuando se quiere transformar una serie no estacionaria en una serie estacionaria para ciertos modelos estadísticos.

#### Diferenciación en un escenario del mundo real.
Por ejemplo, supongamos que eres analista financiero y estás estudiando el precio de las acciones de una compañía. Estás interesado en el cambio diario en el precio de las acciones, no en el precio absoluto. Aquí es donde la función diff() puede ser útil.
```python
import pandas as pd
import numpy as np

# Crear un DataFrame con 365 días de precios de cierre (valores aleatorios para este ejemplo)
df = pd.DataFrame({
    'date': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
    'close': np.random.rand(365) * 100
})

# Convertir la columna de fecha a datetime y establecerla como índice
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Calcular la diferencia día a día en el precio de cierre
df['daily_change'] = df['close'].diff()

print(df.head())
```
En este DataFrame, la nueva columna 'daily_change' representa el cambio en el precio de cierre de la acción de un día a otro. Puedes ver que el primer valor es NaN, porque no hay un día anterior con el que comparar el primer día.

- **Selección y filtrado:** Puedes seleccionar subconjuntos de tus datos basándote en la fecha y la hora. Por ejemplo, puedes seleccionar todos los datos del año 2020, o todos los datos de las 9:00 a las 17:00, y así sucesivamente.
```python
# Seleccionar datos para enero de 2023
df_january = df['2023-01']

print(df_january)
```
Seleccionar y filtrar datos basándose en la fecha y la hora es una técnica muy útil en muchos campos.

#### Selección y filtrado en un escenario del mundo real.
Supongamos que trabajas en un comercio minorista y tienes datos de ventas de varios años. Estás interesado en analizar las ventas de la temporada navideña de cada año. Podrías utilizar la selección y filtrado para hacer esto.
```python
import pandas as pd
import numpy as np

# Crear un DataFrame con 3 años de datos de ventas (valores aleatorios para este ejemplo)
df = pd.DataFrame({
    'date': pd.date_range(start='2021-01-01', end='2023-12-31', freq='D'),
    'sales': np.random.rand(1096) * 1000
})

# Convertir la columna de fecha a datetime y establecerla como índice
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Seleccionar datos para la temporada navideña (diciembre) de cada año
df_december = df[df.index.month == 12]

print(df_december)
```
En este DataFrame, df_december contiene solo los datos de ventas de diciembre de cada año. Puedes utilizar estos datos para analizar las tendencias de las ventas navideñas, comparar las ventas de diferentes años y planificar la próxima temporada de vacaciones.

## Rendimiento
A medida que trabajas con conjuntos de datos más grandes, el rendimiento puede convertirse en un problema. Aprenderemos cómo mejorar el rendimiento de nuestros códigos de Pandas mediante el uso de operaciones vectorizadas (que son más rápidas que los bucles en Python) y reduciendo el uso de memoria.

- **Operaciones vectorizadas:** Los DataFrame y las Series de pandas están construidos sobre la biblioteca NumPy, que es rápida y eficiente debido a su uso de operaciones vectorizadas. Una operación vectorizada es una operación que se realiza en un conjunto de valores a la vez, en lugar de en un solo valor a la vez. En el contexto de pandas, esto significa aplicar una operación a una Serie o un DataFrame entero a la vez, en lugar de aplicarla a cada valor de la Serie o del DataFrame uno por uno (que es lo que sucede cuando usas un bucle for en Python). Las operaciones vectorizadas son mucho más rápidas que los bucles for, por lo que siempre debes tratar de usar operaciones vectorizadas cuando sea posible.

```python
import pandas as pd
import numpy as np

# Crear un DataFrame de ejemplo
df = pd.DataFrame({
    'A': np.random.rand(1000000),
    'B': np.random.rand(1000000),
})

# Usar una operación vectorizada para sumar las columnas A y B
df['C'] = df['A'] + df['B']
```

- **Reducción del uso de memoria:** Pandas no es especialmente eficiente en cuanto a memoria, y trabajar con conjuntos de datos grandes puede causar problemas de rendimiento. Aquí hay algunas técnicas que puedes usar para reducir el uso de memoria de tus DataFrames:

Uso de tipos de datos más eficientes: Pandas tiende a usar tipos de datos que ocupan más memoria de la necesaria. Por ejemplo, podría usar int64 (un entero de 64 bits) para almacenar una columna de datos que solo contiene los números 0 y 1. Podrías reducir el uso de memoria cambiando el tipo de datos de esa columna a int8 (un entero de 8 bits).

Uso del parámetro low_memory en read_csv(): Cuando lees un archivo CSV con pandas, puedes pasar el parámetro low_memory=True para reducir el uso de memoria.
```python
# Crear un DataFrame de ejemplo
df = pd.DataFrame({
    'A': pd.Series(range(100000), dtype='int64'),
    'B': pd.Series(range(100000), dtype='int64'),
})

# Ver el uso de memoria actual
print(df.memory_usage(deep=True))

# Cambiar el tipo de datos de la columna 'A' a int8
df['A'] = df['A'].astype('int8')

# Ver el uso de memoria después de cambiar el tipo de datos
print(df.memory_usage(deep=True))
```
En este ejemplo, cambiamos el tipo de datos de la columna 'A' de int64 a int8, lo que reduce significativamente el uso de memoria de esa columna.

### Actividad

Ahora veamos como poner en practica en un conjunto de datos del mundo real.

[Ver Actividad](https://github.com/apholdings/Ciencia_de_Datos_con_Python/blob/main/8%29%20Pandas%20Avanzado/Titanic%20-%20Machine%20Learning%20From%20Disaster/README.md)