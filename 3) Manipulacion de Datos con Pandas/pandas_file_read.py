# Importación de Pandas
import pandas as pd

# Leer un archivo CSV
df_csv = pd.read_csv("archivo.csv")

# Leer un archivo Excel
df_excel = pd.read_excel("archivo.xlsx")

# Leer de una base de datos SQL
from sqlalchemy import create_engine

engine = create_engine("sqlite:///database.db")
df_sql = pd.read_sql("SELECT * FROM tabla", engine)
