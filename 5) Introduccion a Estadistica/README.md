# 5) Introducción a la Estadística
Descripción general de la estadística: Por qué es importante la estadística en ciencia de datos y machine learning.

- **Estadística descriptiva:** Medidas de tendencia central (media, mediana, moda), medidas de dispersión (varianza, desviación estándar), cuartiles y percentiles.

- **Distribuciones de probabilidad:** Distribuciones normales, distribuciones binomiales.
Inferencia estadística: Pruebas de hipótesis, intervalos de confianza.

- **Correlación y regresión:** Correlación de Pearson, coeficiente de determinación (R^2), regresión lineal simple.

- **Actividad:** Aplicar técnicas de estadística descriptiva e inferencial a un conjunto de datos.

### Estadística Descriptiva: Medidas de tendencia central y variabilidad.
Las medidas de tendencia central y de variabilidad son componentes fundamentales de la estadística descriptiva. Estas métricas ayudan a describir y comprender los conjuntos de datos al proporcionar información sobre el "centro" del conjunto de datos y cuánto se dispersan los datos alrededor de este "centro".

Supongamos que tenemos el siguiente conjunto de datos:
```python
import pandas as pd

data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 2, 3, 3, 3])
```

#### Medidas de tendencia central:
- **Media:** La media es el promedio de un conjunto de números. Se calcula sumando todos los números en el conjunto de datos y dividiendo por la cantidad de números en el conjunto.
```python
mean = data.mean()
print(f"Media: {mean}")
```

- **Mediana:** La mediana es el valor medio de un conjunto de datos cuando los datos se ordenan de menor a mayor. Si el conjunto de datos tiene un número impar de observaciones, la mediana es el número en el medio. Si hay un número par de observaciones, la mediana es el promedio de los dos números del medio.
```python
median = data.median()
print(f"Mediana: {median}")
```

- **Moda:** La moda es el valor que aparece con más frecuencia en un conjunto de datos. Un conjunto de datos puede tener una moda (unimodal), más de una moda (bimodal o multimodal) o ninguna moda (no modal).
```python
mode = data.mode()
print(f"Moda: {mode.values}")
```

#### Medidas de variabilidad (o dispersión):
- **Rango:** El rango es la diferencia entre el valor máximo y mínimo en un conjunto de datos.
```python
range_ = data.max() - data.min()
print(f"Rango: {range_}")
```

- **Varianza:** La varianza es una medida de cómo se dispersan los valores en un conjunto de datos alrededor de la media. Se calcula como el promedio de las diferencias al cuadrado entre cada valor del conjunto de datos y la media del conjunto de datos.
```python
variance = data.var()
print(f"Varianza: {variance}")
```

- **Desviación estándar:** La desviación estándar es la raíz cuadrada de la varianza. Proporciona una medida de dispersión que está en las mismas unidades que los datos.
```python
std_dev = data.std()
print(f"Desviación Estándar: {std_dev}")
```

- **Cuartiles y percentiles:** Los cuartiles son los tres puntos que dividen el conjunto de datos en cuatro partes iguales. Los percentiles son los 99 puntos que dividen el conjunto de datos en 100 partes iguales.
```python
quartiles = data.quantile([0.25, 0.5, 0.75])
print(f"Cuartiles:\n{quartiles}")

percentiles = data.quantile([i/100 for i in range(1, 101)])
print(f"Percentiles:\n{percentiles}")
```

### Estadística inferencial: Pruebas de hipótesis, valores p.

#### Pruebas de hipótesis:
Una prueba de hipótesis es un método estadístico que se utiliza para tomar decisiones sobre una población basándose en los datos de la muestra. En una prueba de hipótesis, se plantea una hipótesis nula (H0) que representa una afirmación de igualdad o de no efecto. 

Además, se plantea una hipótesis alternativa (H1) que representa una afirmación de desigualdad o efecto. Por ejemplo, si estás probando si una moneda está sesgada, la hipótesis nula podría ser que la moneda es justa (H0: P = 0.5), y la hipótesis alternativa podría ser que la moneda está sesgada (H1: P ≠ 0.5).

#### Valores p: 
El valor p es una medida de la evidencia en contra de la hipótesis nula. Proporciona la probabilidad de obtener los resultados observados (o más extremos) si la hipótesis nula es cierta. Un valor p pequeño (generalmente, menos de 0.05) indica fuerte evidencia en contra de la hipótesis nula, por lo que se rechaza la hipótesis nula. 

Un valor p grande (generalmente, más de 0.05) indica evidencia débil en contra de la hipótesis nula, por lo que no se puede rechazar la hipótesis nula.

##### Ejemplo:
Te mostraré cómo realizar una prueba t de Student para una muestra en Python utilizando la biblioteca SciPy. La prueba t se utiliza para determinar si la media de una población difiere significativamente de un valor específico (o de la media de otra población).

Digamos que tienes un conjunto de datos de las alturas de una muestra de individuos, y quieres comprobar si la altura media de estas personas es significativamente diferente de 170 cm.

Primero, importamos las bibliotecas necesarias y creamos nuestros datos:
```python
import numpy as np
import scipy.stats as stats

# Generamos datos de muestra
np.random.seed(0)  # para reproducibilidad
heights = np.random.normal(loc=175, scale=10, size=100)  # alturas con una media de 175 cm y una desviación estándar de 10 cm

# Luego realizamos la prueba
t_statistic, p_value = stats.ttest_1samp(heights, 170)

print(f"Estadística t: {t_statistic}")
print(f"Valor p: {p_value}")
```

En este caso, stats.ttest_1samp realiza una prueba t de una muestra. El primer argumento es la muestra de datos, y el segundo argumento es la media de la población bajo la hipótesis nula (en este caso, 170 cm).

La función devuelve dos valores: la estadística t y el valor p. La estadística t es una medida de cuánto difiere la media de la muestra de la media bajo la hipótesis nula, y el valor p es la probabilidad de obtener una diferencia al menos tan extrema como la observada, asumiendo que la hipótesis nula es cierta.

Si el valor p es pequeño (por lo general, menor a 0.05), se rechaza la hipótesis nula y se concluye que la media de la muestra es significativamente diferente de 170 cm. Si el valor p es grande, no se puede rechazar la hipótesis nula.

### Probabilidad: Fundamentos de la probabilidad
La probabilidad es una rama de las matemáticas que se ocupa de los eventos y sus posibilidades de ocurrencia.

**Fundamentos de la probabilidad:** La probabilidad mide la certeza de que un evento en particular va a ocurrir, y se expresa en una escala de 0 a 1. Un evento con una probabilidad de 0 es imposible, mientras que un evento con una probabilidad de 1 es cierto. La probabilidad de todos los posibles resultados de un experimento siempre suma 1. Por ejemplo, la probabilidad de sacar una cara o una cruz en el lanzamiento de una moneda justa es 1, ya que esos son los únicos dos posibles resultados.

La probabilidad también se puede entender en términos de frecuencia relativa. Si un experimento se repite muchas veces bajo las mismas condiciones, la probabilidad de un evento es aproximadamente igual al número de veces que el evento ocurrió dividido por el número total de repeticiones del experimento.

**Probabilidad condicional:** La probabilidad condicional de un evento es la probabilidad de que el evento ocurra dado que otro evento ya ha ocurrido. Se denota como P(A|B), que se lee "la probabilidad de A dado B". Por ejemplo, si estamos lanzando dos monedas, la probabilidad de que ambas sean caras es 0.25. Sin embargo, si ya sabemos que la primera moneda fue cara, la probabilidad condicional de que la segunda moneda sea cara es 0.5.

La probabilidad condicional es fundamental para muchas conceptos en estadística y aprendizaje automático, incluyendo la regla de Bayes, que proporciona una forma de actualizar nuestras creencias sobre un evento dado nueva evidencia.

##### Ejemplo
Te mostraré un ejemplo sencillo de probabilidad condicional utilizando Python.

Imagina que tienes un mazo de cartas (52 cartas en total, 13 de cada uno de los 4 palos: corazones, diamantes, tréboles y picas). Queremos saber cuál es la probabilidad de que una carta robada al azar sea un corazón dado que sabemos que es roja. Sabemos que hay 26 cartas rojas en total (13 corazones y 13 diamantes), así que podemos calcular esta probabilidad de la siguiente manera:
```python
# Número total de corazones y de cartas rojas
total_hearts = 13
total_red_cards = 26

# Probabilidad condicional de que una carta sea un corazón dado que es roja
prob_heart_given_red = total_hearts / total_red_cards

print(f"La probabilidad de que una carta sea un corazón dado que sabemos que es roja es {prob_heart_given_red}")
```

Este es un ejemplo simple, pero ilustra cómo puedes usar la probabilidad condicional para calcular la probabilidad de un evento dado que sabes que otro evento ha ocurrido.


### Correlacion y Regresion
- **Correlacion:** La correlación mide la relación lineal entre dos variables. Es un valor entre -1 y 1, donde 1 significa una correlación positiva perfecta, -1 una correlación negativa perfecta, y 0 ninguna correlación. La correlación puede ser una herramienta útil para descubrir relaciones entre variables en tus datos.

En Python, puedes usar el método corr() de un DataFrame de pandas para calcular la correlación entre todas las parejas de columnas numéricas. 
```python
correlation_matrix = df.corr()
```

- **Regresión:** La regresión es un enfoque para modelar la relación entre una variable dependiente y una o más variables independientes. La regresión lineal simple es el caso más simple, en el que modelamos la relación entre una variable dependiente y una variable independiente como una línea recta.

En Python, puedes usar la biblioteca statsmodels para ajustar un modelo de regresión lineal. Por ejemplo:
```python
import statsmodels.api as sm

X = df['variable_independiente']
y = df['variable_dependiente']

X = sm.add_constant(X)  # Agregar una constante (intercepto) al modelo

model = sm.OLS(y, X)  # Crear el modelo de regresión lineal
results = model.fit()  # Ajustar el modelo a los datos

print(results.summary())  # Imprimir un resumen de los resultados
```

### Actividad

Muy bien, ahora pondremos en practica lo aprendido, tenemos que analizar el conjuunuto de datos con el que trabajamos en la semana anterior, esta vez caluclaremos las variables de estadistica que aprendimos en esta semana.

[Ver Actividad Completa](https://github.com/apholdings/Ciencia_de_Datos_con_Python/tree/main/5%29%20Introduccion%20a%20Estadistica/Titanic%20-%20Machine%20Learning%20From%20Disaster)