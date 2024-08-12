# Titanic - Machine Learning From Disaster

## Actividad - Implementación de metricas de evaluacion en conjunto de datos.

### Objetivo
El objetivo de esta actividad es implementar y comparar varias métricas de evaluación en un problema de clasificación binaria utilizando el conjunto de datos "Titanic: Machine Learning from Disaster". Evaluaremos un modelo de clasificación (regresión logística) y analizaremos su rendimiento utilizando métricas como la **Exactitud (Accuracy)**, **Precisión (Precision)**, **Recall**, **F1-Score**, y el **Área Bajo la Curva ROC (AUC-ROC)**.

#### Paso 1: Cargar y Preprocesar los Datos
Primero, cargaremos el conjunto de datos y realizaremos un preprocesamiento básico para preparar los datos para el análisis.

``` python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Cargar los datos de entrenamiento
data = pd.read_csv('train.csv')

# Convertir 'Sex' en valores numéricos (0: male, 1: female)
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# Rellenar valores nulos en la columna 'Age' con la mediana
data['Age'].fillna(data['Age'].median(), inplace=True)

# Rellenar valores nulos en 'Embarked' con el valor más frecuente
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)

# Crear una nueva característica 'FamilySize'
data['FamilySize'] = data['SibSp'] + data['Parch'] + 1

# Convertir 'Embarked' en variables dummy
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Seleccionar características relevantes
features = ['Pclass', 'Sex', 'Age', 'Fare', 'FamilySize', 'Embarked_Q', 'Embarked_S']
X = data[features]
y = data['Survived']

# Escalar las características numéricas
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

#### Paso 2: Dividir los Datos en Conjuntos de Entrenamiento y Prueba
Dividiremos los datos en conjuntos de entrenamiento y prueba para evaluar el rendimiento del modelo.

``` python
from sklearn.model_selection import train_test_split

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
```

#### Paso 3: Entrenar un Modelo de Clasificación
A continuación, entrenaremos un modelo de regresión logística con los datos de entrenamiento.

``` python
from sklearn.linear_model import LogisticRegression

# Crear el modelo de regresión logística
model = LogisticRegression(max_iter=200)

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)
```

#### Paso 4: Hacer Predicciones
Con el modelo entrenado, realizaremos predicciones sobre el conjunto de prueba.

``` python
# Hacer predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Obtener las probabilidades predichas para calcular AUC-ROC
y_prob = model.predict_proba(X_test)[:, 1]
```

#### Paso 5: Implementar Métricas de Evaluación
Evaluaremos el rendimiento del modelo utilizando varias métricas de evaluación para clasificación:

1. **Exactitud (Accuracy)**: Proporción de predicciones correctas entre el total de predicciones realizadas.
2. **Precisión (Precision)**: Proporción de verdaderos positivos entre todos los ejemplos que fueron clasificados como positivos.
3. **Recall**: Proporción de verdaderos positivos entre todos los ejemplos que son realmente positivos.
4. **F1-Score**: Media armónica de la precisión y el recall.
5. **Área Bajo la Curva ROC (AUC-ROC)**: Mide la capacidad del modelo para distinguir entre las clases.

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, classification_report

# Calcular la Exactitud
accuracy = accuracy_score(y_test, y_pred)

# Calcular la Precisión
precision = precision_score(y_test, y_pred)

# Calcular el Recall
recall = recall_score(y_test, y_pred)

# Calcular el F1-Score
f1 = f1_score(y_test, y_pred)

# Calcular el AUC-ROC
roc_auc = roc_auc_score(y_test, y_prob)

# Mostrar la matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)

# Generar un reporte de clasificación
class_report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
print(f'ROC AUC Score: {roc_auc}')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{class_report}')
```

#### Paso 6: Interpretación de los Resultados
* **Exactitud (Accuracy)**: Proporción de predicciones correctas sobre el total de predicciones realizadas.

* **Precisión (Precision)**: Proporción de verdaderos positivos entre todos los positivos predichos. Es crucial cuando el costo de una falsa alarma (falsos positivos) es alto.

* **Recall**: Proporción de verdaderos positivos entre todos los positivos reales. Es importante cuando es crítico capturar todos los positivos, incluso si se generan algunos falsos positivos.

* **F1-Score**: Media armónica de la precisión y el recall. Es útil en situaciones de clases desbalanceadas donde ambos, precisión y recall, son importantes.

* **AUC-ROC**: Mide la capacidad del modelo para distinguir entre clases. Un valor de AUC cercano a 1 indica un buen rendimiento del modelo.

### Ejemplo Completo
Aquí tienes el código completo desde la carga de los datos hasta la evaluación del modelo:

``` python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, classification_report

# Cargar los datos de entrenamiento
data = pd.read_csv('train.csv')

# Preprocesamiento de los datos
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Seleccionar características relevantes
features = ['Pclass', 'Sex', 'Age', 'Fare', 'FamilySize', 'Embarked_Q', 'Embarked_S']
X = data[features]
y = data['Survived']

# Escalar las características numéricas
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión logística
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# Calcular y mostrar las métricas de evaluación
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_prob)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
print(f'ROC AUC Score: {roc_auc}')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{class_report}')
```

En esta actividad, hemos implementado y comparado varias métricas de evaluación utilizando un modelo de regresión logística en el conjunto de datos "Titanic: Machine Learning from Disaster". Las métricas como la Exactitud, Precisión, Recall, F1-Score y AUC-ROC nos proporcionan una comprensión más profunda del rendimiento del modelo, permitiéndonos medir su capacidad para clasificar correctamente a los pasajeros en función de si sobrevivieron o no. Estas métricas son esenciales para evaluar y mejorar modelos de aprendizaje automático en problemas de clasificación. ¡Continúa explorando y experimentando para dominar estas técnicas!