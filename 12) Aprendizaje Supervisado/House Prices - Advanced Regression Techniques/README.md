# House Prices: Advanced Regression Techniques

## Actividad - Implementación de Aprendizaje Supervisado en Conjunto de Datos

### Objetivo
El objetivo de esta actividad es predecir el precio de venta (SalePrice) de las viviendas en Ames, Iowa, utilizando diversas características de las propiedades. Aplicaremos un modelo de aprendizaje supervisado (regresión lineal) para realizar estas predicciones.

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
El preprocesamiento de datos es crucial para preparar los datos para el modelado. Esto incluye la gestión de valores nulos, la codificación de variables categóricas y la normalización de los datos.

``` python
import numpy as np
from sklearn.preprocessing import StandardScaler

# Rellenar valores nulos en las columnas numéricas con la mediana
numeric_features = train_data.select_dtypes(include=[np.number])
for column in numeric_features.columns:
    train_data[column].fillna(train_data[column].median(), inplace=True)

# Rellenar valores nulos en las columnas categóricas con el valor más frecuente
categorical_features = train_data.select_dtypes(include=[np.object])
for column in categorical_features.columns:
    train_data[column].fillna(train_data[column].mode()[0], inplace=True)

# Convertir variables categóricas en variables dummy
train_data = pd.get_dummies(train_data)

# Separar características y objetivo
X = train_data.drop('SalePrice', axis=1)
y = train_data['SalePrice']

# Escalar las características numéricas
scaler = StandardScaler()
X = scaler.fit_transform(X)
```

#### Paso 3: Dividir los Datos en Conjuntos de Entrenamiento y Prueba
Para evaluar el rendimiento de nuestro modelo, dividiremos los datos en un conjunto de entrenamiento y un conjunto de prueba.

``` python
from sklearn.model_selection import train_test_split

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

#### Paso 4: Seleccionar y Entrenar el Modelo
Utilizaremos un modelo de regresión lineal, que es un modelo supervisado comúnmente utilizado para predecir valores continuos.

``` python
from sklearn.linear_model import LinearRegression

# Crear el modelo de regresión lineal
model = LinearRegression()

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
Evaluaremos el rendimiento del modelo utilizando métricas de evaluación como el Error Cuadrático Medio (MSE) y el Coeficiente de Determinación (R^2).

``` python
from sklearn.metrics import mean_squared_error, r2_score

# Calcular el MSE
mse = mean_squared_error(y_test, predictions)

# Calcular el R^2
r2 = r2_score(y_test, predictions)

print(f'Mean Squared Error (MSE): {mse}')
print(f'R^2 Score: {r2}')
```

#### Paso 7: Interpretar los Resultados
Al ejecutar este código, obtendrás las métricas que indican el rendimiento de tu modelo:

* **Mean Squared Error (MSE)**: Mide el promedio de los cuadrados de los errores, es decir, la diferencia entre el valor predicho y el valor real. Un MSE más bajo indica un mejor ajuste del modelo.
* **R^2 Score**: Indica la proporción de la variabilidad en los datos que es explicada por el modelo. Un R^2 más cercano a 1 indica un modelo mejor.

#### Paso 8: Mejorar el Modelo (Opcional)
Para mejorar el rendimiento del modelo, puedes probar con diferentes técnicas:

* **Seleccionar más características relevantes** o realizar ingeniería de características.
* **Probar otros modelos** más complejos, como Random Forest, Gradient Boosting, etc.
* **Realizar ajuste de hiperparámetros** mediante técnicas como Grid Search o Random Search.
* **Aplicar técnicas de regularización** como Ridge o Lasso para manejar mejor la multicolinealidad entre características.

##### Ejemplo Completo
Aquí tienes el código completo desde la carga de los datos hasta la evaluación del modelo:

``` python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Cargar los datos de entrenamiento
train_data = pd.read_csv('train.csv')

# Preprocesamiento de los datos
numeric_features = train_data.select_dtypes(include=[np.number])
for column in numeric_features.columns:
    train_data[column].fillna(train_data[column].median(), inplace=True)

categorical_features = train_data.select_dtypes(include=[np.object])
for column in categorical_features.columns:
    train_data[column].fillna(train_data[column].mode()[0], inplace=True)

train_data = pd.get_dummies(train_data)
X = train_data.drop('SalePrice', axis=1)
y = train_data['SalePrice']

scaler = StandardScaler()
X = scaler.fit_transform(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
predictions = model.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f'Mean Squared Error (MSE): {mse}')
print(f'R^2 Score: {r2}')
```