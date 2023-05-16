from modulo import suma

resultado = suma(5, 3)


if __name__ == "__main__":
    print(f"El resultado es {resultado}")


"""
En Python, if __name__ == "__main__": es una construcción comúnmente utilizada para permitir o prevenir partes del código de ser ejecutadas cuando los módulos son importados.

Cuando tu script se ejecuta, antes de que se ejecute cualquier código, Python define unas cuantas variables especiales. Una de ellas es __name__, y su valor depende de cómo estamos ejecutando el script.

Si estamos ejecutando el script directamente, como python mi_script.py, entonces Python asigna a __name__ el valor de __main__.

Si el script se está importando desde otro script, por ejemplo, mediante import mi_script, entonces __name__ tomará el nombre del archivo importado (en este caso, mi_script).

Por lo tanto, la línea if __name__ == "__main__": se utiliza para verificar si el script está siendo ejecutado directamente o no.

Si el script se está ejecutando directamente, el código dentro del bloque if __name__ == "__main__": se ejecutará. Si el script está siendo importado desde otro lugar, el código dentro de ese bloque no se ejecutará.

Este patrón se usa a menudo para organizar el código de tal manera que pueda ser reutilizado de manera eficaz. Es decir, si quieres que ciertas partes de tu código solo se ejecuten cuando el script se corre directamente (por ejemplo, pruebas de código o tareas de inicialización), puedes poner ese código dentro del bloque if __name__ == "__main__":.
"""
