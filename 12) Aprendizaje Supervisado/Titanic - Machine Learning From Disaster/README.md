# Titanic - Machine Learning From Disaster

## Actividad - Implementación de aprendizaje supervisado en conjunto de datos.

### Objetivo
El objetivo de esta actividad es predecir si un pasajero sobrevivió o no al desastre del Titanic `(Survived)`, utilizando diversas características de los pasajeros disponibles en el conjunto de datos. Aplicaremos un modelo de aprendizaje supervisado (regresión logística) para realizar estas predicciones.

#### Paso 1: Cargar y Examinar los Datos
Primero, cargaremos el conjunto de datos y realizaremos una exploración inicial para entender su estructura y contenido.

``` python
import pandas as pd

# Cargar los datos de entrenamiento
train_data = pd.read_csv('train.csv')

# Mostrar las primeras filas del conjunto de datos
print(train_data.head())

# Verificar la estructura del conjunto de datos
print(train_data.info())

# Descripción estadística del conjunto de datos
print(train_data.describe())
```

#### Paso 2: Preprocesamiento de los Datos
El preprocesamiento de datos incluye la gestión de valores nulos, la codificación de variables categóricas y la normalización de los datos. Para este conjunto de datos, también podemos crear nuevas características, como el tamaño de la familia, combinando algunas de las variables existentes.

``` python
import numpy as np
from sklearn.preprocessing import StandardScaler

# Rellenar valores nulos en la columna 'Age' con la mediana
train_data['Age'].fillna(train_data['Age'].median(), inplace=True)

# Rellenar valores nulos en 'Embarked' con el valor más frecuente
train_data['Embarked'].fillna(train_data['Embarked'].mode()[0], inplace=True)

# Convertir la columna 'Sex' en valores numéricos (0: male, 1: female)
train_data['Sex'] = train_data['Sex'].map({'male': 0, 'female': 1})

# Crear una nueva característica 'FamilySize'
train_data['FamilySize'] = train_data['SibSp'] + train_data['Parch'] + 1

# Convertir 'Embarked' en variables dummy
train_data = pd.get_dummies(train_data, columns=['Embarked'], drop_first=True)

# Seleccionar características relevantes
features = ['Pclass', 'Sex', 'Age', 'Fare', 'FamilySize', 'Embarked_Q', 'Embarked_S']
X = train_data[features]
y = train_data['Survived']

# Escalar las características numéricas
scaler = StandardScaler()
X = scaler.fit_transform(X)
```

#### Paso 3: Dividir los Datos en Conjuntos de Entrenamiento y Prueba
Dividiremos los datos en un conjunto de entrenamiento y un conjunto de prueba para evaluar el rendimiento del modelo.

``` python
from sklearn.model_selection import train_test_split

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

#### Paso 4: Seleccionar y Entrenar el Modelo
Utilizaremos un modelo de regresión logística, que es un modelo supervisado comúnmente utilizado para problemas de clasificación binaria como este.

``` python
from sklearn.linear_model import LogisticRegression

# Crear el modelo de regresión logística
model = LogisticRegression()

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)
```

#### Paso 5: Hacer Predicciones
Con el modelo entrenado, realizaremos predicciones sobre el conjunto de prueba.

``` python
# Hacer predicciones en el conjunto de prueba
predictions = model.predict(X_test)
```

#### Paso 6: Evaluar el Modelo
Evaluaremos el rendimiento del modelo utilizando métricas de evaluación como la exactitud, precisión, recall, y F1-score, que son especialmente útiles en problemas de clasificación.

``` python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# Calcular la exactitud
accuracy = accuracy_score(y_test, predictions)

# Calcular la precisión
precision = precision_score(y_test, predictions)

# Calcular el recall
recall = recall_score(y_test, predictions)

# Calcular el F1-score
f1 = f1_score(y_test, predictions)

# Matriz de confusión y reporte de clasificación
conf_matrix = confusion_matrix(y_test, predictions)
class_report = classification_report(y_test, predictions)

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{class_report}')
```

#### Paso 7: Interpretar los Resultados
Al ejecutar este código, obtendrás varias métricas que indican el rendimiento de tu modelo:

* **Exactitud (Accuracy)**: Proporción de predicciones correctas.
* **Precisión (Precision)**: Proporción de verdaderos positivos sobre todos los positivos predichos.
* **Recall**: Proporción de verdaderos positivos sobre todos los positivos reales.
* **F1 Score**: Media armónica de la precisión y el recall, útil en casos de clases desbalanceadas.
* **Matriz de Confusión**: Muestra el número de verdaderos positivos, falsos positivos, verdaderos negativos y falsos negativos.

#### Paso 8: Mejorar el Modelo (Opcional)
Para mejorar el rendimiento del modelo, puedes considerar:

* **Agregar o crear nuevas características** que puedan ser relevantes para predecir la supervivencia.
* **Probar otros modelos** como Random Forest, Support Vector Machines, o Gradient Boosting.
* **Ajuste de hiperparámetros** utilizando Grid Search o Random Search.
* **Implementar técnicas de ensamble** como bagging o boosting para combinar múltiples modelos.

##### Ejemplo Completo
Aquí tienes el código completo desde la carga de los datos hasta la evaluación del modelo:

``` python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# Cargar los datos de entrenamiento
train_data = pd.read_csv('train.csv')

# Preprocesamiento de los datos
train_data['Age'].fillna(train_data['Age'].median(), inplace=True)
train_data['Embarked'].fillna(train_data['Embarked'].mode()[0], inplace=True)
train_data['Sex'] = train_data['Sex'].map({'male': 0, 'female': 1})
train_data['FamilySize'] = train_data['SibSp'] + train_data['Parch'] + 1
train_data = pd.get_dummies(train_data, columns=['Embarked'], drop_first=True)

# Seleccionar características relevantes
features = ['Pclass', 'Sex', 'Age', 'Fare', 'FamilySize', 'Embarked_Q', 'Embarked_S']
X = train_data[features]
y = train_data['Survived']

scaler = StandardScaler()
X = scaler.fit_transform(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión logística
model = LogisticRegression()
model.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
predictions = model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)
conf_matrix = confusion_matrix(y_test, predictions)
class_report = classification_report(y_test, predictions)

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{class_report}')
```