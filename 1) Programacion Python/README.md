# 1) Programacion Python desde Cero
Python es un lenguaje de programación interpretado con una sintaxis clara y legible.

## Conceptos Basicos
- [Declaración de variables:](variables.py) variable = valor
- [Tipos de datos básicos:](tipos_de_datos.py) int, float, str, bool.
- [Operadores aritméticos:](operadores.py) +, -, *, /, **, %.
- [Bucles:](bucles.py) for, while.
- [Condicionales:](condicionales.py) if, elif, else.

### Estructuras de Datos
Python incluye varias estructuras de datos incorporadas: listas, tuplas, sets, y diccionarios.
- **Listas:** Colecciones ordenadas y modificables de elementos. mi_lista = [1, 2, 3]
- **Tuplas:** Colecciones ordenadas e inmutables de elementos. mi_tupla = (1, 2, 3)
- **Sets:** Colecciones desordenadas de elementos únicos. mi_set = {1, 2, 3}
- **Diccionarios:** Colecciones desordenadas de pares clave-valor. mi_diccionario = {"clave": "valor"}
``` python
# Lista
frutas = ["manzana", "banana", "cereza"]
frutas.append("naranja")

# Tupla
colores = ("rojo", "verde", "azul")

# Set
numeros_unicos = {1, 2, 2, 3, 4, 4, 5}

# Diccionario
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
```

### Control de Flujo en Python
Python utiliza las sentencias if, for, while, break, y continue para controlar el flujo del programa.
- **Sentencias if:** Permiten que el programa tome decisiones basadas en ciertas condiciones.
- **Bucles for y while:** Permiten que el programa ejecute cierto código varias veces.
- **break y continue:** Permiten mayor control sobre el flujo de los bucles.
``` python
# Sentencia if
x = 10
if x > 5:
    print("x es mayor que 5")

# Bucles for y while
for i in range(5):
    print(i)

j = 0
while j < 5:
    print(j)
    j += 1

# break y continue
for num in range(10):
    if num == 5:
        break
    print(num)

for num in range(10):
    if num % 2 == 0:
        continue
    print(num)
```

### Funciones en Python
Las funciones son bloques de código reutilizables que realizan una tarea específica.
- **Definición de funciones:** Se utiliza la palabra clave def para definir una función.
- **Llamada a funciones:** Se utilizan paréntesis () para llamar a una función.
- **Argumentos de funciones:** Las funciones pueden tomar argumentos para realizar sus tareas.
Valores de retorno: Las funciones pueden retornar valores que pueden ser utilizados posteriormente.
``` python
# Definición de función
def saludo(nombre):
    return "Hola, " + nombre + "!"

# Llamada a función
mensaje = saludo("Juan")
print(mensaje)

# Función con múltiples argumentos
def suma(a, b):
    return a + b

# Llamada a función con múltiples argumentos
resultado = suma(5, 3)
print(resultado)
```

### Bibliotecas en Python
Las bibliotecas son conjuntos de funciones y métodos que permiten realizar tareas específicas sin tener que escribir tu propio código.
- **NumPy:** Una biblioteca para manejar matrices de datos numéricos y realizar operaciones matemáticas de alto nivel.
- **Pandas:** Una biblioteca para manipulación y análisis de datos. Proporciona estructuras de datos flexibles y permite trabajar con datos de diferentes tipos y en diferentes formatos.
- **Matplotlib:** Una biblioteca para crear visualizaciones estáticas, animadas e interactivas en Python.

``` python 
# Importación de bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Uso de NumPy
array = np.array([1, 2, 3, 4, 5])
print(array.mean())

# Uso de Pandas
data = {'nombres': ['Ana', 'Juan', 'Pedro'], 'edades': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)

# Uso de Matplotlib
plt.plot(array)
plt.show()
```