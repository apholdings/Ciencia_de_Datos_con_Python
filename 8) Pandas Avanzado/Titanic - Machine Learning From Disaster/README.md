# Titanic - Machine Learning From Disaster

## Actividad - Practicar habilidades avanzadas de pandas en un conjunto de datos desafiante.

Nota: No todas las técnicas que hemos cubierto son aplicables a este conjunto de datos. Por ejemplo, no hay datos de series temporales en el conjunto de datos del Titanic, por lo que no podemos practicar la manipulación de series temporales aquí.

#### Manipulaciones de datos más complejas: apply(), tablas dinámicas, multi-index.

Primero, leamos el conjunto de datos y veamos sus primeras filas:
```python
import pandas as pd

df = pd.read_csv('train.csv')
print(df.head())
```

- **Función apply():** Podemos usar la función apply() para crear una nueva columna llamada 'AgeGroup' que agrupa a las personas por su edad.
```python
def age_group(age):
    if age < 18:
        return 'Child'
    elif age < 60:
        return 'Adult'
    else:
        return 'Senior'

df['AgeGroup'] = df['Age'].apply(age_group)
print(df[['Age', 'AgeGroup']].head())
```

- **Tablas dinámicas:** Podemos usar una tabla dinámica para resumir la tasa de supervivencia por grupo de edad y clase.
```python
pivot = df.pivot_table(values='Survived', index='AgeGroup', columns='Pclass', aggfunc='mean')
print(pivot)
```

- **Multi-index:** Podemos establecer un multi-index en las columnas 'AgeGroup' y 'Sex' para analizar la tasa de supervivencia de diferentes grupos.
df.set_index(['AgeGroup', 'Sex'], inplace=True)
print(df.head())

#### Rendimiento: Uso de operaciones vectorizadas, reducción del uso de memoria.

- **Uso de operaciones vectorizadas:** En lugar de usar un bucle for para iterar sobre las filas del DataFrame y calcular la tasa de supervivencia para cada grupo de edad, podemos usar operaciones vectorizadas para hacerlo de manera más eficiente.
```python
survival_rate = df.groupby('AgeGroup')['Survived'].mean()
print(survival_rate)
```

- **Reducción del uso de memoria:** Podemos cambiar el tipo de datos de algunas columnas para reducir el uso de memoria.
```python
print(df.memory_usage(deep=True))

df['Survived'] = df['Survived'].astype('int8')
df['Pclass'] = df['Pclass'].astype('int8')

print(df.memory_usage(deep=True))
```

Ahora podemos seguir practicando con el conjunuto de datos de House Prices.
[Ver Actividad](https://github.com/apholdings/Ciencia_de_Datos_con_Python/tree/main/7%29%20Ingenieria%20de%20Caracteristicas/House%20Prices%20-%20Advanced%20Regression%20Techniques)