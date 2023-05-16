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
