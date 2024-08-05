# Titanic - Machine Learning From Disaster

## Actividad - Implementación de sobreajuste e infraajuste en conjunto de datos.

### Sobreajuste
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Cargar los datos del Titanic
data = pd.read_csv('titanic.csv')

# Preprocesamiento simple
data['Age'].fillna(data['Age'].mean(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# Selección de características
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
X = data[features]
y = data['Survived']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un árbol de decisión muy profundo (alta varianza)
model = DecisionTreeClassifier(max_depth=10)
model.fit(X_train, y_train)

# Evaluar el modelo
train_accuracy = accuracy_score(y_train, model.predict(X_train))
test_accuracy = accuracy_score(y_test, model.predict(X_test))

print(f'Exactitud en entrenamiento: {train_accuracy}')
print(f'Exactitud en prueba: {test_accuracy}')
```


### Infraajuste
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Cargar los datos del Titanic
data = pd.read_csv('titanic.csv')

# Preprocesamiento simple
data['Age'].fillna(data['Age'].mean(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# Selección de características limitadas
features = ['Pclass', 'Sex']
X = data[features]
y = data['Survived']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar una regresión logística simple (alta sesgo)
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluar el modelo
train_accuracy = accuracy_score(y_train, model.predict(X_train))
test_accuracy = accuracy_score(y_test, model.predict(X_test))

print(f'Exactitud en entrenamiento: {train_accuracy}')
print(f'Exactitud en prueba: {test_accuracy}')
```

Ahora podemos seguir practicando con el conjunuto de datos de House Prices.
[Ver Actividad](https://github.com/apholdings/Ciencia_de_Datos_con_Python/blob/main/9%29%20Sobreajuste%20e%20infraajste/House%20Prices%20-%20Advanced%20Regression%20Techniques/README.md)