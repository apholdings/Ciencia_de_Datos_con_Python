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