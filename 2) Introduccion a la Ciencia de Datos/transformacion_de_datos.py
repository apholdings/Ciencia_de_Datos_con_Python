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
