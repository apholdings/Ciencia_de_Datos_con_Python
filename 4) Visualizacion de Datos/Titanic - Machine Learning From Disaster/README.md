# Titanic - Machine Learning From Disaster

## Actividad - Limpieza y Transformación de Datos
Para consolidar lo aprendido, vamos a trabajar con un conjunto de datos del mundo real.

La tarea será cargar los datos, limpiarlos y transformarlos utilizando las habilidades adquiridas.

Se proporcionará un conjunto de datos con problemas comunes como datos faltantes, duplicados y columnas que necesitan ser transformadas.

Esta actividad ayudará a familiarizar a los estudiantes con el proceso de limpieza y transformación de datos, que es un paso crucial en cualquier proyecto de ciencia de datos.

### Descarga el Set de Datos
Usaremos el conjunto de datos ["Titanic: Machine Learning from Disaster"](https://www.kaggle.com/datasets/shuofxz/titanic-machine-learning-from-disaster?resource=download) disponible en Kaggle. 

Este es un conjunto de datos muy popular que es relativamente simple, pero que también ofrece muchas oportunidades para la limpieza y transformación de datos, la ingeniería de características y la aplicación de varios algoritmos de aprendizaje supervisado. 

Incluye datos sobre los pasajeros del Titanic, como la edad, el sexo, la clase de pasajero, el número de parientes a bordo y si sobrevivió o no.

### Importar Bibliotecas y Cargar Conjunto de Datos
1. Para comenzar, es necesario importar las bibliotecas necesarias y cargar los datos. Vamos a utilizar Pandas para manipular los datos y Matplotlib para la visualización de datos. 

```python
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df_train = pd.read_csv('train.csv')

# Mostrar las primeras filas del dataframe
print(df_train.head())
```

Este script cargará los datos de entrenamiento del archivo 'train.csv' y mostrará las primeras filas del dataframe. Esto nos dará una idea inicial de cómo se ven nuestros datos.

Luego, podemos comenzar a explorar y limpiar los datos. Por ejemplo, podríamos querer ver si hay valores faltantes en nuestros datos y tratar con ellos de alguna manera.

```python
# Verificar si hay valores faltantes
print(df_train.isnull().sum())

# Llenar los valores faltantes en la columna 'Age' con la mediana de las edades
df_train['Age'].fillna(df_train['Age'].median(), inplace=True)

# Eliminar la columna 'Cabin' debido a la gran cantidad de valores faltantes
df_train = df_train.drop(['Cabin'], axis=1)

# Mostrar las primeras filas del dataframe después de la limpieza
print(df_train.head())
```

Este script verificará si hay valores faltantes en cada columna del dataframe, llenará los valores faltantes en la columna 'Age' con la mediana de las edades, y eliminará la columna 'Cabin' debido a la gran cantidad de valores faltantes. Luego, mostrará las primeras filas del dataframe después de la limpieza.

Estos son solo algunos pasos básicos de preprocesamiento de datos. Dependiendo de tus objetivos y del conjunto de datos específico con el que estés trabajando, podrías necesitar hacer más limpieza y transformación de datos.

### Visualizacion de Datos
La visualización de datos es una parte muy importante en la ciencia de datos porque puede ayudarnos a entender mejor los datos y a tomar decisiones sobre cómo tratar con ellos.

Podemos comenzar con algunos gráficos simples para entender la distribución de ciertas variables. Por ejemplo, podríamos querer ver la distribución de las edades de los pasajeros o la relación entre la supervivencia y otras variables.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Cargar los datos preprocesados
from preprocesamiento import df_train

# Histograma de las edades
plt.figure(figsize=(10, 6))
plt.title("Distribución de las edades")
sns.histplot(df_train["Age"], kde=False, bins=30)
plt.show()
# Gráfico de barras de la supervivencia por género
plt.figure(figsize=(10, 6))
plt.title("Supervivencia por género")
sns.countplot(x="Survived", hue="Sex", data=df_train)
plt.show()
# Gráfico de barras de la supervivencia por clase de pasajero
plt.figure(figsize=(10, 6))
plt.title("Supervivencia por clase de pasajero")
sns.countplot(x="Survived", hue="Pclass", data=df_train)
plt.show()

```

Este script creará tres gráficos: un histograma de las edades de los pasajeros, un gráfico de barras que muestra la supervivencia por género, y un gráfico de barras que muestra la supervivencia por clase de pasajero.

Es importante entender la razon de por que hacemos esos graficos.

1. **Histograma de las edades:** Este gráfico nos muestra la distribución de las edades de los pasajeros en el Titanic. El eje x representa diferentes grupos de edad y el eje y representa la cantidad de pasajeros en cada grupo de edad. Este gráfico nos puede dar una idea general de la demografía de los pasajeros en el Titanic. Por ejemplo, podemos ver si la mayoría de los pasajeros eran jóvenes, de mediana edad, o mayores.
```python
plt.figure(figsize=(10, 6))
plt.title("Distribución de las edades")
sns.histplot(df_train["Age"], kde=False, bins=30)
plt.show()
```

2. **Gráfico de barras de la supervivencia por género:** Este gráfico nos muestra la relación entre el género de los pasajeros y si sobrevivieron o no. El eje x representa la supervivencia (0 para los que no sobrevivieron y 1 para los que sobrevivieron), y el eje y representa el número de pasajeros. Las barras están coloreadas por género. Este gráfico puede ayudarnos a entender si el género tuvo algún impacto en la supervivencia de los pasajeros. Por ejemplo, si vemos que una proporción significativamente mayor de mujeres sobrevivió en comparación con los hombres, esto podría indicar que las mujeres tenían más probabilidades de sobrevivir.
```python
plt.figure(figsize=(10, 6))
plt.title("Supervivencia por género")
sns.countplot(x="Survived", hue="Sex", data=df_train)
plt.show()
```

3. **Gráfico de barras de la supervivencia por clase de pasajero:** Este gráfico es similar al anterior, pero en lugar de mostrar la supervivencia por género, muestra la supervivencia por la clase de pasajero (1ª, 2ª, o 3ª clase). Este gráfico puede ayudarnos a entender si la clase de pasajero tuvo algún impacto en la supervivencia. Por ejemplo, si vemos que una proporción significativamente mayor de pasajeros de 1ª clase sobrevivió en comparación con los pasajeros de 2ª y 3ª clase, esto podría indicar que los pasajeros de 1ª clase tenían más probabilidades de sobrevivir.
```python
plt.figure(figsize=(10, 6))
plt.title("Supervivencia por clase de pasajero")
sns.countplot(x="Survived", hue="Pclass", data=df_train)
plt.show()
```

Ahora podemos ver otro ejercicio similar esta vez con un conjunto de datos mas complejo sobre bienes raices.
[House Prices - Advanced Regression Techniques](https://github.com/apholdings/Ciencia_de_Datos_con_Python/tree/main/4%29%20Visualizacion%20de%20Datos/House%20Prices%20-%20Advanced%20Regression%20Techniques)