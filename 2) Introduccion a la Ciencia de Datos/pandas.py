# Importación de Pandas
import pandas as pd

# Creación de un DataFrame en Pandas
data = {"Nombres": ["Ana", "Juan", "Pedro"], "Edades": [25, 30, 35]}
df = pd.DataFrame(data)

# Realizar operaciones en el DataFrame
print("Información básica del DataFrame:\n")
print(df.info())
print("\nDescripción del DataFrame:\n")
print(df.describe())
