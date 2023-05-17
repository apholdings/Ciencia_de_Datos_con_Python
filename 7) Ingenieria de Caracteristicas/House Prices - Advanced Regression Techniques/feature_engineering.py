import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# Cargar los datos
df_train = pd.read_csv("train.csv")

# Ver las primeras filas del DataFrame
print(df_train.head())

# Llenar los valores faltantes en las columnas numéricas con la mediana de las columnas correspondientes
df_train = df_train.fillna(df_train.median(numeric_only=True))

# Para las columnas categóricas, llenamos los valores faltantes con la moda (el valor más común)
for column in df_train.select_dtypes(include=["object"]).columns:
    df_train[column] = df_train[column].fillna(df_train[column].mode()[0])


# Ahora, vamos a crear algunas características nuevas y hacer algunas codificaciones.
# Crear una nueva característica 'TotalSF' que es la suma de 'TotalBsmtSF', '1stFlrSF' y '2ndFlrSF'
df_train["TotalSF"] = (
    df_train["TotalBsmtSF"] + df_train["1stFlrSF"] + df_train["2ndFlrSF"]
)

# Codificación One-Hot para la característica 'MSZoning'
df_train = pd.get_dummies(df_train, columns=["MSZoning"])

# Codificación Ordinal para la característica 'LotShape'
# Aquí asumimos que la forma del lote tiene un orden de preferencia
ordinal_encoder = OrdinalEncoder(categories=[["Reg", "IR1", "IR2", "IR3"]])
df_train["LotShape"] = ordinal_encoder.fit_transform(df_train[["LotShape"]])

print(df_train.head())
