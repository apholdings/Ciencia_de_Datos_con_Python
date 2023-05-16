# 6) Análisis Exploratorio de Datos (AED)
El Análisis Exploratorio de Datos (AED) es un paso fundamental en cualquier proyecto de análisis de datos o ciencia de datos. 

Antes de sumergirnos en el modelado complejo o el aprendizaje automático, es vital entender las características básicas, las estructuras, los patrones y las anomalías presentes en nuestros datos. 

Esta comprensión nos ayudará a tomar decisiones informadas sobre cómo procesar los datos, qué modelos usar, qué características son importantes, cómo validar nuestros modelos y más.

### El objetivo principal del AED es:

1. **Maximizar la comprensión de un conjunto de datos.** El AED proporciona una descripción detallada de los datos mediante el uso de estadísticas descriptivas y visualizaciones. Esto nos ayuda a entender qué están diciendo realmente nuestros datos.

2. **Descubrir patrones en los datos.** A través de gráficos y tablas, podemos identificar las tendencias, los patrones y las relaciones en nuestros datos.

3. **Identificar anomalías en los datos.** El AED puede ayudarnos a detectar errores, valores atípicos y otras anomalías que podrían afectar nuestros análisis.

4. **Probar hipótesis.** Mediante el AED, podemos formular y probar hipótesis sobre nuestras variables y sus relaciones.

5. **Preparar el terreno para la inferencia y el modelado.** Al entender nuestros datos, podemos tomar decisiones informadas sobre qué técnicas de inferencia estadística o modelado son apropiadas.

En resumen, el AED es la primera (y una de las más importantes) etapas en la cadena de análisis de datos. Sin él, corremos el riesgo de hacer suposiciones erróneas, usar modelos inapropiados, perder información importante y, en última instancia, obtener resultados incorrectos. Además, la habilidad para realizar un AED efectivo es una de las habilidades más valoradas en los analistas y científicos de datos, ya que demuestra la capacidad para entender y trabajar con los datos en un nivel fundamental.

## Tecnicas de AED
Vamos a ver cómo se realizan algunas de estas técnicas de Análisis Exploratorio de Datos (AED) utilizando Pandas y Matplotlib en Python

Primero, empezaremos por cargar los datos y prepararlos para el análisis. Usaremos el conjunto de datos de "House Prices" que has mencionado antes.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df = pd.read_csv("train.csv")

# Llenar los valores faltantes en las columnas numéricas con la mediana de las columnas correspondientes
df = df.fillna(df.median(numeric_only=True))

# Para las columnas categóricas, llenamos los valores faltantes con la moda (el valor más común)
for column in df.select_dtypes(include=["object"]).columns:
    df[column] = df[column].fillna(df[column].mode()[0])
```

Ahora, haremos algunos gráficos para entender mejor nuestros datos.

### Histogramas
Los histogramas son útiles para visualizar la distribución de una variable numérica. Aquí veremos la distribución de los precios de las viviendas.
```python
plt.hist(df['SalePrice'], bins=30, alpha=0.5)
plt.xlabel('Sale Price')
plt.ylabel('Count')
plt.title('Distribution of Sale Prices')
plt.show()
```

### Boxplots
Los boxplots nos dan una visión rápida de cómo están distribuidos los datos. Son especialmente útiles para identificar valores atípicos. Veamos un boxplot de los precios de las viviendas.
```python
plt.boxplot(df['SalePrice'])
plt.ylabel('Sale Price')
plt.title('Boxplot of Sale Price')
plt.show()
```

### Análisis de correlación
El análisis de correlación nos ayuda a entender cómo están relacionadas entre sí las variables numéricas en nuestro conjunto de datos. Pandas tiene un método muy útil llamado corr() que calcula la correlación entre todas las columnas numéricas del DataFrame.
```python
correlation_matrix = df.corr()
print(correlation_matrix)
```
Para visualizar mejor esta matriz de correlación, podemos usar un mapa de calor.
```python
sns.heatmap(correlation_matrix)
plt.show()
```

### Estadísticos de resumen y groupby
Pandas tiene muchos métodos útiles para obtener estadísticos de resumen. Por ejemplo, el método describe() proporciona un resumen estadístico de todas las columnas numéricas.
```python
print(df.describe())
```
El método groupby() puede ser útil para agrupar los datos por una o más columnas y calcular estadísticas resumen para cada grupo. Por ejemplo, podríamos querer ver el precio medio de venta por tipo de zona residencial (columna 'MSZoning').
```python
print(df.groupby('MSZoning')['SalePrice'].mean())
```

### Manejo de valores atípicos
Los valores atípicos pueden distorsionar nuestras estadísticas y modelos, por lo que es importante identificarlos y tratarlos adecuadamente. Una forma común de tratar los valores atípicos es eliminarlos, pero hay que tener cuidado de no eliminar demasiados datos.

Podríamos identificar los valores atípicos en el precio de venta utilizando la regla del rango intercuartil (IQR). Esta regla dice que un valor es un valor atípico si es menor que Q

1 - 1.5IQR o mayor que Q3 + 1.5IQR, donde Q1 y Q3 son el primer y tercer cuartiles, respectivamente, e IQR es el rango intercuartil.

```python
Q1 = df['SalePrice'].quantile(0.25)
Q3 = df['SalePrice'].quantile(0.75)
IQR = Q3 - Q1

# Definir un límite para los valores atípicos
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identificar los valores atípicos
outliers = df[(df['SalePrice'] < lower_bound) | (df['SalePrice'] > upper_bound)]

# Tratar los valores atípicos
df_no_outliers = df[(df['SalePrice'] >= lower_bound) & (df['SalePrice'] <= upper_bound)]
```

### Actividad
Es momento de poner en practica lo aprendido, como actividad tenemos que hacer analisis exploratorio de datos al conjunto de datos del titanic.

[Ir a la Actividad](https://github.com/apholdings/Ciencia_de_Datos_con_Python/blob/main/6%29%20Analisis%20Exploratorio%20de%20Datos/Titanic%20-%20Machine%20Learning%20From%20Disaster/README.md)