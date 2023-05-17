# 7) Ingeniería de Características
La ingeniería de características es una parte esencial del aprendizaje automático y la ciencia de datos. Es un proceso creativo que implica la creación de nuevas características a partir de las ya existentes para mejorar el rendimiento de los modelos de aprendizaje automático. Esta tarea es tanto un arte como una ciencia, y a menudo puede ser la diferencia entre un modelo mediocre y un modelo altamente efectivo.

### ¿Qué es la ingeniería de características?
La ingeniería de características es el proceso de utilizar el conocimiento de dominio para crear nuevas características (columnas de datos) que hacen que los algoritmos de aprendizaje automático funcionen mejor. Es una parte esencial del modelado predictivo y, cuando se hace bien, puede tener un impacto mayor en la eficacia del modelo que el algoritmo de aprendizaje automático que se utilice.

### ¿Por qué es importante la ingeniería de características?
Los algoritmos de aprendizaje automático aprenden una solución a un problema a partir de datos de muestra. Cuanto más relevante y significativa sea la información contenida en estos datos, mejor será la solución que el algoritmo pueda aprender.

La ingeniería de características mejora la eficacia del aprendizaje automático al transformar los datos brutos en una forma que es más adecuada para los algoritmos aprender. Aunque los algoritmos de aprendizaje automático pueden aprender a partir de los datos brutos, normalmente pueden aprender de manera más eficaz y eficiente a partir de datos que han sido transformados y organizados de manera inteligente.

### ¿cómo sabemos cuándo considerar la ingeniería de características y qué técnicas utilizar? 
Eso depende en gran medida del problema específico que estemos tratando de resolver y de los datos con los que estemos trabajando. Sin embargo, hay algunas situaciones comunes en las que la ingeniería de características puede ser especialmente útil:

Cuando nuestros datos tienen una estructura compleja que no puede ser capturada fácilmente por un modelo de aprendizaje automático. Por ejemplo, si tenemos una característica de fecha y hora, podríamos crear nuevas características como "hora del día", "día de la semana" o "mes del año", ya que estas podrían tener más relevancia predictiva.

Cuando nuestros datos tienen características categóricas. Los algoritmos de aprendizaje automático requieren entradas numéricas, por lo que necesitamos codificar las variables categóricas en una forma numérica. Una forma común de hacer esto es la codificación one-hot, donde cada valor único en la variable categórica se convierte en una nueva característica binaria.

Cuando nuestras características tienen una distribución sesgada o están en una escala diferente. Algunos algoritmos de aprendizaje automático pueden funcionar mejor cuando los datos están en una determinada forma. Podríamos transformar una característica con una distribución sesgada utilizando la transformación de logaritmo, o normalizar las características para que estén en la misma escala.

Cuando tenemos una gran cantidad de características y no todas son útiles. La selección de características es el proceso de elegir las características más útiles para un problema de aprendizaje automático. Esto puede ayudar a mejorar la eficacia del modelo y a reducir el tiempo de entrenamiento.

### ¿Cómo se hace la ingeniería de características?
La ingeniería de características puede implicar una variedad de actividades, entre las que se incluyen:

1. **Creación de características:** Por ejemplo, si tienes una característica de fecha y hora, podrías crear nuevas características como "hora del día", "día de la semana", "mes del año", etc.

2. **Transformación de características:** Algunos algoritmos de aprendizaje automático pueden funcionar mejor cuando los datos están en una determinada forma. Por ejemplo, podrías transformar una característica con una distribución sesgada utilizando la transformación de logaritmo.

3. **Codificación de variables categóricas:** Los algoritmos de aprendizaje automático requieren entradas numéricas, por lo que necesitamos codificar las variables categóricas en una forma numérica. Una forma común de hacer esto es el "one-hot encoding", donde cada valor único en la variable categórica se convierte en una nueva característica binaria.

4. **Selección de características:** No todas las características son útiles para un problema de aprendizaje automático. Algunas características pueden no contener información relevante, mientras que otras pueden contener información duplicada. La selección de características es el proceso de elegir las características más útiles para un problema de aprendizaje automático.

La ingeniería de características requiere una combinación de conocimientos de dominio, intuición y experimentación. A menudo, es útil visualizar los datos y las relaciones entre las características para obtener ideas para la ingeniería de características.

Ahora veamos como poner en practica la ingenieria de caracteristicas en un conjuntod e datos del mundo real.

[Ver Actividad](https://github.com/apholdings/Ciencia_de_Datos_con_Python/tree/main/7%29%20Ingenieria%20de%20Caracteristicas/Titanic%20-%20Machine%20Learning%20From%20Disaster)