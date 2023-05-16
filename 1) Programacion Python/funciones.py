# Funciones

# Una función es un bloque de código que solo se ejecuta cuando se llama.
# Puedes pasar datos, conocidos como parámetros, a una función.
# Una función puede devolver datos como resultado.

# Aquí hay un ejemplo de una función:


def saludo():
    print("¡Hola, Mundo!")


# Para llamar a esta función, simplemente escriba:

saludo()

# La función saludo() se define y luego se llama. Cuando se llama, imprime "¡Hola, Mundo!".

# También puedes pasar argumentos a una función. Los argumentos son especificados después del nombre de la función, entre paréntesis:


def saludo_con_nombre(nombre):
    print(f"¡Hola, {nombre}!")


saludo_con_nombre("Estudiante")

# Aquí, la función saludo_con_nombre() toma un argumento (nombre) y lo utiliza dentro de la función.

# Las funciones también pueden devolver valores. Para hacerlo, usamos la palabra clave return:


def suma(a, b):
    return a + b


resultado = suma(5, 3)
print(f"El resultado de la suma es: {resultado}")

# Aquí, la función suma() toma dos argumentos (a y b), los suma y devuelve el resultado.
