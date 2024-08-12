# House Prices: Advanced Regression Techniques

## Actividad - Implementación de Metricas de Evaluacion en Conjunto de Datos

### Objetivo
El objetivo de esta actividad es utilizar métricas de evaluación en un problema de regresión, específicamente para predecir los precios de las viviendas en el conjunto de datos "House Prices: Advanced Regression Techniques" de Kaggle. Implementaremos y compararemos varias métricas de evaluación, como el **Error Cuadrático Medio (MSE)**, el **Error Absoluto Medio (MAE)** y el **Coeficiente de Determinación (R²)** para evaluar el rendimiento de un modelo de regresión lineal.

#### Paso 1: Cargar y Preprocesar los Datos
Primero, cargaremos el conjunto de datos y realizaremos un preprocesamiento básico para preparar los datos para el análisis.

``` python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Cargar los datos de entrenamiento
data = pd.read_csv('train.csv')

# Seleccionar algunas características numéricas relevantes
features = ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', '1stFlrSF', 'YearBuilt', 'YearRemodAdd']
X = data[features]
y = data['SalePrice']

# Rellenar valores nulos con la mediana de cada columna
X = X.fillna(X.median())

# Escalar las características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

#### Paso 2: Dividir los Datos en Conjuntos de Entrenamiento y Prueba
Dividiremos los datos en conjuntos de entrenamiento y prueba para evaluar el rendimiento del modelo.

``` python
# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
```

#### Paso 3: Entrenar un Modelo de Regresión Lineal
A continuación, entrenaremos un modelo de regresión lineal con los datos de entrenamiento.

``` python
from sklearn.linear_model import LinearRegression

# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)
```

#### Paso 4: Hacer Predicciones
Con el modelo entrenado, realizaremos predicciones sobre el conjunto de prueba.

``` python
# Hacer predicciones en el conjunto de prueba
y_pred = model.predict(X_test)
```

#### Paso 5: Implementar Métricas de Evaluación
Evaluaremos el rendimiento del modelo utilizando varias métricas de evaluación para regresión:

*   **Error Cuadrático Medio (MSE):** \( MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 \)

*   **Error Absoluto Medio (MAE):** \( MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| \)

*   **Coeficiente de Determinación (R²):** \( R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} \)

``` python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Calcular el MSE
mse = mean_squared_error(y_test, y_pred)

# Calcular el MAE
mae = mean_absolute_error(y_test, y_pred)

# Calcular el R²
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error (MSE): {mse}')
print(f'Mean Absolute Error (MAE): {mae}')
print(f'R^2 Score: {r2}')
```

#### Paso 6: Interpretación de los Resultados
* **MSE (Error Cuadrático Medio)**: Mide la magnitud promedio de los errores cuadrados, penalizando los errores grandes más que los pequeños. Un MSE más bajo indica un mejor rendimiento del modelo.

* **MAE (Error Absoluto Medio)**: Mide la magnitud promedio de los errores absolutos, lo que da una idea clara de cuánto se desvían, en promedio, las predicciones del valor real. Es más robusto ante valores atípicos que el MSE.

* **R² (Coeficiente de Determinación)**: Indica qué proporción de la variabilidad en la variable de salida (SalePrice) es explicada por las variables de entrada seleccionadas. Un R² cercano a 1 indica que el modelo explica bien la variabilidad de los datos.

### Ejemplo Completo
Aquí tienes el código completo desde la carga de los datos hasta la evaluación del modelo:

``` python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Cargar los datos de entrenamiento
data = pd.read_csv('train.csv')

# Seleccionar algunas características numéricas relevantes
features = ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', '1stFlrSF', 'YearBuilt', 'YearRemodAdd']
X = data[features]
y = data['SalePrice']

# Rellenar valores nulos con la mediana de cada columna
X = X.fillna(X.median())

# Escalar las características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular y mostrar las métricas de evaluación
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error (MSE): {mse}')
print(f'Mean Absolute Error (MAE): {mae}')
print(f'R^2 Score: {r2}')
```

En esta actividad, hemos implementado y comparado varias métricas de evaluación utilizando un modelo de regresión lineal en el conjunto de datos "House Prices: Advanced Regression Techniques". Las métricas MSE, MAE y R² nos proporcionan una comprensión más profunda del rendimiento del modelo, permitiéndonos medir la precisión de las predicciones y la capacidad del modelo para generalizar a datos no vistos. Estas métricas son esenciales para evaluar y mejorar modelos de aprendizaje automático en problemas de regresión. ¡Continúa explorando y experimentando para dominar estas técnicas!