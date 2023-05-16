# 5) Introducción a la Estadística
Descripción general de la estadística: Por qué es importante la estadística en ciencia de datos y machine learning.

- **Estadística descriptiva:** Medidas de tendencia central (media, mediana, moda), medidas de dispersión (varianza, desviación estándar), cuartiles y percentiles.

- **Distribuciones de probabilidad:** Distribuciones normales, distribuciones binomiales.
Inferencia estadística: Pruebas de hipótesis, intervalos de confianza.

- **Correlación y regresión:** Correlación de Pearson, coeficiente de determinación (R^2), regresión lineal simple.

- **Actividad:** Aplicar técnicas de estadística descriptiva e inferencial a un conjunto de datos.

### Estadística Descriptiva: Medidas de tendencia central y variabilidad.
Las medidas de tendencia central y de variabilidad son componentes fundamentales de la estadística descriptiva. Estas métricas ayudan a describir y comprender los conjuntos de datos al proporcionar información sobre el "centro" del conjunto de datos y cuánto se dispersan los datos alrededor de este "centro".

#### Medidas de tendencia central:
- **Media:** La media es el promedio de un conjunto de números. Se calcula sumando todos los números en el conjunto de datos y dividiendo por la cantidad de números en el conjunto.

- **Mediana:** La mediana es el valor medio de un conjunto de datos cuando los datos se ordenan de menor a mayor. Si el conjunto de datos tiene un número impar de observaciones, la mediana es el número en el medio. Si hay un número par de observaciones, la mediana es el promedio de los dos números del medio.

- **Moda:** La moda es el valor que aparece con más frecuencia en un conjunto de datos. Un conjunto de datos puede tener una moda (unimodal), más de una moda (bimodal o multimodal) o ninguna moda (no modal).

#### Medidas de variabilidad (o dispersión):
- **Rango:** El rango es la diferencia entre el valor máximo y mínimo en un conjunto de datos.

- **Varianza:** La varianza es una medida de cómo se dispersan los valores en un conjunto de datos alrededor de la media. Se calcula como el promedio de las diferencias al cuadrado entre cada valor del conjunto de datos y la media del conjunto de datos.

- **Desviación estándar:** La desviación estándar es la raíz cuadrada de la varianza. Proporciona una medida de dispersión que está en las mismas unidades que los datos.

- **Cuartiles y percentiles:** Los cuartiles son los tres puntos que dividen el conjunto de datos en cuatro partes iguales. Los percentiles son los 99 puntos que dividen el conjunto de datos en 100 partes iguales.

### Estadística inferencial: Pruebas de hipótesis, valores p.

#### Pruebas de hipótesis:
Una prueba de hipótesis es un método estadístico que se utiliza para tomar decisiones sobre una población basándose en los datos de la muestra. En una prueba de hipótesis, se plantea una hipótesis nula (H0) que representa una afirmación de igualdad o de no efecto. 

Además, se plantea una hipótesis alternativa (H1) que representa una afirmación de desigualdad o efecto. Por ejemplo, si estás probando si una moneda está sesgada, la hipótesis nula podría ser que la moneda es justa (H0: P = 0.5), y la hipótesis alternativa podría ser que la moneda está sesgada (H1: P ≠ 0.5).

#### Valores p: 
El valor p es una medida de la evidencia en contra de la hipótesis nula. Proporciona la probabilidad de obtener los resultados observados (o más extremos) si la hipótesis nula es cierta. Un valor p pequeño (generalmente, menos de 0.05) indica fuerte evidencia en contra de la hipótesis nula, por lo que se rechaza la hipótesis nula. 

Un valor p grande (generalmente, más de 0.05) indica evidencia débil en contra de la hipótesis nula, por lo que no se puede rechazar la hipótesis nula.

### Probabilidad: Fundamentos de la probabilidad
La probabilidad es una rama de las matemáticas que se ocupa de los eventos y sus posibilidades de ocurrencia.

**Fundamentos de la probabilidad:** La probabilidad mide la certeza de que un evento en particular va a ocurrir, y se expresa en una escala de 0 a 1. Un evento con una probabilidad de 0 es imposible, mientras que un evento con una probabilidad de 1 es cierto. La probabilidad de todos los posibles resultados de un experimento siempre suma 1. Por ejemplo, la probabilidad de sacar una cara o una cruz en el lanzamiento de una moneda justa es 1, ya que esos son los únicos dos posibles resultados.

La probabilidad también se puede entender en términos de frecuencia relativa. Si un experimento se repite muchas veces bajo las mismas condiciones, la probabilidad de un evento es aproximadamente igual al número de veces que el evento ocurrió dividido por el número total de repeticiones del experimento.

**Probabilidad condicional:** La probabilidad condicional de un evento es la probabilidad de que el evento ocurra dado que otro evento ya ha ocurrido. Se denota como P(A|B), que se lee "la probabilidad de A dado B". Por ejemplo, si estamos lanzando dos monedas, la probabilidad de que ambas sean caras es 0.25. Sin embargo, si ya sabemos que la primera moneda fue cara, la probabilidad condicional de que la segunda moneda sea cara es 0.5.

La probabilidad condicional es fundamental para muchas conceptos en estadística y aprendizaje automático, incluyendo la regla de Bayes, que proporciona una forma de actualizar nuestras creencias sobre un evento dado nueva evidencia.