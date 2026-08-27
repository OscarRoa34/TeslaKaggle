import pandas as pd

# Cargar el CSV definiendo la primera columna como índice y parseando la fecha
df = pd.read_csv('TESLA.csv', index_col=0)

# Convertir la columna Date a formato datetime explícitamente
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%y')

# Mostrar resumen del dataset
print("Información del Dataset:")
print(df.info())
print("\nPrimeras filas:")
print(df.head())