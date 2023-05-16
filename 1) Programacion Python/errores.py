"""
Manejo de errores en Python

En Python, utilizamos bloques try/except para manejar errores o excepciones que pueden surgir durante la ejecución de un programa. 

Podemos manejar diferentes tipos de errores especificando diferentes bloques except para cada tipo de error.
"""

# Ejemplo básico de manejo de errores
try:
    # intentamos dividir por cero, lo cual causará un error
    x = 1 / 0
except ZeroDivisionError:
    print("Error: División por cero.")

# También podemos manejar múltiples errores. Aquí intentaremos convertir una cadena a un número
try:
    # intentamos convertir una cadena a un número, lo cual causará un error
    y = int("Hola Mundo")
except ValueError:
    print("Error: No se puede convertir la cadena a número.")

# Podemos usar un bloque 'finally' para ejecutar código independientemente de si ocurrió un error o no
try:
    # intentamos dividir por cero nuevamente
    x = 1 / 0
except ZeroDivisionError:
    print("Error: División por cero.")
finally:
    print("Esto se imprime independientemente de si ocurrió un error o no.")

# También podemos lanzar nuestros propios errores con la palabra clave 'raise'
try:
    # lanzamos un error con un mensaje personalizado
    raise ValueError("Este es un error personalizado.")
except ValueError as e:
    print(f"Error: {e}")
