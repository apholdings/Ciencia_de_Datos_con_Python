# House Prices: Advanced Regression Techniques

## Actividad - Implementación de Sobreajuste e Infraajuste en Conjunto de Datos

### Sobreajuste
En esta sección, vamos a crear un modelo que está sobreajustado a los datos de entrenamiento. Utilizaremos un árbol de decisión muy profundo, que es propenso al sobreajuste porque puede aprender detalles específicos y ruido en los datos de entrenamiento.

1. **Cargar los datos y realizar el preprocesamiento básico:**
``` python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Cargar los datos
train_data = pd.read_csv('train.csv')

# Rellenar valores nulos en las columnas numéricas con la mediana
numeric_features = train_data.select_dtypes(include=[np.number])
for column in numeric_features.columns:
    train_data[column].fillna(train_data[column].median(), inplace=True)

# Convertir variables categóricas en variables dummy
train_data = pd.get_dummies(train_data)

# Separar características y objetivo
X = train_data.drop('SalePrice', axis=1)
y = train_data['SalePrice']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

2. **Entrenar un modelo de árbol de decisión muy profundo:**
``` python
# Entrenar un árbol de decisión muy profundo (alta varianza)
model = DecisionTreeRegressor(max_depth=100, random_state=42)
model.fit(X_train, y_train)

# Evaluar el modelo en los datos de entrenamiento y prueba
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

train_rmse = np.sqrt(mean_squared_error(y_train, train_predictions))
test_rmse = np.sqrt(mean_squared_error(y_test, test_predictions))

print(f'RMSE en entrenamiento: {train_rmse}')
print(f'RMSE en prueba: {test_rmse}')
```

3. **Interpretar los resultados:**
Al ejecutar el código anterior, es probable que veas una RMSE (Root Mean Squared Error) muy baja en el conjunto de entrenamiento y significativamente más alta en el conjunto de prueba, lo que indica que el modelo está sobreajustado.

### Infraajuste
En esta sección, vamos a crear un modelo que está infraajustado a los datos de entrenamiento. Utilizaremos una regresión lineal simple con muy pocas características, lo que es propenso al infraajuste porque no captura la complejidad subyacente en los datos.

1. **Cargar los datos y realizar el preprocesamiento básico:**
``` python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cargar los datos
train_data = pd.read_csv('train.csv')

# Rellenar valores nulos en las columnas numéricas con la mediana
numeric_features = train_data.select_dtypes(include=[np.number])
for column in numeric_features.columns:
    train_data[column].fillna(train_data[column].median(), inplace=True)

# Convertir variables categóricas en variables dummy
train_data = pd.get_dummies(train_data)

# Seleccionar solo algunas características para inducir infraajuste
features = ['OverallQual', 'GrLivArea']
X = train_data[features]
y = train_data['SalePrice']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

2. **Entrenar un modelo de regresión lineal simple:**
``` python
# Entrenar una regresión lineal simple (alto sesgo)
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluar el modelo en los datos de entrenamiento y prueba
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

train_rmse = np.sqrt(mean_squared_error(y_train, train_predictions))
test_rmse = np.sqrt(mean_squared_error(y_test, test_predictions))

print(f'RMSE en entrenamiento: {train_rmse}')
print(f'RMSE en prueba: {test_rmse}')
```

3. **Interpretar los resultados:**
Al ejecutar el código anterior, es probable que veas una RMSE alta tanto en el conjunto de entrenamiento como en el conjunto de prueba, lo que indica que el modelo está infraajustado y no captura adecuadamente la complejidad de los datos.