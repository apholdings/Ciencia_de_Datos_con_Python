# 12) Aprendizaje Supervisado
El aprendizaje supervisado es uno de los paradigmas más importantes en el campo del aprendizaje automático. En este enfoque, un modelo es entrenado utilizando datos etiquetados, lo que significa que cada ejemplo en el conjunto de datos de entrenamiento incluye tanto las características de entrada como el resultado deseado.

## Conceptos Fundamentales del Aprendizaje Supervisado
#### 1. Etiquetas y Características
* **Etiquetas (Targets)**: Son los resultados deseados que el modelo intenta predecir. Pueden ser categorías (para clasificación) o valores continuos (para regresión).
* **Características (Features)**: Son las variables de entrada que se utilizan para hacer las predicciones.
#### 2. Clasificación vs. Regresión
* **Clasificación**: Tareas en las que el objetivo es asignar una etiqueta discreta a cada ejemplo de entrada. Ejemplos incluyen la detección de spam, el reconocimiento de imágenes, etc.
* **Regresión**: Tareas en las que el objetivo es predecir un valor continuo. Ejemplos incluyen la predicción de precios de viviendas, la previsión de ventas, etc.
#### 3. Conjunto de Datos
* **Entrenamiento**: Subconjunto de datos utilizado para entrenar el modelo.
* **Validación**: Subconjunto de datos utilizado para ajustar hiperparámetros del modelo y prevenir sobreajuste.
* **Prueba**: Subconjunto de datos utilizado para evaluar el rendimiento final del modelo.
#### 4. Modelo
* Un algoritmo que aprende a mapear entradas a salidas basándose en los datos de entrenamiento.
#### 5. Función de Pérdida
* Mide la discrepancia entre las predicciones del modelo y las etiquetas reales. El objetivo del entrenamiento es minimizar esta función.
#### 6. Hiperparámetros
* Parámetros que se establecen antes del entrenamiento del modelo y que afectan su rendimiento. Ejemplos incluyen la tasa de aprendizaje, la profundidad del árbol de decisión, etc.

## Algoritmos Comunes de Aprendizaje Supervisado

#### 1. Regresión Lineal
* Se utiliza para predecir un valor continuo. Asume una relación lineal entre las características de entrada y la etiqueta.

``` python
from sklearn.linear_model import LinearRegression

# Crear un modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Hacer predicciones
predictions = model.predict(X_test)
```

#### 2. Regresión Logística
* Se utiliza para clasificación binaria. Predice la probabilidad de que una instancia pertenezca a una clase particular.

``` python
from sklearn.linear_model import LogisticRegression

# Crear un modelo de regresión logística
model = LogisticRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Hacer predicciones
predictions = model.predict(X_test)
```

#### 3. Árboles de Decisión
* Se utilizan tanto para clasificación como para regresión. Dividen el espacio de características en subespacios más simples.

``` python
from sklearn.tree import DecisionTreeClassifier

# Crear un modelo de árbol de decisión
model = DecisionTreeClassifier()

# Entrenar el modelo
model.fit(X_train, y_train)

# Hacer predicciones
predictions = model.predict(X_test)
```

#### 4. Bosques Aleatorios (Random Forests)
* Un conjunto de árboles de decisión que mejora la precisión y reduce el sobreajuste.

``` python
from sklearn.ensemble import RandomForestClassifier

# Crear un modelo de bosque aleatorio
model = RandomForestClassifier()

# Entrenar el modelo
model.fit(X_train, y_train)

# Hacer predicciones
predictions = model.predict(X_test)
```

#### 5. Support Vector Machines (SVM)
* Se utilizan para clasificación y regresión. Encuentran el hiperplano que mejor separa las clases en el espacio de características.

``` python
from sklearn.svm import SVC

# Crear un modelo SVM
model = SVC()

# Entrenar el modelo
model.fit(X_train, y_train)

# Hacer predicciones
predictions = model.predict(X_test)
```

#### 6. K-Nearest Neighbors (KNN)
* Asigna etiquetas basándose en las etiquetas de los vecinos más cercanos en el espacio de características.

``` python
from sklearn.neighbors import KNeighborsClassifier

# Crear un modelo KNN
model = KNeighborsClassifier()

# Entrenar el modelo
model.fit(X_train, y_train)

# Hacer predicciones
predictions = model.predict(X_test)
```

### Proceso de Evaluación y Validación

#### 1. División de los Datos
* Utilizamos `train_test_split` para dividir los datos en conjuntos de entrenamiento y prueba.

``` python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

#### 2. Validación Cruzada
* Técnica para evaluar la robustez del modelo dividiendo los datos en múltiples subconjuntos y validando el modelo en cada subconjunto.
``` python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)
print(f'Cross-validation scores: {scores}')
```

#### 3. Métricas de Evaluación
* Clasificación: Exactitud, precisión, recall, F1-score, matriz de confusión.
* Regresión: Error cuadrático medio (MSE), error absoluto medio (MAE), coeficiente de determinación (R^2).

``` python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_squared_error, r2_score

# Para clasificación
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, average='macro')
recall = recall_score(y_test, predictions, average='macro')
f1 = f1_score(y_test, predictions, average='macro')

# Para regresión
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
print(f'MSE: {mse}')
print(f'R^2: {r2}')
```

### Consideraciones Adicionales
#### 1. Preprocesamiento Avanzado
* **Imputación**: Rellenar valores faltantes.
* **Escalado**: Normalización o estandarización de características.
* **Codificación de Variables Categóricas**: One-hot encoding.
#### 2. Selección de Características
* Técnicas como eliminación de características con baja varianza, selección de características basada en modelos y selección secuencial hacia adelante.
#### 3. Ajuste de Hiperparámetros
* Utilizar técnicas como Grid Search o Random Search para encontrar los mejores hiperparámetros del modelo.
```python
from sklearn.model_selection import GridSearchCV

# Definir el espacio de búsqueda de hiperparámetros
param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}

# Crear el objeto GridSearchCV
grid_search = GridSearchCV(SVC(), param_grid, cv=5)

# Entrenar el modelo
grid_search.fit(X_train, y_train)

# Mejor hiperparámetro
print(f'Mejor hiperparámetro: {grid_search.best_params_}')
```

### Ejemplo Completo: Clasificación con el Conjunto de Datos Iris
``` python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# Cargar los datos
data = load_iris()
X, y = data.data, data.target

# Preprocesar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir los datos
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Seleccionar y entrenar el modelo
model = LogisticRegression()
model.fit(X_train, y_train)

# Hacer predicciones
predictions = model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, average='macro')
recall = recall_score(y_test, predictions, average='macro')
f1 = f1_score(y_test, predictions, average='macro')

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
print(f'Confusion Matrix:\n{confusion_matrix(y_test, predictions)}')
print(f'Classification Report:\n{classification_report(y_test, predictions)}')

# Validación cruzada
scores = cross_val_score(model, X, y, cv=5)
print(f'Cross-validation scores: {scores}')

# Ajuste de hiperparámetros
param_grid = {'C': [0.1, 1, 10], 'solver': ['liblinear', 'saga']}
grid_search = GridSearchCV(LogisticRegression(), param_grid, cv=5)
grid_search.fit(X_train, y_train)
print(f'Mejor hiperparámetro: {grid_search.best_params_}')
```
