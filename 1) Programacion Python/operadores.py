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

suma = x+y
resta = y-x
multiplicacion = x*y
division = y/x
modulo = x%y
exponenciacion = x**y
division_por_suelo = y//x

print(f"""
====================================================================================
1) Operadores Aritméticos: Se utilizan para realizar operaciones aritméticas como 
suma {suma} (+), resta {resta} (-), multiplicación {multiplicacion} (*), división {division} (/), 
módulo {modulo} (%), exponenciación {exponenciacion} (**) y división por el suelo {division_por_suelo} (//).
====================================================================================
""")


# Operadores de Comparacion
x1 = 1
x2 = 2
booleano = True

comparacion = x1 == x2 # Esto nos da Falso

if(comparacion):
    print("Comparacion es verdadero para que esto sea visto")

print(f"""
====================================================================================
2) Operadores de comparación: Se utilizan para comparar valores. 
Devuelven Verdadero o Falso según la condición. 
Ejemplos son igual a (==), no igual a (!=), mayor que (>), menor que (<), mayor o igual que (>=), 
y menor o igual que (<=).
====================================================================================
""")


# Operadores de asignación

print(f"""
====================================================================================
3) Operadores de asignación: Se utilizan para asignar valores a variables. 
El más común es igual a (=), pero existen otros como sumar y asignar (+=), restar y asignar (-=), etc.
====================================================================================
""")


# Operadores de lógicos

print(f"""
====================================================================================
4) Operadores lógicos: Se utilizan para combinar sentencias condicionales. Incluyen y, o y no.
====================================================================================
""")