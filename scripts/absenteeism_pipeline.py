import pandas as pd

#leer archivo excel
archivo = "data/absenteeism.xlsx"

df = pd.read_excel(archivo, engine = "openpyxl")

# mostrar información inicial
print("Data original")
print(df)

# crea indicador total de incidencias
df["total_incidencia"] = df["ausencias"] + df["tardanzas"]

#clasificación de riesgo
df["riesgo"] = df["total_incidencia"].apply(
    lambda x: "Alto" if x>=5 else "Bajo"
)

# mostrar resultado
print("\nData transformada")
print(df)

# exportar a csv limpio
output = "output/absenteeism_clean.csv"

df.to_csv(output, index=False)

print("\nArchivo exportado correctamente")


