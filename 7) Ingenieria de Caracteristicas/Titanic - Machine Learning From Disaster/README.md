# Titanic - Machine Learning From Disaster

## Actividad - Aplicar técnicas de ingeniería de características a un conjunto de datos y discutir el impacto en un modelo simple.

Podemos tomar el conjunto de datos de Titanic y realizar algunas ingenierías de características. Para este ejemplo, vamos a realizar codificación one-hot en la característica 'Sex' y codificación ordinal en la característica 'Embarked'. Además, vamos a crear una nueva característica 'FamilySize' que será la suma de 'SibSp' y 'Parch'.

```python
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# Cargar los datos
df_train = pd.read_csv("train.csv")

# Llenar los valores faltantes en la columna 'Embarked' con el valor más común
df_train["Embarked"].fillna(df_train["Embarked"].mode()[0], inplace=True)

# Crear una nueva característica 'FamilySize'
df_train['FamilySize'] = df_train['SibSp'] + df_train['Parch']

# Codificación One-Hot para la característica 'Sex'
df_train = pd.get_dummies(df_train, columns=['Sex'])

# Codificación Ordinal para la característica 'Embarked'
ordinal_encoder = OrdinalEncoder()
df_train['Embarked'] = ordinal_encoder.fit_transform(df_train[['Embarked']])

print(df_train.head())
```

Este código carga el conjunto de datos de Titanic, llena los valores faltantes en 'Embarked', crea una nueva característica 'FamilySize', realiza codificación one-hot en 'Sex' y codificación ordinal en 'Embarked'. Ahora, nuestras características están listas para ser utilizadas en un algoritmo de machine learning.

### Desglose Paso a Paso
1. **Cargar los datos:** Usamos pandas.read_csv para cargar los datos del archivo CSV. Es el primer paso en cualquier análisis de datos.

2. **Llenar los valores faltantes en la columna 'Embarked':** La columna 'Embarked' tiene algunos valores faltantes. Los algoritmos de aprendizaje automático no pueden manejar los valores faltantes, por lo que los rellenamos con el valor más común (la moda) en esa columna. Esto se llama imputación y es una estrategia común para tratar con los datos faltantes.

3. **Crear una nueva característica 'FamilySize':** Creamos una nueva característica llamada 'FamilySize' sumando las características 'SibSp' y 'Parch', que representan el número de hermanos/cónyuges y padres/hijos a bordo, respectivamente. La ingeniería de características como esta puede ayudar a mejorar el rendimiento de los modelos de aprendizaje automático al combinar o transformar las características existentes para capturar más información.

4. **Codificación One-Hot para la característica 'Sex':** La característica 'Sex' es categórica, pero los algoritmos de aprendizaje automático requieren que los datos estén en formato numérico. Usamos la codificación one-hot para convertir la característica categórica 'Sex' en un formato numérico. Crea nuevas columnas para cada valor único en la característica 'Sex', y para cada fila, pone un 1 en la columna correspondiente al valor de 'Sex' de esa fila y 0 en todas las demás columnas.

5. **Codificación Ordinal para la característica 'Embarked':** Similar a la característica 'Sex', la característica 'Embarked' es categórica y necesita ser convertida a un formato numérico. Sin embargo, en lugar de la codificación one-hot, usamos la codificación ordinal para 'Embarked'. Esto asigna un número entero único a cada valor único en la característica 'Embarked'. Elegimos la codificación ordinal en lugar de la one-hot porque 'Embarked' tiene 3 valores únicos, y la codificación ordinal resultará en una única columna de datos numéricos en lugar de múltiples columnas en la codificación one-hot. Esto puede ayudar a mantener el tamaño del conjunto de datos manejable.


Ahora podemos seguir practicando con el conjunuto de datos de House Prices.
[Ver Actividad](test)