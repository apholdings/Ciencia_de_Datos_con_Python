# 15) Seleccion de Modelos e Hiperparametros
La selección de modelos e hiperparámetros es un aspecto crucial en el proceso de desarrollo de modelos de aprendizaje automático. La elección del modelo correcto y el ajuste adecuado de los hiperparámetros pueden tener un impacto significativo en el rendimiento del modelo y su capacidad para generalizar bien en datos no vistos.

#### 1. Selección de Modelos
La selección de modelos implica elegir el algoritmo de aprendizaje adecuado para una tarea específica. Dado que no existe un modelo universalmente mejor para todas las tareas, la selección de modelos depende de factores como la naturaleza del problema, el tamaño del conjunto de datos, la complejidad de los datos y las necesidades específicas del proyecto.

##### a) Tipos Comunes de Modelos
* **Regresión Lineal y Logística**: Usados para problemas de regresión y clasificación binaria, respectivamente.
* **Árboles de Decisión**: Modelos interpretables que funcionan bien con datos heterogéneos y no requieren escalado.
* **Máquinas de Soporte Vectorial (SVM)**: Eficaces en espacios de alta dimensionalidad, pero requieren ajuste de hiperparámetros.
* **Bosques Aleatorios (Random Forests)**: Conjuntos de árboles de decisión que mejoran la precisión y reducen el sobreajuste.
* **Redes Neuronales**: Modelos potentes para tareas complejas como el reconocimiento de imágenes y el procesamiento del lenguaje natural.
* **K-Nearest Neighbors (KNN)**: Modelo simple que clasifica basado en la distancia a los puntos de datos más cercanos.

##### b) Consideraciones para la Selección de Modelos
* **Naturaleza del Problema**: Determinar si es un problema de clasificación, regresión, clustering, etc.
* **Tamaño del Conjunto de Datos**: Algunos modelos funcionan mejor con grandes volúmenes de datos, mientras que otros pueden manejar bien conjuntos de datos más pequeños.
* **Tiempo y Recursos Computacionales**: Modelos más complejos como las redes neuronales profundas pueden requerir más tiempo y potencia computacional.
* **Interpretabilidad**: Modelos como árboles de decisión y regresión lineal son más fáciles de interpretar, lo que puede ser importante en ciertos contextos.

#### 2. Ajuste de Hiperparámetros
Los hiperparámetros son parámetros que se configuran antes de entrenar el modelo y no se aprenden de los datos. El ajuste adecuado de los hiperparámetros es fundamental para mejorar el rendimiento del modelo y evitar problemas como el sobreajuste o el infraajuste.

##### a) Hiperparámetros Comunes
* **Tasa de Aprendizaje (Learning Rate)**: Controla el tamaño de los pasos que da el modelo durante el entrenamiento. Es crucial en modelos de redes neuronales y SVM.
* **Número de Árboles en Random Forests**: Afecta la precisión y el tiempo de entrenamiento. Más árboles generalmente mejoran la precisión pero aumentan el tiempo de cómputo.
* **Profundidad Máxima de los Árboles**: Limita la profundidad de los árboles de decisión para controlar el sobreajuste.
* **Regularización (L1, L2)**: Añade un término de penalización para evitar que el modelo se ajuste demasiado a los datos de entrenamiento.
* **Número de Vecinos en KNN**: Afecta la suavidad de la frontera de decisión. Menos vecinos pueden hacer que el modelo sea más sensible al ruido.

##### b) Métodos de Búsqueda de Hiperparámetros
* **Grid Search (Búsqueda en Cuadrícula)**: Explora un conjunto predefinido de hiperparámetros, evaluando todas las combinaciones posibles.
* **Random Search (Búsqueda Aleatoria)**: Muestra aleatoriamente combinaciones de hiperparámetros de un espacio predefinido. Es más eficiente en casos con un gran número de hiperparámetros.
* **Bayesian Optimization**: Un enfoque más avanzado que construye un modelo probabilístico del rendimiento del modelo en función de los hiperparámetros y elige nuevas combinaciones basadas en este modelo.

##### c) Validación Cruzada
* **Cross-Validation**: Técnica utilizada para evaluar el rendimiento del modelo al dividir los datos en múltiples subconjuntos (folds) y entrenar el modelo en diferentes combinaciones de estos subconjuntos. Esto proporciona una estimación más robusta del rendimiento del modelo y ayuda a seleccionar los mejores hiperparámetros.

#### 3. Implementación Práctica con Scikit-learn
A continuación, se presenta un ejemplo de cómo seleccionar un modelo y ajustar sus hiperparámetros utilizando Scikit-learn.

##### Ejemplo: Selección de Modelos e Hiperparámetros en el Conjunto de Datos Iris
``` python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris
data = load_iris()
X = data.data
y = data.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Ejemplo 1: Grid Search con Random Forest
param_grid_rf = {
    'n_estimators': [10, 50, 100],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

rf_model = RandomForestClassifier(random_state=42)
grid_search_rf = GridSearchCV(estimator=rf_model, param_grid=param_grid_rf, cv=5, n_jobs=-1, verbose=2)
grid_search_rf.fit(X_train, y_train)

# Mejor modelo y sus parámetros
print(f"Best parameters (Random Forest): {grid_search_rf.best_params_}")
print(f"Best accuracy (Random Forest): {grid_search_rf.best_score_}")

# Evaluación en el conjunto de prueba
y_pred_rf = grid_search_rf.best_estimator_.predict(X_test)
print(f"Test accuracy (Random Forest): {accuracy_score(y_test, y_pred_rf)}")

# Ejemplo 2: Random Search con SVM
param_dist_svc = {
    'C': [0.1, 1, 10, 100],
    'gamma': [0.001, 0.01, 0.1, 1],
    'kernel': ['rbf', 'linear']
}

svc_model = SVC(random_state=42)
random_search_svc = RandomizedSearchCV(estimator=svc_model, param_distributions=param_dist_svc, n_iter=10, cv=5, random_state=42, n_jobs=-1, verbose=2)
random_search_svc.fit(X_train, y_train)

# Mejor modelo y sus parámetros
print(f"Best parameters (SVM): {random_search_svc.best_params_}")
print(f"Best accuracy (SVM): {random_search_svc.best_score_}")

# Evaluación en el conjunto de prueba
y_pred_svc = random_search_svc.best_estimator_.predict(X_test)
print(f"Test accuracy (SVM): {accuracy_score(y_test, y_pred_svc)}")
```

La selección de modelos e hiperparámetros es una parte fundamental del desarrollo de modelos de aprendizaje automático. Elegir el modelo correcto y optimizar sus hiperparámetros puede mejorar significativamente el rendimiento del modelo y su capacidad de generalización. Las herramientas como Grid Search y Random Search en combinación con la validación cruzada son estrategias eficaces para encontrar los mejores hiperparámetros. Es esencial experimentar con diferentes modelos y técnicas para encontrar la mejor solución para un problema específico.