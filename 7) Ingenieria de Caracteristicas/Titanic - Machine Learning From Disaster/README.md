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

### Discutir el Impacto en un Modelo Simple
Para continuar con la actividad, podríamos entrenar un modelo de aprendizaje automático sencillo (como una regresión logística) en nuestros datos transformados y ver cómo se desempeña.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Eliminar las columnas que no vamos a usar
df_train = df_train.drop(['Name', 'Ticket', 'Cabin'], axis=1)

# Tratamiento de los valores faltantes en 'Age'
df_train['Age'].fillna(df_train['Age'].median(), inplace=True)

# Definir las características y la variable objetivo
X = df_train.drop('Survived', axis=1)
y = df_train['Survived']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un modelo de regresión logística
model = LogisticRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Predecir los resultados para el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy: ", accuracy)
```
Este código entrena un modelo de regresión logística en los datos de entrenamiento y luego lo evalúa en los datos de prueba, imprimiendo la precisión del modelo. En este caso, la precisión es la fracción de las predicciones que el modelo hace correctamente.

La regresión logística es un buen modelo para comenzar porque es simple y rápido de entrenar. Sin embargo, puede que no sea el mejor modelo para este conjunto de datos. Una vez que hayas completado la ingeniería de características y el preprocesamiento de los datos, te animo a que pruebes diferentes modelos y veas cuál funciona mejor.

Es importante destacar que la ingeniería de características y la selección del modelo son procesos iterativos. Puede que encuentres que ciertas características funcionan bien con un modelo pero no con otro. O puede que encuentres que ciertas características que creaste no son útiles en absoluto. La clave es experimentar y aprender de cada iteración.

Ahora podemos seguir practicando con el conjunuto de datos de House Prices.
[Ver Actividad](https://github.com/apholdings/Ciencia_de_Datos_con_Python/tree/main/7%29%20Ingenieria%20de%20Caracteristicas/House%20Prices%20-%20Advanced%20Regression%20Techniques)