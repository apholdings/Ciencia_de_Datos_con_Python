# Titanic - Machine Learning From Disaster

## Actividad - Implementación de modelos básicos de aprendizaje automático en un conjunto de datos.

Primero, importamos las librerías necesarias y cargamos los datos:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Cargamos el conjunto de datos
df = pd.read_csv('train.csv')

# Mostramos las primeras 5 filas del conjunto de datos
print(df.head())
```

A continuación, realizamos algunas operaciones de preprocesamiento de datos. En este caso, vamos a eliminar las columnas que no vamos a utilizar, a tratar los datos faltantes y a codificar las variables categóricas:

```python
# Eliminamos las columnas que no vamos a utilizar
df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)

# Tratamos los datos faltantes
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Codificamos las variables categóricas
df = pd.get_dummies(df, drop_first=True)
```

Después de eso, dividimos los datos en un conjunto de entrenamiento y un conjunto de prueba:

```python
# Definimos la variable objetivo y las variables predictoras
X = df.drop('Survived', axis=1)
y = df['Survived']

# Dividimos los datos en un conjunto de entrenamiento y un conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

Ahora estamos listos para entrenar nuestro modelo. En este caso, vamos a utilizar la regresión logística:

```python
# Creamos el modelo
model = LogisticRegression(max_iter=1000)

# Entrenamos el modelo
model.fit(X_train, y_train)
```

Finalmente, evaluamos la precisión del modelo en el conjunto de prueba:

```python
# Hacemos predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluamos la precisión del modelo
print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

Ahora podemos seguir practicando con el conjunuto de datos de House Prices.
[Ver Actividad](https://github.com/apholdings/Ciencia_de_Datos_con_Python/blob/main/9%29%20Introduccion%20a%20Aprendizaje%20Automatico/House%20Prices%20-%20Advanced%20Regression%20Techniques/README.md)