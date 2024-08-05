# 11) Scikit-Learn
Scikit-learn es una biblioteca de Python de código abierto que proporciona herramientas simples y eficientes para el análisis de datos y el aprendizaje automático. Es una de las bibliotecas más populares y ampliamente utilizadas en la comunidad de ciencia de datos.

## Instalación
Para instalar Scikit-learn, puedes usar `pip`:
```bash
pip install scikit-learn
```

## Estructura General de Scikit-learn
Scikit-learn está organizado en varios módulos que contienen algoritmos y herramientas para diferentes tareas de aprendizaje automático. Los módulos principales son:

* ***sklearn.datasets***: Carga y genera conjuntos de datos.
* ***sklearn.preprocessing***: Preprocesa y transforma datos.
* ***sklearn.model_selection***: Selecciona y valida modelos.
* ***sklearn.linear_model***: Modelos lineales.
* ***sklearn.tree***: Árboles de decisión.
* ***sklearn.ensemble***: Métodos de ensamble.
* ***sklearn.cluster***: Algoritmos de clustering.
* ***sklearn.metrics***: Métricas de evaluación de modelos.

## Flujo de Trabajo en Scikit-learn
El flujo de trabajo típico en Scikit-learn incluye:

1. Cargar los datos
2. Preprocesar los datos
3. Dividir los datos en conjuntos de entrenamiento y prueba
4. Seleccionar un modelo
5. Entrenar el modelo
6. Hacer predicciones
7. Evaluar el modelo

## Ejemplo de Uso

### 1. Cargar los Datos
Scikit-learn proporciona algunos conjuntos de datos integrados para practicar, y también puedes cargar tus propios datos desde archivos.
```python
from sklearn.datasets import load_iris
data = load_iris()
X, y = data.data, data.target
```

### 2. Preprocesar los Datos
El preprocesamiento puede incluir la normalización, estandarización, manejo de valores nulos, y conversión de variables categóricas en variables dummy.
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### 3. Dividir los Datos en Conjuntos de Entrenamiento y Prueba
Dividir los datos es crucial para evaluar el rendimiento del modelo.
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

### 4. Seleccionar un Modelo
Scikit-learn proporciona una amplia variedad de modelos. Aquí mostramos un ejemplo con un modelo de regresión logística.
```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
```

### 5. Entrenar el Modelo
Entrenar el modelo implica ajustar los parámetros del modelo a los datos de entrenamiento.
``` python
model.fit(X_train, y_train)
```

### 6. Hacer Predicciones
Después de entrenar el modelo, puedes usarlo para hacer predicciones en los datos de prueba.
```  python
predictions = model.predict(X_test)
```

### 7. Evaluar el Modelo
Evaluar el modelo es esencial para entender su rendimiento. Scikit-learn proporciona varias métricas para diferentes tipos de modelos.
```python
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

accuracy = accuracy_score(y_test, predictions)
conf_matrix = confusion_matrix(y_test, predictions)
class_report = classification_report(y_test, predictions)

print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{class_report}')
```

### Ejemplo Completo
A continuación se muestra un ejemplo completo del flujo de trabajo utilizando el conjunto de datos Iris y un modelo de regresión logística.
``` python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

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
conf_matrix = confusion_matrix(y_test, predictions)
class_report = classification_report(y_test, predictions)

print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{class_report}')
```

## Recursos Adicionales
* [Documentación oficial de Scikit-learn](https://scikit-learn.org/stable/user_guide.html)
* [Kaggle](https://kaggle.com) para conjuntos de datos adicionales y competencias.