# 8) Pandas Avanzado
Pandas es una de las bibliotecas más populares y útiles en Python para la manipulación y el análisis de datos. Ya hemos cubierto algunas de las funcionalidades básicas de Pandas en las semanas anteriores, pero hay mucho más que aprender. 

En esta semana, vamos a profundizar en las capacidades de Pandas, aprendiendo técnicas más avanzadas y poderosas que te permitirán sacar aún más partido a tus datos.

1. **Manipulaciones de datos más complejas:** Ya hemos visto cómo utilizar funciones como groupby(), merge(), y concat(). Pero Pandas ofrece muchas otras herramientas para manipular datos, como apply() para aplicar funciones personalizadas a los datos, las tablas dinámicas para resumir los datos de manera similar a Excel, y el multi-index para tener múltiples niveles de índices en un DataFrame.

2. **Manipulación de datos de series temporales:** Muchos conjuntos de datos incluyen información temporal. Pandas ofrece una serie de funcionalidades para trabajar con datos de series temporales, como herramientas para el análisis de fechas (por ejemplo, extracción de mes, día de la semana, etc. de una fecha) y remuestreo (cambiando la frecuencia de los datos de tiempo).

3. **Rendimiento:** A medida que trabajas con conjuntos de datos más grandes, el rendimiento puede convertirse en un problema. Aprenderemos cómo mejorar el rendimiento de nuestros códigos de Pandas mediante el uso de operaciones vectorizadas (que son más rápidas que los bucles en Python) y reduciendo el uso de memoria.

4. **Actividad:** Para poner en práctica lo que hemos aprendido, trabajaremos con un conjunto de datos desafiante y aplicaremos nuestras nuevas habilidades de Pandas avanzado.

### Manipulaciones de datos más complejas
Las manipulaciones de datos más complejas son las operaciones que nos permiten transformar nuestros datos de maneras más sofisticadas y flexibles que las operaciones básicas. 

Estas son algunas de las manipulaciones de datos más complejas que podemos realizar con Pandas:

- **Función apply():** Esta es una de las funciones más versátiles en Pandas. Te permite aplicar una función personalizada a cada elemento de una Serie, o a cada fila o columna de un DataFrame. Por ejemplo, podrías tener una columna de fechas en un formato de cadena de texto y querrías convertirlas en objetos de fecha y hora de Python. Podrías definir una función personalizada para hacer esta conversión y luego usar apply() para aplicarla a toda la columna.

- **Tablas dinámicas:** Si alguna vez has trabajado con Excel, probablemente estés familiarizado con las tablas dinámicas. Permiten resumir y agrupar los datos de formas útiles para el análisis. Por ejemplo, podrías tener un conjunto de datos de ventas y querrías resumir las ventas totales por mes y por producto. Podrías hacer esto fácilmente con una tabla dinámica.

- **Multi-index:** En algunos casos, puede ser útil tener múltiples niveles de índices en un DataFrame. Por ejemplo, podrías tener datos de ventas para diferentes productos en diferentes tiendas, y querrías indexar los datos tanto por producto como por tienda. Los multi-índices de Pandas te permiten hacer esto.

Aquí tienes un ejemplo de cómo podríamos usar estas técnicas en un conjunto de datos:

```python
import pandas as pd

# Supongamos que tenemos un DataFrame de ventas
df = pd.DataFrame({
    'date': ['2020-01-01', '2020-01-02', '2020-01-02', '2020-01-03'],
    'store': ['A', 'A', 'B', 'A'],
    'product': ['X', 'X', 'Y', 'Z'],
    'sales': [10, 15, 12, 20]
})

# Convertir la columna de fecha a datetime usando apply()
df['date'] = pd.to_datetime(df['date'])

# Crear una tabla dinámica para resumir las ventas por tienda y producto
pivot = df.pivot_table(values='sales', index='product', columns='store', aggfunc='sum')

# Establecer un multi-index con las columnas de tienda y producto
df.set_index(['store', 'product'], inplace=True)
```

Estas son solo algunas de las manipulaciones de datos más complejas que puedes hacer con Pandas. Las posibilidades son casi infinitas, y la mejor manera de aprender es practicando con tus propios conjuntos de datos.