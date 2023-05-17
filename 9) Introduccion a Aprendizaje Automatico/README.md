# 9) Introducción al aprendizaje automático
Es hora de sumergirnos en uno de los componentes más emocionantes y dinámicos del campo: el Aprendizaje Automático (Machine Learning).

El Aprendizaje Automático es una rama de la Inteligencia Artificial que utiliza métodos estadísticos para permitir que las máquinas mejoren con la experiencia. En esencia, el objetivo del Aprendizaje Automático es crear sistemas que puedan aprender de los datos y hacer predicciones o decisiones sin ser explícitamente programados para hacerlo.

El aprendizaje automático es fundamental para una serie de aplicaciones, incluyendo el análisis de texto, sistemas de recomendación, reconocimiento de imágenes y voz, detección de fraude, predicciones financieras, y más.

### En este módulo, abordaremos los siguientes temas:

- **Introducción al Aprendizaje Automático:** Exploraremos qué es el Aprendizaje Automático, cómo funciona y dónde se utiliza en la vida real.

- **Tipos de Aprendizaje Automático:** Aprenderemos sobre los diferentes tipos de aprendizaje automático, incluyendo el aprendizaje supervisado, no supervisado, semi-supervisado y el aprendizaje por refuerzo.

- **Preprocesamiento de datos:** Aprenderemos cómo preparar los datos para el entrenamiento del modelo, incluyendo cómo manejar los datos faltantes, cómo tratar con los valores atípicos, y cómo escalar y codificar los datos.

- **Selección de características:** Hablaremos de cómo seleccionar las características apropiadas para tu modelo y cómo puedes reducir la dimensionalidad de tus datos.

- **Modelos de Aprendizaje Automático:** Introduciremos varios modelos de aprendizaje automático comunes, incluyendo la regresión lineal, la regresión logística, los árboles de decisión, y los bosques aleatorios.

- **Evaluación del modelo:** Aprenderemos cómo evaluar la efectividad de un modelo de aprendizaje automático, cómo ajustar sus parámetros, y cómo manejar los problemas de sobreajuste y subajuste.

## Introducción al Aprendizaje Automático
El Aprendizaje Automático es una disciplina dentro de la Inteligencia Artificial que se enfoca en el diseño de sistemas que pueden aprender y mejorar a partir de la experiencia. En términos más técnicos, el aprendizaje automático utiliza algoritmos y modelos estadísticos para hacer que las computadoras realicen tareas sin ser explícitamente programadas para hacerlo.

En lugar de escribir código que detalle exactamente cómo realizar una tarea, en el aprendizaje automático utilizamos los datos para entrenar un modelo. Este modelo puede hacer predicciones o decisiones basándose en los datos de entrada que se le proporcionen.

#### ¿Cómo funciona el Aprendizaje Automático?
Aquí hay un ejemplo simple para ilustrar cómo funciona el aprendizaje automático:

Imaginemos que queremos crear un sistema que pueda identificar si una foto contiene una manzana. En lugar de programar reglas específicas sobre cómo luce una manzana (lo que sería extremadamente difícil), podemos alimentar nuestro modelo de aprendizaje automático con muchas fotos que sí contienen manzanas (esto es conocido como datos de entrenamiento).

El modelo "aprende" a partir de estos ejemplos de entrenamiento y luego puede predecir si una nueva foto contiene una manzana. Es importante notar que el modelo no "entiende" realmente lo que es una manzana de la misma manera que un humano lo haría, sino que reconoce patrones en los datos que le permiten hacer esta predicción.

#### ¿Dónde se utiliza el Aprendizaje Automático?
El Aprendizaje Automático se utiliza en una variedad impresionante de aplicaciones en la actualidad, algunas de las cuales son:

- **Reconocimiento de voz:** Los asistentes virtuales como Siri, Alexa y Google Assistant utilizan el aprendizaje automático para entender lo que estás diciendo.

- **Recomendaciones personalizadas:** Los servicios de streaming como Netflix y Spotify utilizan el aprendizaje automático para recomendar contenido que podría gustarte basándose en tu historial de visualización o escucha.

- **Detección de fraude:** Los bancos utilizan el aprendizaje automático para identificar patrones de transacciones fraudulentas.

- **Conducción autónoma:** Los vehículos autónomos utilizan el aprendizaje automático para navegar y tomar decisiones de conducción.

En resumen, el Aprendizaje Automático es una herramienta poderosa que permite a las computadoras aprender de los datos y tomar decisiones o hacer predicciones basadas en esos datos. Está revolucionando una amplia gama de industrias y se está convirtiendo en una habilidad cada vez más importante en el mundo de la ciencia de datos.

## Tipos de Aprendizaje Automático
Vamos a explorar los diferentes tipos de aprendizaje automático:

- **Aprendizaje Supervisado:** Este es probablemente el tipo más común de aprendizaje automático. En el aprendizaje supervisado, tenemos un conjunto de datos etiquetado. Esto significa que para cada conjunto de entradas en nuestros datos, tenemos una salida o etiqueta correspondiente. Por ejemplo, podríamos tener imágenes de perros y gatos, y cada imagen tiene una etiqueta que indica si es un perro o un gato. El objetivo es entrenar un modelo que pueda predecir la etiqueta correcta para nuevas entradas. Ejemplos de algoritmos de aprendizaje supervisado incluyen regresión lineal y logística, máquinas de vectores de soporte (SVM), y árboles de decisión.

- **Aprendizaje No Supervisado:** En el aprendizaje no supervisado, no tenemos etiquetas. En lugar de eso, queremos que el modelo descubra la estructura subyacente en los datos. Por ejemplo, podríamos tener un montón de datos de clientes y queremos que el modelo identifique segmentos o grupos de clientes similares. Ejemplos de algoritmos de aprendizaje no supervisado incluyen k-means, PCA (Principal Component Analysis) y algoritmos de agrupamiento jerárquico.

- **Aprendizaje Semi-supervisado:** Este tipo de aprendizaje automático se encuentra en algún lugar entre el aprendizaje supervisado y el no supervisado. Aquí, tenemos un conjunto de datos en su mayoría sin etiquetar, pero con algunas etiquetas. Los algoritmos de aprendizaje semi-supervisado pueden usar las etiquetas disponibles para ayudar a entender mejor la estructura de los datos y hacer predicciones sobre los datos sin etiquetar. Ejemplos de este tipo de aprendizaje son los algoritmos de propagación de etiquetas y los modelos de mezcla gaussiana.

- **Aprendizaje por Refuerzo:** En el aprendizaje por refuerzo, un agente aprende cómo comportarse en un entorno realizando acciones y recibiendo recompensas o castigos. El objetivo es aprender una serie de acciones que maximicen la recompensa total. Este tipo de aprendizaje automático es comúnmente usado en problemas como el entrenamiento de un modelo para jugar a un videojuego o para controlar un robot en la vida real. Ejemplos de algoritmos de aprendizaje por refuerzo incluyen Q-Learning y Deep Q-Learning.

Cada uno de estos tipos de aprendizaje automático tiene sus propios usos y aplicaciones, y elegir el tipo correcto para tu problema es un primer paso crucial en cualquier proyecto de aprendizaje automático.

## Pre-Procesamiento de Datos
A continuación, te proporciono una introducción a algunas técnicas comunes de preprocesamiento de datos y cómo se pueden implementar en Python utilizando la biblioteca Pandas y Scikit-Learn.

- **Manejo de datos faltantes:** Los datos del mundo real suelen estar llenos de datos faltantes. Antes de poder entrenar un modelo de aprendizaje automático, generalmente tendrás que decidir cómo manejar estos datos faltantes. Algunas de las técnicas más comunes incluyen:

    - **Eliminación:** Si solo faltan unas pocas observaciones, puedes optar por eliminarlas.

    - **Imputación:** En otros casos, puedes reemplazar los datos faltantes con un valor calculado, como la media, mediana o moda.

```python
import pandas as pd
from sklearn.impute import SimpleImputer

# Crear un DataFrame de ejemplo con algunos datos faltantes
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [9, 10, 11, np.nan]
})

# Utilizar un imputador para reemplazar los datos faltantes con la media de cada columna
imputer = SimpleImputer(strategy='mean')
df_imputed = imputer.fit_transform(df)
```

- **Tratamiento de valores atípicos:** Los valores atípicos pueden tener un efecto significativo en tus modelos de aprendizaje automático, a menudo llevando a predicciones pobres. Algunas de las técnicas más comunes para manejar los valores atípicos incluyen:

    - **Capping:** Puedes limitar los valores extremos a un cierto valor.

    - **Transformación:** Aplicar una transformación, como una transformación logarítmica, puede reducir el impacto de los valores atípicos.

- **Escalado y codificación de datos:** Muchos algoritmos de aprendizaje automático requieren que todas las características estén en la misma escala. Además, los algoritmos de aprendizaje automático requieren que las características categóricas se conviertan en numéricas. Aquí es donde entran en juego el escalado y la codificación.

```python
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Para las características numéricas, podemos usar StandardScaler para escalar las características a una media de 0 y una desviación estándar de 1
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[['A', 'B']])

# Para las características categóricas, podemos usar OneHotEncoder para convertirlas en variables ficticias
encoder = OneHotEncoder()
df_encoded = encoder.fit_transform(df[['C']])
```

#### Como se cual tecnica usar
Cada técnica de preprocesamiento de datos tiene su momento y lugar dependiendo del problema que estés resolviendo, el tipo de datos con los que estás trabajando y el modelo que planeas usar. 

1. *Manejo de datos faltantes:*

- **Eliminación:** Útil cuando solo faltan unas pocas observaciones en tu conjunto de datos, y estás seguro de que las observaciones faltantes son aleatorias y no sesgarán el modelo.
- **Imputación:** Es útil cuando hay muchos datos faltantes, y es importante que no se pierda el resto de la información en las observaciones con datos faltantes.

2. **Tratamiento de valores atípicos:**

- **Capping:** Útil cuando sabes que los valores extremos son incorrectos o poco probable que sean representativos de futuras observaciones. Por ejemplo, si tienes una variable de edad y ves un valor de 200, probablemente quieras limitar este valor a un número más razonable.
- **Transformación:** Útil cuando los valores extremos son correctos pero tienen una escala excesiva en comparación con otros datos. Por ejemplo, si estás trabajando con variables financieras que están altamente sesgadas, es posible que desees aplicar una transformación logarítmica para reducir el impacto de los valores extremos.


3. **Escalado y codificación de datos:**

- **Escalado:** Es útil cuando estás utilizando un algoritmo de aprendizaje automático que asume que todas las características están en la misma escala, como la regresión logística, las redes neuronales, y los algoritmos basados en la distancia como K-nearest neighbors y SVM.
- **Codificación:** Se utiliza cuando estás trabajando con variables categóricas en un algoritmo de aprendizaje automático que requiere entradas numéricas. La codificación one-hot es una técnica común, pero hay muchas otras, incluyendo la codificación ordinal y la codificación de variables dummy.

## Selección de características
La selección de características es un paso crucial en la preparación de tus datos para el aprendizaje automático. Al elegir las características más relevantes para tu problema, puedes mejorar el rendimiento de tu modelo y reducir la complejidad de tu modelo, lo que a su vez puede hacer que tu modelo sea más rápido y más interpretable.

#### Existen varias técnicas para la selección de características, incluyendo:

- **Filtrado:** Esta es la forma más simple de selección de características y se basa en características numéricas de las características, como la correlación con la característica objetivo.

- **Envoltura (Wrapper methods):** Estos métodos tratan de encontrar el subconjunto de características que proporciona el mejor rendimiento del modelo. Por ejemplo, el método de eliminación recursiva de características (RFE, por sus siglas en inglés) entrena un modelo, elimina la característica menos importante, y repite el proceso hasta que se alcanza un número predefinido de características.

- **Incorporadas (Embedded methods):** Algunos modelos de aprendizaje automático tienen incorporada la selección de características. Por ejemplo, los modelos basados en árboles como la regresión de bosque aleatorio y el potenciador de gradiente pueden proporcionar una importancia de característica basada en la cantidad de veces que una característica se usa para dividir los datos.

En cuanto a la reducción de la dimensionalidad, es una técnica útil cuando se trabaja con datos de alta dimensión que puede ser difícil de manejar para algunos algoritmos de aprendizaje automático. Las técnicas de reducción de dimensionalidad, como el Análisis de Componentes Principales (PCA) o el Análisis Factorial, pueden ayudarte a reducir la cantidad de características en tus datos transformando tus características originales en un nuevo conjunto de características que mantienen la mayor parte de la información relevante, pero con una dimensionalidad reducida.

Recuerda que la selección de características y la reducción de la dimensionalidad son procesos iterativos y es importante probar diferentes combinaciones y evaluar el rendimiento del modelo.

## Modelos de Aprendizaje Automático
Existen varios modelos de aprendizaje automático, cada uno de los cuales es adecuado para diferentes tipos de problemas. Aquí hay una descripción de algunos de los más comunes:

- **Regresión Lineal:** Este es uno de los algoritmos más simples y se utiliza para predecir un valor numérico basado en las características. El algoritmo de regresión lineal asume una relación lineal entre las características y el valor objetivo.

- **Regresión Logística:** Este es un algoritmo similar a la regresión lineal, pero se utiliza para problemas de clasificación binaria. Predice la probabilidad de que un ejemplo pertenezca a una clase en particular.

- **Árboles de Decisión:** Este algoritmo predice el valor objetivo al aprender reglas de decisión simples inferidas de las características. Los árboles de decisión son muy interpretativos y pueden manejar tanto características numéricas como categóricas.

- **Bosques Aleatorios:** Este es un método de conjunto que construye múltiples árboles de decisión y los combina para obtener una predicción más precisa y robusta. Los bosques aleatorios son menos propensos a sobreajustar los datos que un solo árbol de decisión.

- **Máquinas de Vectores de Soporte (SVM):** Este algoritmo se utiliza para problemas de clasificación y regresión. Las SVMs pueden manejar datos de alta dimensión y son efectivas cuando el número de dimensiones es mayor que el número de muestras.

- **Redes Neuronales:** Este es un algoritmo que se inspira en el funcionamiento del cerebro humano y puede modelar relaciones complejas entre características. Las redes neuronales son muy potentes y se utilizan en una variedad de aplicaciones, desde la visión por computadora hasta el procesamiento del lenguaje natural.

Cada uno de estos algoritmos tiene sus ventajas y desventajas, y la elección del algoritmo depende del problema específico que estés tratando de resolver. Además, la mayoría de estos algoritmos tienen hiperparámetros que debes ajustar para obtener el mejor rendimiento posible. El ajuste de hiperparámetros es un área en sí misma y existen varias técnicas para hacerlo de manera eficiente, como la búsqueda en cuadrícula y la búsqueda aleatoria.

## Evaluación del modelo
La evaluación del modelo es una parte crucial del proceso de aprendizaje automático. Una vez que hemos entrenado nuestro modelo, necesitamos evaluar cuán bien está realizando sus predicciones. Aquí hay algunos conceptos que necesitaremos entender:

- **Métricas de evaluación:** Dependiendo del tipo de problema de aprendizaje automático que estemos tratando (es decir, clasificación, regresión, agrupación), utilizaremos diferentes métricas para evaluar la efectividad de nuestro modelo. Algunas métricas comunes incluyen precisión, recall, F1-score para problemas de clasificación; error cuadrático medio (MSE), error absoluto medio (MAE) para problemas de regresión.

- **Validación cruzada:** La idea de la validación cruzada es dividir nuestro conjunto de datos en 'k' subconjuntos, y luego iterar 'k' veces el proceso de entrenamiento y evaluación, cada vez utilizando un subconjunto diferente para la evaluación y el resto para el entrenamiento. Esto nos proporciona una estimación más robusta de la capacidad de generalización del modelo.

- **Sobreajuste y subajuste:** Cuando nuestro modelo es demasiado complejo para la cantidad de datos que tenemos, puede empezar a 'memorizar' los datos de entrenamiento, lo que resulta en un mal rendimiento en los datos no vistos. A esto se le llama sobreajuste. Por otro lado, si nuestro modelo es demasiado simple, puede no ser capaz de capturar todas las relaciones en los datos, lo que resulta en un rendimiento deficiente tanto en el conjunto de entrenamiento como en el de prueba. A esto se le llama subajuste. Necesitamos encontrar un buen equilibrio entre la complejidad del modelo y su capacidad para generalizar a partir de los datos no vistos.

- **Ajuste de hiperparámetros:** Los hiperparámetros son los parámetros del algoritmo de aprendizaje automático que se establecen antes del entrenamiento. Estos pueden tener un gran impacto en el rendimiento del modelo y, a menudo, necesitan ser optimizados. Algunas técnicas comunes para la optimización de hiperparámetros incluyen la búsqueda en cuadrícula y la búsqueda aleatoria.

Al final de esta semana, los estudiantes tendrán una sólida comprensión de los conceptos fundamentales del aprendizaje automático y estarán listos para aplicar estos conceptos en la práctica.

## Actividad

Apliquemos lo aprendido en la práctica usando el conjunto de datos del Titanic.

[Ver Actividad](1234)