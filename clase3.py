import pandas as pd
archivo=pd.read_excel("Registro_Horario.xls", engine="calamine")
# print("forma", archivo.shape)
# print()
# print("columnas", list(archivo.columns))
# print()
# print("primeras filas", archivo.head())
# print()
# print("linea seleccionada", archivo.iloc[865])

# archivo.iterrows()

dias=("SÁBADO", "DOMINGO")
etiqueta=("TRABAJO", "FALTA", "SALTEAR")

for i,f in archivo.head(15).iterrows():
  finde=f["Calendario"] in dias # Si es sabado o domingo
  no_marcacion=pd.isna(f["Marc-Ent"]) # si el marc-ent

  if finde and no_marcacion:
    print("No va al reporte")
  elif f["Calendario"] and no_marcacion:
    print("Falto en dia habil")
  else:
    print(f)
    print(len(f))


# Nº              20416601101
# Nombre        ALVAREZ RENZO
# Fecha            15/10/2026
# Calendario           JUEVES
# Marc-Ent              07:58
# Marc-Sal              17:00
# TiemAsist             09:02
# Tiempo OT               NaN
# Name: 869, dtype: object