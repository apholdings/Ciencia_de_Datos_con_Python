"""
Condicionales

Un condicional es una estructura de control que permite que cierto código 
se ejecute solo si se cumple una condición.

"""
# Aquí hay un ejemplo de una sentencia if simple:

edad = 21

if edad >= 18:
    print("Eres mayor de edad")

# En este caso, el mensaje "Eres mayor de edad" solo se imprimirá si la variable edad es mayor o igual a 18.

# Podemos añadir una sentencia else para que se ejecute cuando la condición del if no se cumpla:

edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# En este caso, si la edad es menor a 18, se imprimirá el mensaje "Eres menor de edad".

# También podemos encadenar varias condiciones usando elif:

edad = 15

if edad >= 18:
    print("Eres mayor de edad")
elif edad < 18 and edad >= 13:
    print("Eres un adolescente")
else:
    print("Eres un niño")

# En este caso, si la edad es entre 13 y 18, se imprimirá "Eres un adolescente".
# Si no se cumple ninguna de las condiciones anteriores, se imprimirá "Eres un niño".
