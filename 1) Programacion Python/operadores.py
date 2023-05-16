"""
Operadores

Python incluye varios tipos de operadores:

1) Operadores Aritméticos: Se utilizan para realizar operaciones aritméticas como suma (+), resta (-), multiplicación (*), división (/), módulo (%), exponenciación (**) y división por el suelo (//).
2) Operadores de comparación: Se utilizan para comparar valores. Devuelven Verdadero o Falso según la condición. Ejemplos son igual a (==), no igual a (!=), mayor que (>), menor que (<), mayor o igual que (>=), y menor o igual que (<=).
3) Operadores de asignación: Se utilizan para asignar valores a variables. El más común es igual a (=), pero existen otros como sumar y asignar (+=), restar y asignar (-=), etc.
4) Operadores lógicos: Se utilizan para combinar sentencias condicionales. Incluyen y, o y no.

"""

# Operadores de Aritmetica:
x = 6
y = 9

suma = x + y
resta = y - x
multiplicacion = x * y
division = y / x
modulo = x % y
exponenciacion = x**y
division_por_suelo = y // x

print(
    f"""
====================================================================================
1) Operadores Aritméticos: Se utilizan para realizar operaciones aritméticas como 
suma {suma} (+), resta {resta} (-), multiplicación {multiplicacion} (*), división {division} (/), 
módulo {modulo} (%), exponenciación {exponenciacion} (**) y división por el suelo {division_por_suelo} (//).
====================================================================================
"""
)


# Operadores de Comparacion
numero_uno = 1
numero_dos = 2

# Ejemplos de todos los operadores de comparación
es_igual = numero_uno == numero_dos
no_es_igual = numero_uno != numero_dos
es_mayor = numero_uno > numero_dos
es_menor = numero_uno < numero_dos
es_mayor_o_igual = numero_uno >= numero_dos
es_menor_o_igual = numero_uno <= numero_dos

print(
    f"""
====================================================================================
2) Operadores de comparación: Se utilizan para comparar valores. 
Devuelven Verdadero o Falso según la condición. 
Ejemplos son igual a {es_igual}, no igual a {no_es_igual}, mayor que {es_mayor}, menor que {es_menor}, mayor o igual que {es_mayor_o_igual}, 
y menor o igual que {es_menor_o_igual}.
====================================================================================
"""
)


# Operadores de Asignación
variable = 10
variable += 5  # equivalente a variable = variable + 5
variable -= 3  # equivalente a variable = variable - 3
variable *= 2  # equivalente a variable = variable * 2
variable /= 2  # equivalente a variable = variable / 2
variable %= 3  # equivalente a variable = variable % 3

print(
    f"""
====================================================================================
3) Operadores de asignación: Se utilizan para asignar valores a variables. 
El más común es igual a (=), pero existen otros como sumar y asignar (+=), restar y asignar (-=), etc.
Valor final de la variable: {variable}
====================================================================================
"""
)

# Operadores Lógicos

verdadero = True
falso = False

operacion_y = (
    verdadero and falso
)  # Devuelve Verdadero si ambas afirmaciones son verdaderas
operacion_o = (
    verdadero or falso
)  # Devuelve Verdadero si al menos una de las afirmaciones es verdadera
operacion_no = (
    not verdadero
)  # Invierte el resultado, devuelve Falso si el resultado es verdadero

print(
    f"""
====================================================================================
4) Operadores lógicos: Se utilizan para combinar sentencias condicionales. Incluyen y, o y no.
Operación Y: {operacion_y}, Operación O: {operacion_o}, Operación NO: {operacion_no}
====================================================================================
"""
)
