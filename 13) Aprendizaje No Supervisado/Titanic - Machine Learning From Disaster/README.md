# Titanic - Machine Learning From Disaster

## Actividad - Implementación de aprendizaje no supervisado en conjunto de datos.

### Objetivo
El objetivo de esta actividad es aplicar técnicas de aprendizaje no supervisado al conjunto de datos "Titanic: Machine Learning from Disaster" de Kaggle para descubrir patrones ocultos en los datos y explorar cómo los pasajeros se agrupan en función de sus características. Utilizaremos el algoritmo de clustering K-Means para agrupar a los pasajeros y PCA para la reducción de dimensionalidad y visualización de los resultados.

#### Paso 1: Cargar y Preprocesar los Datos
Primero, cargaremos el conjunto de datos y realizaremos un preprocesamiento básico para preparar los datos para el análisis.

``` python
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Cargar los datos de entrenamiento
data = pd.read_csv('train.csv')

# Seleccionar algunas características numéricas y categóricas relevantes
features = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex']

# Convertir 'Sex' en valores numéricos (0: male, 1: female)
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# Rellenar valores nulos en la columna 'Age' con la mediana
data['Age'].fillna(data['Age'].median(), inplace=True)

# Seleccionar las características para el clustering
X = data[features]

# Escalar las características numéricas
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

#### Paso 2: Aplicar K-Means para Agrupamiento
Aplicaremos el algoritmo K-Means para agrupar a los pasajeros del Titanic en diferentes clústeres basados en sus características.

``` python
from sklearn.cluster import KMeans

# Definir el modelo K-Means
kmeans = KMeans(n_clusters=3, random_state=42)

# Ajustar el modelo a los datos
kmeans.fit(X_scaled)

# Obtener las etiquetas de clúster predichas
labels = kmeans.labels_

# Añadir las etiquetas al DataFrame original
data['Cluster'] = labels
```

#### Paso 3: Visualizar los Resultados
Podemos visualizar los resultados del clustering para ver cómo se agrupan los pasajeros.

``` python
import matplotlib.pyplot as plt

# Visualizar los clústeres utilizando dos características como ejemplo
plt.scatter(data['Age'], data['Fare'], c=labels, cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Clustering de Pasajeros del Titanic')
plt.show()
```

#### Paso 4: Reducción de Dimensionalidad con PCA
Para facilitar la visualización de los clústeres en un espacio bidimensional, aplicaremos PCA para reducir las dimensiones de los datos.

``` python
from sklearn.decomposition import PCA

# Aplicar PCA para reducir las dimensiones a 2
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Visualizar los clústeres en el espacio reducido
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.title('PCA de Clústeres en el Conjunto de Datos Titanic')
plt.show()
```

#### Interpretación de los Resultados
* **Clustering con K-Means**: El algoritmo K-Means ha agrupado a los pasajeros del Titanic en tres clústeres basados en las características seleccionadas, como la clase del pasajero, su edad, el número de familiares a bordo, el precio del billete y el género. Estos clústeres podrían representar diferentes perfiles de pasajeros, como familias, personas que viajaban solas, o pasajeros de diferentes clases sociales.

* **Reducción de Dimensionalidad con PCA**: La aplicación de PCA nos ha permitido reducir la dimensionalidad de los datos y visualizar los clústeres en un espacio bidimensional. Esta visualización puede ayudar a entender mejor cómo se distribuyen y agrupan los pasajeros según sus características principales.

En esta actividad, hemos aplicado técnicas de aprendizaje no supervisado utilizando el conjunto de datos "Titanic: Machine Learning from Disaster". Aunque este conjunto de datos está diseñado principalmente para predicciones supervisadas, las técnicas no supervisadas, como K-Means y PCA, nos permiten descubrir patrones ocultos y explorar cómo se agrupan los pasajeros en función de sus características. Estas técnicas pueden proporcionar información valiosa que podría utilizarse para segmentar a los pasajeros o para preprocesar los datos antes de aplicar modelos supervisados. ¡Continúa explorando y experimentando con diferentes enfoques para profundizar en el aprendizaje no supervisado!