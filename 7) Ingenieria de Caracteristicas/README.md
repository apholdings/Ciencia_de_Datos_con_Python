# 7) Ingeniería de Características
La ingeniería de características es una parte esencial del aprendizaje automático y la ciencia de datos. Es un proceso creativo que implica la creación de nuevas características a partir de las ya existentes para mejorar el rendimiento de los modelos de aprendizaje automático. Esta tarea es tanto un arte como una ciencia, y a menudo puede ser la diferencia entre un modelo mediocre y un modelo altamente efectivo.

### ¿Qué es la ingeniería de características?
La ingeniería de características es el proceso de utilizar el conocimiento de dominio para crear nuevas características (columnas de datos) que hacen que los algoritmos de aprendizaje automático funcionen mejor. Es una parte esencial del modelado predictivo y, cuando se hace bien, puede tener un impacto mayor en la eficacia del modelo que el algoritmo de aprendizaje automático que se utilice.

### ¿Por qué es importante la ingeniería de características?
Los algoritmos de aprendizaje automático aprenden una solución a un problema a partir de datos de muestra. Cuanto más relevante y significativa sea la información contenida en estos datos, mejor será la solución que el algoritmo pueda aprender.

La ingeniería de características mejora la eficacia del aprendizaje automático al transformar los datos brutos en una forma que es más adecuada para los algoritmos aprender. Aunque los algoritmos de aprendizaje automático pueden aprender a partir de los datos brutos, normalmente pueden aprender de manera más eficaz y eficiente a partir de datos que han sido transformados y organizados de manera inteligente.

### ¿cómo sabemos cuándo considerar la ingeniería de características y qué técnicas utilizar? 
Eso depende en gran medida del problema específico que estemos tratando de resolver y de los datos con los que estemos trabajando. Sin embargo, hay algunas situaciones comunes en las que la ingeniería de características puede ser especialmente útil:

Cuando nuestros datos tienen una estructura compleja que no puede ser capturada fácilmente por un modelo de aprendizaje automático. Por ejemplo, si tenemos una característica de fecha y hora, podríamos crear nuevas características como "hora del día", "día de la semana" o "mes del año", ya que estas podrían tener más relevancia predictiva.

Cuando nuestros datos tienen características categóricas. Los algoritmos de aprendizaje automático requieren entradas numéricas, por lo que necesitamos codificar las variables categóricas en una forma numérica. Una forma común de hacer esto es la codificación one-hot, donde cada valor único en la variable categórica se convierte en una nueva característica binaria.

Cuando nuestras características tienen una distribución sesgada o están en una escala diferente. Algunos algoritmos de aprendizaje automático pueden funcionar mejor cuando los datos están en una determinada forma. Podríamos transformar una característica con una distribución sesgada utilizando la transformación de logaritmo, o normalizar las características para que estén en la misma escala.

Cuando tenemos una gran cantidad de características y no todas son útiles. La selección de características es el proceso de elegir las características más útiles para un problema de aprendizaje automático. Esto puede ayudar a mejorar la eficacia del modelo y a reducir el tiempo de entrenamiento.

### ¿Cómo se hace la ingeniería de características?
La ingeniería de características puede implicar una variedad de actividades, entre las que se incluyen:

1. **Creación de características:** Por ejemplo, si tienes una característica de fecha y hora, podrías crear nuevas características como "hora del día", "día de la semana", "mes del año", etc.

2. **Transformación de características:** Algunos algoritmos de aprendizaje automático pueden funcionar mejor cuando los datos están en una determinada forma. Por ejemplo, podrías transformar una característica con una distribución sesgada utilizando la transformación de logaritmo.

3. **Codificación de variables categóricas:** Los algoritmos de aprendizaje automático requieren entradas numéricas, por lo que necesitamos codificar las variables categóricas en una forma numérica. Una forma común de hacer esto es el "one-hot encoding", donde cada valor único en la variable categórica se convierte en una nueva característica binaria.

4. **Selección de características:** No todas las características son útiles para un problema de aprendizaje automático. Algunas características pueden no contener información relevante, mientras que otras pueden contener información duplicada. La selección de características es el proceso de elegir las características más útiles para un problema de aprendizaje automático.

La ingeniería de características requiere una combinación de conocimientos de dominio, intuición y experimentación. A menudo, es útil visualizar los datos y las relaciones entre las características para obtener ideas para la ingeniería de características.


## Tipos de Ingenieria de Caracteristica y Ejemplos
Existen muchas técnicas de ingeniería de características y cuál se utiliza depende del problema específico y de los datos.

- **Imputación:** Esta técnica se utiliza cuando nuestros datos tienen valores faltantes. Podemos llenar los valores faltantes con un valor específico, la media, la mediana, el modo, etc.
```python
import pandas as pd
import numpy as np

# Crear un DataFrame con valores faltantes
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
})

# Llenar los valores faltantes con la media
df.fillna(df.mean(), inplace=True)
```

- **Binning:** Esta técnica se utiliza para convertir una característica numérica en una característica categórica. Podemos hacer esto dividiendo el rango de la característica en bins y luego asignando los valores a estos bins. 
```python
# Crear una característica numérica
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
})

# Convertir la característica numérica en una característica categórica utilizando binning
df['A_binned'] = pd.cut(df['A'], bins=[0, 2, 4, 6, 8, 10], labels=['Bin_1', 'Bin_2', 'Bin_3', 'Bin_4', 'Bin_5'])
```

- **Creación de características polinómicas:** Esta técnica se utiliza para capturar las relaciones entre las características que no son lineales.
```python
from sklearn.preprocessing import PolynomialFeatures

# Crear un DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 3, 4, 5, 6]
})

# Crear características polinómicas
poly = PolynomialFeatures(degree=2, interaction_only=False, include_bias=False)
df_poly = pd.DataFrame(poly.fit_transform(df), columns=poly.get_feature_names(df.columns))
```

- **Codificación de variables categóricas:** Esta técnica se utiliza para convertir las características categóricas en una forma que los algoritmos de aprendizaje automático puedan utilizar. Existen varias técnicas para esto, como One-Hot Encoding, Ordinal Encoding, entre otras.
```python
# Crear una característica categórica
df = pd.DataFrame({
    'A': ['cat', 'dog', 'cat', 'dog', 'cat']
})

# Convertir la característica categórica en características numéricas utilizando One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=['A'])
```

## Variables Categoricas
Las variables categóricas son aquellas que contienen valores de etiqueta en lugar de valores numéricos. El número de posibles valores a menudo se limita a un conjunto fijo. Por ejemplo, los usuarios suelen describir su género como hombre o mujer. Aunque podemos encontrar formas de convertir estas variables en números, los algoritmos de aprendizaje automático pueden no ser capaces de interpretar correctamente las relaciones entre estos números.

Por lo tanto, necesitamos encontrar una forma de codificar estas variables categóricas que permita a los algoritmos de aprendizaje automático entender mejor los patrones en los datos.

### Las técnicas de codificación más comunes son:
- **One-Hot Encoding:** Convierte cada valor de una característica categórica en una nueva característica binaria (0 o 1). Este método es muy eficaz cuando las categorías no tienen ningún tipo de relación ordinal.
```python
import pandas as pd

df = pd.DataFrame({
    'A': ['cat', 'dog', 'mouse']
})

df_encoded = pd.get_dummies(df, columns=['A'])

print(df_encoded)
```
Resultado:

|     |A_cat  |A_dog  |A_mouse  |
|:---:|:-----:|:-----:|:-------:|
| 0   |  1    |  0    |   0     |
| 1   |  0    |  1    |   0     |
| 2   |  0    |  0    |   1     |

- **Ordinal Encoding:** Asigna un valor único a cada categoría de una característica categórica. Este método es útil cuando las categorías tienen una relación ordinal clara, es decir, cuando se puede decir que una categoría es "mayor" o "menor" que otra.
```python
from sklearn.preprocessing import OrdinalEncoder

df = pd.DataFrame({
    'A': ['cold', 'warm', 'hot']
})

ordinal_encoder = OrdinalEncoder()
df['A'] = ordinal_encoder.fit_transform(df[['A']])

print(df)
```
Resultado:

|     |   A   |
|:---:|:-----:|
|  0  |   1   |
|  1  |   0   |
|  2  |   0   | 


- **Binary Encoding:** Este método es una combinación de Hash encoding y One-Hot encoding. Primero, las categorías se codifican como números ordinales. Luego, los números ordinales se convierten en binario. Este método puede ser útil cuando una característica categórica tiene muchas categorías, ya que puede reducir la dimensionalidad de los datos.
```python
import category_encoders as ce

df = pd.DataFrame({
    'A': ['cat', 'dog', 'mouse', 'bird', 'fish', 'elephant']
})

encoder = ce.BinaryEncoder(cols=['A'])
df_encoded = encoder.fit_transform(df)

print(df_encoded)
```
Resultado (simplificado):

|     |  A_0  |  A_1  |  A_2  |  A_3  |
|:---:|:-----:|:-----:|:-----:|:-----:|
|  0  |   0   |   0   |   0   |   1   |
|  1  |   0   |   0   |   1   |   0   |
|  2  |   0   |   0   |   1   |   1   |
|  3  |   0   |   1   |   0   |   0   |
|  4  |   0   |   1   |   0   |   1   |
|  5  |   0   |   1   |   1   |   0   |

En la elección de qué técnica de codificación utilizar, es importante considerar la naturaleza de la característica categórica (si tiene una relación ordinal o no), el número de categorías únicas y el algoritmo de aprendizaje automático que se utilizará.

### Actividad

Ahora veamos como poner en practica la ingenieria de caracteristicas en un conjuntod e datos del mundo real.

[Ver Actividad](https://github.com/apholdings/Ciencia_de_Datos_con_Python/tree/main/7%29%20Ingenieria%20de%20Caracteristicas/Titanic%20-%20Machine%20Learning%20From%20Disaster)