"""
Paquetes

usaremos numpy y matplotlib para aprender comoo interactuar con librerias externas.

Podemos encontrar todos los paquetes disponibles en pypi. https://pypi.org

"""

###
# Aquí tienes un ejemplo sencillo utilizando numpy y matplotlib para crear un gráfico simple.
# Primero, necesitarás instalar las librerías numpy y matplotlib. Puedes hacerlo con el siguiente comando:
###

# Primero, necesitamos importar las librerías que vamos a utilizar
import numpy as np
import matplotlib.pyplot as plt

# Creamos un arreglo de valores desde 0 hasta 2*pi (un ciclo completo) con un total de 1000 puntos
x = np.linspace(0, 2 * np.pi, 1000)

# Creamos una función senoidal y cosenoidal con estos valores
y_sin = np.sin(x)
y_cos = np.cos(x)

# Generamos el gráfico de la función seno
plt.figure()  # Crea una nueva figura
plt.plot(x, y_sin)  # Dibuja los datos
plt.title("Función seno")  # Agrega un título al gráfico
plt.xlabel("x")  # Agrega un título al eje x
plt.ylabel("sin(x)")  # Agrega un título al eje y
plt.grid(True)  # Agrega una grilla al gráfico
plt.show()  # Muestra el gráfico

# Generamos el gráfico de la función coseno
plt.figure()  # Crea una nueva figura
plt.plot(x, y_cos, "r")  # Dibuja los datos en color rojo
plt.title("Función coseno")  # Agrega un título al gráfico
plt.xlabel("x")  # Agrega un título al eje x
plt.ylabel("cos(x)")  # Agrega un título al eje y
plt.grid(True)  # Agrega una grilla al gráfico
plt.show()  # Muestra el gráfico
