# 10) Sobreajuste e infraajuste
El sobreajuste (overfitting) y el infraajuste (underfitting) son problemas comunes en el aprendizaje automático que ocurren cuando un modelo no se generaliza bien a partir de los datos de entrenamiento a los datos no vistos.

## Sobreajuste
El sobreajuste ocurre cuando un modelo aprende los detalles y el ruido en los datos de entrenamiento hasta el punto de que se desempeña mal en los datos no vistos. En otras palabras, el modelo se ajusta demasiado bien a los datos de entrenamiento. Un modelo sobreajustado tiene una alta varianza y bajo sesgo. Es como estudiar para un examen recordando cada pregunta y respuesta de un examen de práctica, pero luego fallar en el examen real porque las preguntas no son exactamente las mismas.

### Técnicas para Prevenir el Sobreajuste

1. **Validación Cruzada:**
    * Divide los datos en múltiples subconjuntos.
    * Entrena el modelo en algunos subconjuntos y valida en los restantes.
    * Esto asegura que el modelo sea validado en diferentes porciones de los datos, reduciendo el riesgo de sobreajuste.

2. **Regularización:**
    * Penaliza la complejidad del modelo.
    * Técnicas como L1 (Lasso) y L2 (Ridge) regularización añaden un término de penalización a la función de costo del modelo, evitando que los coeficientes se vuelvan demasiado grandes.

3. **Parada Temprana (Early Stopping):**
    * Monitorea el rendimiento del modelo en un conjunto de validación durante el entrenamiento.
    * Detiene el entrenamiento cuando el rendimiento en el conjunto de validación comienza a deteriorarse.

4. **Poda (Pruning):**
    * En algoritmos basados en árboles, la poda elimina ramas que tienen poca importancia en la predicción, reduciendo la complejidad del modelo.

5. **Aumento de Datos (Data Augmentation):**
    * Genera más datos de entrenamiento mediante técnicas como rotaciones, traslaciones, y escalados en imágenes, o mediante la creación de variaciones sintéticas en otros tipos de datos.

6. **Dropout:**
    * En redes neuronales, el dropout desconecta aleatoriamente neuronas durante el entrenamiento, lo que ayuda a evitar que el modelo se vuelva demasiado dependiente de ciertas neuronas.

## **Ejemplo de Sobreajuste en el Conjunto de Datos del Titanic**
Supongamos que estamos construyendo un modelo de clasificación para predecir la supervivencia de los pasajeros del Titanic. Si entrenamos un modelo muy complejo, como un árbol de decisión sin restricciones, es probable que se ajuste demasiado bien a los datos de entrenamiento, capturando detalles específicos como nombres de pasajeros o números de boletos que no son generalizables a otros pasajeros.

*Para ilustrar esto con código en Python usando scikit-learn:*
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

## Infraajuste
El infraajuste ocurre cuando un modelo es demasiado simple para capturar los patrones subyacentes en los datos de entrenamiento. Esto resulta en un mal desempeño tanto en los datos de entrenamiento como en los datos no vistos. Un modelo infraajustado tiene un sesgo alto y una varianza baja. Es como estudiar para un examen solo entendiendo el concepto principal y fallar porque no puedes responder a las preguntas detalladas.

### Causas del Infraajuste
1. **Modelo Demasiado Simple:** Modelos con pocos parámetros o baja capacidad (como regresiones lineales simples) pueden no ser capaces de captar la complejidad de los datos.

2. **Demasiada Regularización:** Aplicar una regularización excesiva puede restringir demasiado al modelo, impidiéndole aprender los patrones importantes.

3. **Insuficientes Características:** No incluir suficientes variables o características relevantes en el modelo puede llevar a un infraajuste.

### Técnicas para Prevenir el Infraajuste
1. **Añadir Más Características:**
    * Incluir más variables relevantes en el modelo.
    * Realizar ingeniería de características para crear nuevas variables que puedan ayudar a capturar mejor los patrones en los datos.

2. **Aumentar la Complejidad del Modelo:**
    * Utilizar modelos más complejos como árboles de decisión más profundos, modelos de ensamble (bosques aleatorios, boosting) o redes neuronales con más capas.

3. **Reducir la Regularización:**
    * Disminuir los parámetros de regularización (como los coeficientes de L1 o L2) para permitir que el modelo se ajuste mejor a los datos de entrenamiento.

4. **Aumentar las Iteraciones de Entrenamiento:**
    * Entrenar el modelo durante más iteraciones para permitirle aprender mejor los patrones de los datos (aplicable en modelos iterativos como redes neuronales).

## **Ejemplo de Infraajuste en el Conjunto de Datos del Titanic**
Supongamos que estamos construyendo un modelo de clasificación para predecir la supervivencia de los pasajeros del Titanic. Si entrenamos un modelo muy simple, como una regresión logística con pocas características, es probable que no capture adecuadamente los patrones subyacentes y resulte en infraajuste.

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