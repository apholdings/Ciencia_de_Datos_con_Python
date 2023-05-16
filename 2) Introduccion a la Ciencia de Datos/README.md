# 2) Introducción a la Ciencia de Datos
#### ¿Qué es la ciencia de datos? 
Es el campo de estudio que utiliza algoritmos, métodos científicos y sistemas para extraer conocimiento y perspectivas de datos estructurados y no estructurados.

- **Roles en la ciencia de datos:** científico de datos, analista de datos, ingeniero de datos, etc.
- **Proceso de la ciencia de datos:** definir el problema, recoger los datos, procesar los datos, analizar los datos, interpretar los resultados.
- **Herramientas de la ciencia de datos:** Python, R, SQL, Excel, Tableau, etc.
- **Aplicaciones de la ciencia de datos:** desde la toma de decisiones empresariales hasta el desarrollo de productos y servicios innovadores.

### Profundizando en NumPy
NumPy (Numerical Python) es una biblioteca de Python que proporciona soporte para grandes matrices multidimensionales y matrices, junto con una gran colección de funciones matemáticas de alto nivel para operar en estas matrices.
Proporciona funciones para operaciones como la adición de matrices, la multiplicación, la transformada de Fourier, el álgebra lineal, etc.
NumPy es especialmente útil cuando se necesita realizar cálculos numéricos con Python.
``` python
# Importación de NumPy
import numpy as np

# Creación de una matriz en NumPy
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz)

# Realizar operaciones en la matriz
print("Suma de todos los elementos:", np.sum(matriz))
print("Transpuesta de la matriz:\n", np.transpose(matriz))
```

### Profundizando en Pandas
Pandas es una biblioteca de Python que proporciona estructuras de datos y funciones de análisis de datos extremadamente eficientes y flexibles.
Proporciona estructuras de datos como Series y DataFrames para manejar y analizar datos de manera eficiente.
Pandas es particularmente útil para el manejo de datos tabulares, como los que se encuentran en archivos CSV o en bases de datos SQL.
``` python
# Importación de Pandas
import pandas as pd

# Creación de un DataFrame en Pandas
data = {'Nombres': ['Ana', 'Juan', 'Pedro'], 'Edades': [25, 30, 35]}
df = pd.DataFrame(data)

# Realizar operaciones en el DataFrame
print("Información básica del DataFrame:\n")
print(df.info())
print("\nDescripción del DataFrame:\n")
print(df.describe())
```

### Profundizando en Matplotlib
Matplotlib es una biblioteca de Python para la creación de gráficos estáticos, animados e interactivos.
Proporciona una manera muy rápida de visualizar datos y figuras con calidad de publicación en varios formatos.
Puedes generar histogramas, gráficos de barras, gráficos de dispersión, gráficos de líneas, etc., con solo unas pocas líneas de código.
``` python
# Importación de Matplotlib
import matplotlib.pyplot as plt

# Creación de un gráfico de líneas
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 2]
plt.plot(x, y)
plt.show()
```


## El Proceso de la Ciencia de Datos
1. **Recolección de Datos:** El primer paso en cualquier proyecto de ciencia de datos es recoger los datos. Esto puede implicar la extracción de datos de bases de datos, la recopilación de datos a través de API, web scraping, o el uso de datos disponibles en archivos CSV, Excel, etc.
2. **Limpieza de Datos:** Los datos recogidos raramente están en el formato perfecto para el análisis. Por lo tanto, a menudo se requiere limpiar y preprocesar los datos.
3. **Análisis Exploratorio de Datos:** Esta etapa implica entender los datos, buscar patrones, relaciones entre variables, etc.
4. **Modelo de Machine Learning:** En esta etapa, se utilizan algoritmos de machine learning para construir un modelo que puede hacer predicciones o decisiones sin ser explícitamente programado para hacerlo.
5. **Validación del Modelo:** Aquí, se evalúa la precisión y eficacia del modelo.
6. **Despliegue del Modelo:** Una vez que el modelo está validado y probado, puede ser desplegado en un entorno de producción.

### Roles en la Ciencia de Datos
- *Analista de Datos:* Se enfocan principalmente en el análisis y la visualización de datos para ayudar a las empresas a tomar decisiones basadas en datos.
- *Ingeniero de Datos:* Se centran en la recopilación, almacenamiento y procesamiento de datos. Ellos construyen y mantienen los sistemas de datos que permiten a los analistas y científicos de datos hacer su trabajo.
- *Científico de Datos:* Combina habilidades de ambos roles anteriores y también puede construir modelos de machine learning para hacer predicciones basadas en datos.

### Herramientas en la Ciencia de Datos
- **Python:** Un lenguaje de programación de alto nivel muy popular en la ciencia de datos debido a su sintaxis clara y legible, y a las numerosas bibliotecas para el análisis de datos y machine learning.
- **R:** Un lenguaje de programación y un entorno de software para el análisis estadístico y la visualización de datos.
- **SQL:** Un lenguaje de programación utilizado para gestionar y manipular bases de datos.
- **Jupyter Notebooks:** Una aplicación web de código abierto que permite crear y compartir documentos que contienen código en vivo, ecuaciones, visualizaciones y texto narrativo. Es una herramienta esencial para la ciencia de datos.

## Manipulación de datos con Pandas
- **Carga de datos:** Lectura de datos desde CSVs, archivos Excel y bases de datos SQL.
- **Limpieza de datos:** Manejo de datos faltantes, datos duplicados y tipos de datos incorrectos.
- **Transformación de datos:** Creación de nuevas columnas, agregación de datos, fusión de marcos de datos.

### Carga de Datos con Pandas
Pandas es increíblemente eficiente para leer una variedad de formatos de datos, incluyendo CSV, Excel y SQL.
Para leer datos desde estos formatos, Pandas proporciona funciones como read_csv(), read_excel(), y read_sql().
Una vez leídos, los datos se almacenan en un objeto DataFrame, que es una estructura de datos bidimensional etiquetada con columnas que pueden ser de diferentes tipos.
``` python
# Importación de Pandas
import pandas as pd

# Leer un archivo CSV
df_csv = pd.read_csv('archivo.csv')

# Leer un archivo Excel
df_excel = pd.read_excel('archivo.xlsx')

# Leer de una base de datos SQL
from sqlalchemy import create_engine
engine = create_engine('sqlite:///database.db')
df_sql = pd.read_sql('SELECT * FROM tabla', engine)
```

## Limpieza de Datos con Pandas
Los datos del mundo real a menudo están llenos de errores, faltantes, duplicados, y pueden tener tipos de datos incorrectos.
Pandas proporciona funciones eficientes para manejar estos problemas.
Para tratar con los datos faltantes, Pandas proporciona funciones como dropna(), que elimina las filas o columnas con valores faltantes, y fillna(), que llena los valores faltantes con un valor específico.
Para tratar con los datos duplicados, Pandas proporciona la función drop_duplicates().
Para cambiar los tipos de datos de las columnas, Pandas proporciona la función astype().
[Ver Codigo de Ejemplo](limpieza_de_datos.py)

## Transformación de Datos con Pandas
Pandas proporciona una gran cantidad de funciones para transformar datos en un DataFrame.
Podemos crear nuevas columnas a partir de las existentes, utilizando operaciones matemáticas, funciones de string, funciones de fecha y hora, y más.
La función groupby() permite agregar datos basándose en alguna columna. Por ejemplo, podríamos calcular el promedio de todas las filas que tienen el mismo valor en una columna específica.
Los DataFrames pueden ser fusionados utilizando funciones como merge() y concat(), similares a las operaciones JOIN en SQL.
[Ver Codigo de Ejemplo](transformacion_de_datos.py)