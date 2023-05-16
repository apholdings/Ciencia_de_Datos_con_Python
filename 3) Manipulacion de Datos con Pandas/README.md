# 3) Manipulacion de Datos con Pandas

- **Carga de datos:** Lectura de datos desde CSVs, archivos Excel y bases de datos SQL.
- **Limpieza de datos:** Manejo de datos faltantes, datos duplicados y tipos de datos incorrectos.
- **Transformación de datos:** Creación de nuevas columnas, agregación de datos, fusión de marcos de datos.

### Carga de Datos con Pandas
Pandas es increíblemente eficiente para leer una variedad de formatos de datos, incluyendo CSV, Excel y SQL.
Para leer datos desde estos formatos, Pandas proporciona funciones como read_csv(), read_excel(), y read_sql().
Una vez leídos, los datos se almacenan en un objeto DataFrame, que es una estructura de datos bidimensional etiquetada con columnas que pueden ser de diferentes tipos.
``` python
# Importación de Pandas
import pandas as pd

# Leer un archivo CSV
df_csv = pd.read_csv('archivo.csv')

# Leer un archivo Excel
df_excel = pd.read_excel('archivo.xlsx')

# Leer de una base de datos SQL
from sqlalchemy import create_engine
engine = create_engine('sqlite:///database.db')
df_sql = pd.read_sql('SELECT * FROM tabla', engine)
```

### Limpieza de Datos con Pandas
Los datos del mundo real a menudo están llenos de errores, faltantes, duplicados, y pueden tener tipos de datos incorrectos.

#### Pandas proporciona funciones eficientes para manejar estos problemas.

Para tratar con los datos faltantes, Pandas proporciona funciones como **dropna()**, que *elimina las filas o columnas con valores faltantes*, y **fillna()**, que *llena los valores faltantes con un valor específico*.

Para *tratar con los datos duplicados*, Pandas proporciona la función **drop_duplicates()**.

Para *cambiar los tipos de datos de las columnas*, Pandas proporciona la función **astype()**.

``` python
# Importar pandas
import pandas as pd
import numpy as np

# Crear un DataFrame con algunos datos faltantes y duplicados
df = pd.DataFrame(
    {"columna": [1, 2, np.nan, 3, 2], "otra_columna": [np.nan, "b", "b", "c", "d"]}
)

print("DataFrame original:")
print(df)
print("\n")

# Eliminar filas con valores faltantes
df_clean = df.dropna()
print("DataFrame después de eliminar los valores faltantes:")
print(df_clean)
print("\n")

# Llenar los valores faltantes con cero
df_fill = df.fillna(0)
print("DataFrame después de llenar los valores faltantes con cero:")
print(df_fill)
print("\n")

# Eliminar duplicados
df_unique = df.drop_duplicates()
print("DataFrame después de eliminar duplicados:")
print(df_unique)
print("\n")

# Cambiar el tipo de datos de una columna a 'int'
df["columna"] = df["columna"].fillna(0).astype(int)
print("DataFrame después de cambiar el tipo de datos de 'columna' a 'int':")
print(df)

```

[Ver Codigo de Ejemplo](limpieza_de_datos.py)

### Transformación de Datos con Pandas
Pandas proporciona una gran cantidad de funciones para transformar datos en un DataFrame.
Podemos crear nuevas columnas a partir de las existentes, utilizando operaciones matemáticas, funciones de string, funciones de fecha y hora, y más.
La función groupby() permite agregar datos basándose en alguna columna. Por ejemplo, podríamos calcular el promedio de todas las filas que tienen el mismo valor en una columna específica.
Los DataFrames pueden ser fusionados utilizando funciones como merge() y concat(), similares a las operaciones JOIN en SQL.

``` python
from limpieza_de_datos import df

# Importar pandas
import pandas as pd
import numpy as np

# Crear una nueva columna a partir de las existentes
df["nueva_columna"] = df["columna"] * 2

# Agregar datos con groupby
df_grouped = df.groupby("otra_columna").mean()

# Fusionar dos DataFrames
df1 = pd.DataFrame(
    {"A": ["A0", "A1", "A2"], "B": ["B0", "B1", "B2"]}, index=["K0", "K1", "K2"]
)
df2 = pd.DataFrame(
    {"C": ["C0", "C1", "C2"], "D": ["D0", "D1", "D2"]}, index=["K0", "K2", "K3"]
)
df_merged = pd.concat([df1, df2], axis=1)

```

[Ver Codigo de Ejemplo](transformacion_de_datos.py)

En este código, estamos utilizando un DataFrame de pandas para demostrar las operaciones comunes de limpieza de datos. Primero, creamos un DataFrame con algunos datos faltantes y duplicados. Luego, mostramos cómo eliminar las filas con valores faltantes, cómo llenar los valores faltantes con cero, cómo eliminar los duplicados y cómo cambiar el tipo de datos de una columna a 'int'.

Nota: Como astype(int) no puede manejar los valores NaN, utilizamos fillna(0) antes de cambiar el tipo de datos para asegurarnos de que no haya valores faltantes en la columna.

