# Titanic - Machine Learning From Disaster

## Actividad - Realizar EDA en un conjunto de datos del mundo real y presentar los resultados.

Comencemos con el análisis exploratorio de los datos. Empezaremos con algunas estadísticas descriptivas básicas, luego observaremos las distribuciones de algunas variables y, finalmente, exploraremos algunas relaciones entre variables.

#### 1. Estadísticas Descriptivas
Empezaremos por obtener algunas estadísticas descriptivas de las variables numéricas en nuestro DataFrame. Esto incluirá el conteo, la media, la desviación estándar, el mínimo, los cuartiles y el máximo.
```python
# Estadísticas descriptivas
print(df_train.describe())
```
Este paso nos da una idea general de la distribución de cada variable numérica.

#### 2. Distribuciones de las Variables
A continuación, podemos visualizar las distribuciones de algunas de nuestras variables. Crearemos histogramas para las variables 'Age', 'Fare' y 'Survived'. Los histogramas son útiles para visualizar la distribución de una variable numérica.
```python
# Histograma de edades
plt.hist(df_train['Age'], bins=10, edgecolor='black')
plt.title('Distribución de las Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()

# Histograma de tarifas
plt.hist(df_train['Fare'], bins=10, edgecolor='black')
plt.title('Distribución de las Tarifas')
plt.xlabel('Tarifa')
plt.ylabel('Frecuencia')
plt.show()

# Histograma de supervivencia
plt.hist(df_train['Survived'], bins=3, edgecolor='black')
plt.title('Distribución de la Supervivencia')
plt.xlabel('Supervivencia')
plt.ylabel('Frecuencia')
plt.show()
```
Estas visualizaciones nos ayudan a entender la forma de las distribuciones de estas variables.

#### 3. Relaciones entre Variables
Finalmente, podemos explorar las relaciones entre algunas de nuestras variables. Un gráfico de caja (boxplot) es una excelente manera de visualizar la relación entre una variable categórica y una variable numérica.
```python
# Boxplot de la edad por supervivencia
df_train.boxplot(column='Age', by='Survived')
plt.title('Edad por Supervivencia')
plt.suptitle('') # Eliminar el título automático
plt.xlabel('Supervivencia')
plt.ylabel('Edad')
plt.show()
```
Este gráfico nos ayuda a ver si hay una diferencia significativa en la distribución de las edades de los que sobrevivieron en comparación con los que no.

### Actividad

Ahora que completamos la primera actividad, hagamos lo mismo pero con un conjunto de datos mas complejo.

[Ver Actividad Completa](https://github.com/apholdings/Ciencia_de_Datos_con_Python/tree/main/6%29%20Analisis%20Exploratorio%20de%20Datos/House%20Prices%20-%20Advanced%20Regression%20Techniques)