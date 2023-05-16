# Bucles

# Un bucle es una estructura de control que repite un bloque de código mientras se cumpla una condición.

# Aquí hay un ejemplo de un bucle while:

contador = 0

while contador < 5:
    print(f"El contador es {contador}")
    contador += 1

# En este caso, el mensaje se imprimirá y el contador se incrementará en 1 hasta que el contador sea igual a 5.

# También podemos usar un bucle for para iterar sobre una secuencia (como una lista o una cadena):

for i in range(5):
    print(f"El número es {i}")

# Aquí, el mensaje se imprimirá con cada número de 0 a 4.

# Podemos usar la sentencia break para detener el bucle antes de que se cumpla la condición:

for i in range(5):
    if i == 3:
        break
    print(f"El número es {i}")

# En este caso, el bucle se detendrá cuando i sea igual a 3.

# También podemos usar la sentencia continue para saltar a la siguiente iteración del bucle:

for i in range(5):
    if i == 3:
        continue
    print(f"El número es {i}")

# En este caso, cuando i sea igual a 3, no se imprimirá el mensaje y se saltará a la siguiente iteración.