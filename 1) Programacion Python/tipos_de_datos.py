"""
Tipos de datos

Python tiene varios tipos de datos estándar:

1) Números: Pueden ser enteros (1 y 2), flotantes (1,1 y 1,2), números complejos (1+2j), etc.
2) Cadenas: Cadena de texto, secuencias de datos de caracteres. El tipo string en Python se llama "str".
3) Lista: Una lista es una colección de elementos ordenados. Los elementos de una lista están indexados y el índice empieza por 0.
4) Tupla: Una tupla es similar a una lista pero es inmutable. Esto significa que, una vez creada, no se puede modificar.
5) Diccionario: Una colección desordenada de datos en un formato de par clave:valor.

"""

# Numeros

from decimal import Decimal

x = int(5)
y = float(3.4)
z = Decimal("6.9")
j = 1j # El sufijo "j" procede de la ingeniería eléctrica, donde la variable "i" suele utilizarse para la corriente.
# El razonamiento se encuentra aqui: https://stackoverflow.com/questions/24812444/why-are-complex-numbers-in-python-denoted-with-j-instead-of-i

print(f"""
====================================================================================
1) Números: Pueden ser enteros {x}, flotantes {y} y {z}, números complejos {j}, etc.
====================================================================================
""")

# Cadenas de Texto

string = "Cadena de Texto"
f_string = f"Cadena de Texto que Acepta Codigo en Corchetes {x}"
large_string = """Cadena de texto
que puede tener espacios
"""
x = str(x) # Podemos convertir numeros a cadenas y vice versa
secuencia_de_caracteres = string + " Hola :D" + " " + x

print(f"""
====================================================================================
2) Cadenas: {string}, Secuencias de datos de caracteres {secuencia_de_caracteres}. 
El tipo string en Python se llama "str".
====================================================================================
""")


# Listas
lista = [1,2,3,4]
lista2 = [5,6,7,8]
suma_de_listas = lista + lista2

nuevo_item = 9
suma_de_listas.append(nuevo_item) # Aqui he agregado un item a la lista
suma_de_listas.remove(1) # Aqui removi el item por su valor, odseaa el nuumero 1 fue removido de la lista
del lista[2] #Aqui he removido el tercer item por indice

nested_list = ["a", 120, lista]

print(f"""
====================================================================================
3) Lista: Una lista es una colección de elementos ordenados. Ej: {lista}
Los elementos de una lista están indexados y el índice empieza por 0. Ej: {lista[0]}
Podemos agregar y remover items de una lista, Ej: {nuevo_item} fue agregado a {suma_de_listas}
Podemos ver cuantos items tiene una lista, Ej: {len(suma_de_listas)}
Podemos tener una lista adentro de otra e incluir cualquier tipo de dato: {nested_list} 
====================================================================================
""")


# Tuplas
tuple = (1,2,3,4,)

print(f"""
====================================================================================
4) Tupla: Una tupla es similar a una lista pero es inmutable. 
Esto significa que, una vez creada, no se puede modificar.
====================================================================================
""")

# Diccionarios
valor =5 
diccionario = {"llave":valor}

diccionario_complejo = {
    "llave":valor,
    "lista": lista,
    "cadena": secuencia_de_caracteres,
    "diccionario": diccionario
    }

print(f"""
====================================================================================
5) Diccionario: Una colección desordenada de datos en un formato de par clave:valor.
- Podemos acceder al valor de un diccionario de esta manera: {diccionario["llave"]} esto
muestra el valor que guarda la llave.
- Podemos guardar cuualquier tipo de dato como valor {diccionario_complejo['lista']}, 
- incluso podemos nestear diccionarios, similar a como hicimos con laa lista. {diccionario_complejo['diccionario']}
====================================================================================
""")