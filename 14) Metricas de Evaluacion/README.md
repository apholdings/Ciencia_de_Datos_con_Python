# 14) Metricas de Evaluacion
Las métricas de evaluación son herramientas cruciales en el aprendizaje automático que nos permiten medir el rendimiento de un modelo y su capacidad para generalizar a datos no vistos. La elección de la métrica adecuada depende del tipo de problema que estamos resolviendo, ya sea clasificación, regresión, clustering u otros. Aquí, exploraremos algunas de las métricas más comunes para problemas de clasificación y regresión, y luego proporcionaremos un ejemplo práctico usando Scikit-learn.

### 1. Métricas para Problemas de Clasificación

##### a) Exactitud (Accuracy)
* Es la proporción de predicciones correctas entre el total de predicciones realizadas.
* Se usa comúnmente en problemas de clasificación binaria o multiclase.
* **Fórmula**: *`Exactitud = Numero de predicciones correctas / Total de predicciones`*

##### b) Matriz de Confusión
* Es una tabla que se utiliza para describir el rendimiento de un modelo de clasificación.
* Muestra las verdaderas positivas, falsas positivas, verdaderas negativas y falsas negativas.

|                | Predicción Positiva | Predicción Negativa |
| -------------- | ------------------- | ------------------- |
| Clase Positiva | Verdadero Positivo  | Falso Negativo      |
| Clase Negativa | Falso Positivo      | Verdadero Negativo  |

##### c) Precisión (Precision)
* Es la proporción de verdaderos positivos entre todos los ejemplos que fueron clasificados como positivos.
* Es útil cuando el costo de una falsa alarma (falsos positivos) es alto.
* **Fórmula**: *`Precision = Verdaderos positivos / (Verdaderos Positivos + Falsos positivos)`*

##### d) Recall (Sensibilidad o Tasa de Verdaderos Positivos)
* Es la proporción de verdaderos positivos entre todos los ejemplos que son realmente positivos.
* Es útil cuando es importante capturar todos los positivos, incluso si se generan algunos falsos positivos.
* **Fórmula**: *`Recall = Verdaderos positivos / Verdadores positivos + Falsos positivos`*

##### e) F1-Score
* Es la media armónica de la precisión y el recall.
* Es útil en situaciones de clases desbalanceadas donde ambos, precisión y recall, son importantes.
* **Fórmula**: *`F1 = 2 * (Precision * Recall) / (Precision + Recall)`*

##### f) Área Bajo la Curva ROC (AUC-ROC)
* ROC es una curva que muestra la relación entre el recall y la tasa de falsos positivos.
* El AUC mide el área bajo esta curva y proporciona una medida de la capacidad del modelo para distinguir entre clases.

### 2. Métricas para Problemas de Regresión

##### a) Error Cuadrático Medio (MSE)
* Es la media de los cuadrados de los errores, es decir, la diferencia entre los valores predichos y los valores reales.
* Penaliza fuertemente los errores grandes.
* **Fórmula:** \( MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 \)

##### b) Error Absoluto Medio (MAE)
* Es la media de los valores absolutos de los errores.
* Es más robusto ante valores atípicos en comparación con el MSE.
* **Fórmula:** \( MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| \)

##### c) Coeficiente de Determinación (R^2)
* Mide qué tan bien las predicciones del modelo se ajustan a los valores reales.
* Un valor de R^2 cercano a 1 indica un buen ajuste.
* **Fórmula:** \( R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} \)

### Ejemplo Práctico con Scikit-learn
Vamos a aplicar algunas de estas métricas de evaluación en un problema de clasificación utilizando el conjunto de datos Iris y en un problema de regresión utilizando el conjunto de datos de precios de viviendas (Boston Housing).

#### 1. Problema de Clasificación: Iris Dataset
``` python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score

# Cargar los datos de Iris
data = load_iris()
X = data.data
y = data.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entrenar un modelo de regresión logística
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Hacer predicciones
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]  # Probabilidad para AUC-ROC

# Calcular y mostrar las métricas
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')
conf_matrix = confusion_matrix(y_test, y_pred)
roc_auc = roc_auc_score(y_test, model.predict_proba(X_test), multi_class="ovr")

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'ROC AUC Score: {roc_auc}')
```

#### 2. Problema de Regresión: Boston Housing Dataset
``` python
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Cargar los datos de Boston Housing
boston = load_boston()
X = boston.data
y = boston.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entrenar un modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Hacer predicciones
y_pred = model.predict(X_test)

# Calcular y mostrar las métricas
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error (MSE): {mse}')
print(f'Mean Absolute Error (MAE): {mae}')
print(f'R^2 Score: {r2}')
```

Las métricas de evaluación son fundamentales para medir el rendimiento de los modelos de aprendizaje automático y para compararlos entre sí. La elección de la métrica correcta depende del tipo de problema que estás abordando y de la importancia relativa de diferentes tipos de errores (como falsos positivos frente a falsos negativos en clasificación). Usando Scikit-learn, podemos implementar fácilmente estas métricas y obtener una comprensión más profunda del rendimiento de nuestros modelos.





