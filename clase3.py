import pandas as pd
archivo=pd.read_excel("Registro_Horario.xls", engine="calamine")
# print("forma", archivo.shape)
# print()
# print("columnas", list(archivo.columns))
# print()
# print("primeras filas", archivo.head())
# print()
# print("linea seleccionada", archivo.iloc[865])

DIAS_FINDE=("SÁBADO", "DOMINGO")
etiqueta=("TRABAJO", "FALTA", "SALTEAR")
def normalizador(cadena):
  resultado=cadena.strip().upper()
  return resultado

# Bueno hay que crear un diccionario vacio y adentro del for sumar cada
# empleado

empleados={}
empleados["Nombre"]=[]
empleados["Num-emp"]=[]

for i,f in archivo.head(30).iterrows():
  dia=normalizador(f["Calendario"])
  es_finde=dia in DIAS_FINDE # Si es sabado o domingo
  dias_semana=dia not in DIAS_FINDE
  no_marcacion=pd.isna(f["Marc-Ent"]) # si el marc-ent

  clave=(f["Nombre"],f["Nº"])

  if clave[0] is not empleados["Nombre"]:
    empleados["Nombre"].append(clave[0])
    empleados["Num-emp"].append(clave[1])
  else:
    print("ya esta repetido")


  if es_finde and no_marcacion:
    print(f["Nombre"], f["Fecha"], f["Calendario"], etiqueta[2])
  elif dias_semana and no_marcacion:
    print(f["Nombre"], f["Fecha"], f["Calendario"], etiqueta[1])
  else:
    print(f["Nombre"], f["Fecha"], f["Calendario"], etiqueta[0])

print(empleados)
# Nº              20416601101
# Nombre        ALVAREZ RENZO
# Fecha            15/10/2026
# Calendario           JUEVES
# Marc-Ent              07:58
# Marc-Sal              17:00
# TiemAsist             09:02
# Tiempo OT               NaN
# Name: 869, dtype: object