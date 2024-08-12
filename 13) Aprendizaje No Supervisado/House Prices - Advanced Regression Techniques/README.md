# House Prices: Advanced Regression Techniques

## Actividad - Implementación de Aprendizaje No Supervisado en Conjunto de Datos

### Objetivo
Aplicaremos técnicas de aprendizaje no supervisado, como K-Means para clustering y PCA para reducción de dimensionalidad, en el conjunto de datos "House Prices: Advanced Regression Techniques". El objetivo es identificar patrones entre las características de las viviendas y visualizar cómo se agrupan las casas en función de estas características.

##### Paso 1: Cargar y Preprocesar los Datos
Primero, cargaremos el conjunto de datos y realizaremos un preprocesamiento básico.

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Cargar los datos de entrenamiento
data = pd.read_csv('train.csv')

# Seleccionar algunas características numéricas relevantes para el clustering
features = ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', '1stFlrSF', 'YearBuilt', 'YearRemodAdd']
X = data[features]

# Rellenar valores nulos con la mediana de cada columna
X = X.fillna(X.median())

# Escalar las características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```


##### Paso 2: Aplicar K-Means para Agrupamiento
Aplicaremos el algoritmo K-Means para agrupar las casas en clústeres basados en sus características.

```python
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

##### Paso 3: Visualizar los Resultados
Podemos visualizar los resultados del clustering para ver cómo se agrupan las casas.

``` python
import matplotlib.pyplot as plt

# Visualizar los clústeres utilizando dos características como ejemplo
plt.scatter(data['GrLivArea'], data['SalePrice'], c=labels, cmap='viridis')
plt.xlabel('GrLivArea (Área Habitable)')
plt.ylabel('SalePrice (Precio de Venta)')
plt.title('Clustering de Casas en el Conjunto de Datos House Prices')
plt.show()
```

##### Paso 4: Reducción de Dimensionalidad con PCA
Para visualizar mejor los grupos y reducir la complejidad de los datos, podemos aplicar PCA y luego visualizar los clústeres en un gráfico 2D.

``` python
from sklearn.decomposition import PCA

# Aplicar PCA para reducir las dimensiones a 2
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Visualizar los clústeres en el espacio reducido
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.title('PCA de Clústeres en el Conjunto de Datos House Prices')
plt.show()
```

**Interpretación de los Resultados**
* **Clustering con K-Means**: El algoritmo K-Means ha agrupado las casas en tres clústeres basados en las características seleccionadas. Estos clústeres pueden representar diferentes segmentos de viviendas, como casas de alta, media y baja calidad.

* **Reducción de Dimensionalidad con PCA**: La aplicación de PCA nos ha permitido visualizar los clústeres en un espacio bidimensional, lo que facilita la interpretación visual de cómo se agrupan las casas según sus características principales.

Aunque el conjunto de datos de "House Prices: Advanced Regression Techniques" está diseñado principalmente para aprendizaje supervisado, es posible aplicar técnicas de aprendizaje no supervisado como K-Means y PCA para descubrir patrones subyacentes en los datos. Estas técnicas pueden ser útiles para explorar los datos, identificar segmentos de viviendas, y comprender mejor la estructura de los datos antes de aplicar modelos supervisados.