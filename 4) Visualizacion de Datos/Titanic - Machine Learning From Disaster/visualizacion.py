"""
La visualización de datos es una parte muy importante en la ciencia de datos porque 
puede ayudarnos a entender mejor los datos y a tomar decisiones sobre cómo tratar con ellos.

Podemos comenzar con algunos gráficos simples para entender la distribución de ciertas 
variables. Por ejemplo, podríamos querer ver la distribución de las edades de los pasajeros 
o la relación entre la supervivencia y otras variables. 

Aquí tienes un código de ejemplo para hacer esto:
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
El módulo seaborn es un módulo de Python para la visualización de datos basado en 
matplotlib que proporciona una interfaz de alto nivel para dibujar gráficos estadísticos 
atractivos e informativos. 
Si no lo tienes instalado, puedes instalarlo con pip: pip install seaborn.
"""

# Cargar los datos preprocesados
from preprocesamiento import df_train

# Histograma de las edades
"""
Histograma de las edades: Este gráfico nos muestra la distribución de las edades de los 
pasajeros en el Titanic. El eje x representa diferentes grupos de edad y el eje y representa
la cantidad de pasajeros en cada grupo de edad. Este gráfico nos puede dar una idea general
de la demografía de los pasajeros en el Titanic. Por ejemplo, podemos ver si la mayoría 
de los pasajeros eran jóvenes, de mediana edad, o mayores.
"""
plt.figure(figsize=(10, 6))
plt.title("Distribución de las edades")
sns.histplot(df_train["Age"], kde=False, bins=30)
plt.show()

# Gráfico de barras de la supervivencia por género
"""
Gráfico de barras de la supervivencia por género: Este gráfico nos muestra la relación entre 
el género de los pasajeros y si sobrevivieron o no. El eje x representa la supervivencia 
(0 para los que no sobrevivieron y 1 para los que sobrevivieron), y el eje y representa el 
número de pasajeros. Las barras están coloreadas por género. Este gráfico puede ayudarnos a 
entender si el género tuvo algún impacto en la supervivencia de los pasajeros. 
Por ejemplo, si vemos que una proporción significativamente mayor de mujeres sobrevivió en 
comparación con los hombres, esto podría indicar que las mujeres tenían más probabilidades 
de sobrevivir.
"""
plt.figure(figsize=(10, 6))
plt.title("Supervivencia por género")
sns.countplot(x="Survived", hue="Sex", data=df_train)
plt.show()

# Gráfico de barras de la supervivencia por clase de pasajero
"""
Gráfico de barras de la supervivencia por clase de pasajero: Este gráfico es similar al 
anterior, pero en lugar de mostrar la supervivencia por género, muestra la supervivencia por 
la clase de pasajero (1ª, 2ª, o 3ª clase). Este gráfico puede ayudarnos a entender si la 
clase de pasajero tuvo algún impacto en la supervivencia. Por ejemplo, si vemos que una 
proporción significativamente mayor de pasajeros de 1ª clase sobrevivió en comparación con 
los pasajeros de 2ª y 3ª clase, esto podría indicar que los pasajeros de 1ª clase tenían 
más probabilidades de sobrevivir.
"""
plt.figure(figsize=(10, 6))
plt.title("Supervivencia por clase de pasajero")
sns.countplot(x="Survived", hue="Pclass", data=df_train)
plt.show()

"""
Este script creará tres gráficos: un histograma de las edades de los pasajeros, 
un gráfico de barras que muestra la supervivencia por género, y un gráfico de barras que 
muestra la supervivencia por clase de pasajero.
"""
