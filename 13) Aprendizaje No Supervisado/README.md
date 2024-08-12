# 13) Aprendizaje No Supervisado
El aprendizaje no supervisado es un paradigma del aprendizaje automático en el que un modelo se entrena con datos que no están etiquetados. A diferencia del aprendizaje supervisado, donde el objetivo es predecir una etiqueta o valor, el aprendizaje no supervisado busca descubrir patrones, estructuras o relaciones subyacentes en los datos sin referencia a una etiqueta de salida.

## Conceptos Fundamentales del Aprendizaje No Supervisado

#### 1. Datos Sin Etiquetar
* Los datos en aprendizaje no supervisado no tienen etiquetas asociadas. Solo contamos con las características de entrada, y el modelo debe identificar patrones por sí mismo.

#### 2. Agrupamiento (Clustering)
* El objetivo es agrupar los datos en subconjuntos (o clústeres) de manera que los elementos dentro de un clúster sean más similares entre sí que con los elementos de otros clústeres.

* Ejemplos comunes de algoritmos de clustering:
    * K-Means
    * DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
    * Hierarchical Clustering

#### 3. Reducción de Dimensionalidad
* El objetivo es reducir el número de características en un conjunto de datos, mientras se conserva la mayor cantidad posible de la información relevante.
* Ejemplos comunes de algoritmos de reducción de dimensionalidad:
    * PCA (Principal Component Analysis)
    * t-SNE (t-Distributed Stochastic Neighbor Embedding)

#### 4. Asociación
* Identificar reglas que describen grandes porciones de los datos, como encontrar relaciones interesantes entre variables en grandes bases de datos.
* **Ejemplo común**:
    * Algoritmo Apriori

### Ejemplos de Aprendizaje No Supervisado con Scikit-learn

##### Ejemplo 1: Clustering con K-Means
El algoritmo K-Means es uno de los métodos de clustering más utilizados. Su objetivo es dividir un conjunto de datos en un número fijo de clústeres, minimizando la variación dentro de cada clúster.

**Paso 1: Cargar un Conjunto de Datos**
Scikit-learn proporciona varios conjuntos de datos incorporados que son útiles para practicar, como el conjunto de datos de flores de iris.

``` python
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el conjunto de datos Iris
data = load_iris()
X = data.data

# Visualización inicial
sns.pairplot(pd.DataFrame(X, columns=data.feature_names))
plt.show()
```

**Paso 2: Aplicar K-Means para Agrupamiento**
Aplicaremos el algoritmo K-Means para agrupar las flores en tres clústeres.

``` python
from sklearn.cluster import KMeans

# Definir el modelo K-Means
kmeans = KMeans(n_clusters=3, random_state=42)

# Ajustar el modelo a los datos
kmeans.fit(X)

# Obtener las etiquetas de clúster predichas
labels = kmeans.labels_

# Ver los centros de los clústeres
centroids = kmeans.cluster_centers_

print(f"Centroids:\n{centroids}")
```

**Paso 3: Visualizar los Resultados**
Podemos visualizar los resultados del clustering para ver cómo el algoritmo agrupó los datos.

``` python
import matplotlib.pyplot as plt

# Visualizar los clústeres
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red')  # Centroides
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('K-Means Clustering en Iris Dataset')
plt.show()
```

##### Ejemplo 2: Reducción de Dimensionalidad con PCA
PCA es una técnica de reducción de dimensionalidad que transforma un conjunto de datos a un nuevo sistema de coordenadas de modo que la mayor varianza se explique en las primeras coordenadas.

**Paso 1: Aplicar PCA**
Aplicaremos PCA al conjunto de datos Iris para reducir las dimensiones de 4 a 2, y luego visualizaremos los resultados.

``` python
from sklearn.decomposition import PCA

# Definir el modelo PCA
pca = PCA(n_components=2)

# Ajustar el modelo a los datos
X_pca = pca.fit_transform(X)

print(f"Explained variance ratio: {pca.explained_variance_ratio_}")
```

**Paso 2: Visualizar los Resultados**
Podemos visualizar los datos reducidos en un gráfico de dispersión 2D.

``` python
# Visualizar los datos en el espacio reducido
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.title('PCA en Iris Dataset')
plt.show()
```