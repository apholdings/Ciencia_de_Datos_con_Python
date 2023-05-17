import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# Cargar los datos
df_train = pd.read_csv("train.csv")

# Ver las primeras filas del DataFrame
print(df_train.head())

# Llenar los valores faltantes en la columna 'Embarked' con el valor más común
df_train["Embarked"].fillna(df_train["Embarked"].mode()[0], inplace=True)

# Crear una nueva característica 'FamilySize'
df_train["FamilySize"] = df_train["SibSp"] + df_train["Parch"]

# Codificación One-Hot para la característica 'Sex'
df_train = pd.get_dummies(df_train, columns=["Sex"])

# Codificación Ordinal para la característica 'Embarked'
# El OrdinalEncoder de sklearn.preprocessing es una herramienta que convierte cada valor categórico en un número entero.
ordinal_encoder = OrdinalEncoder()
df_train["Embarked"] = ordinal_encoder.fit_transform(df_train[["Embarked"]])

print(df_train.head())
