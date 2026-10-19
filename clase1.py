ventas=[100,200,75]
print(ventas[0])
ventas.append(300)
print(ventas)

for v in ventas:
  print(v)

cliente={"Nombre":"Ana", "monto":300, "Apellido":"Gonzales"}
print(cliente["Nombre"], cliente["Apellido"], cliente["monto"])

#Function
def total(lista):
  suma=0
  for n in lista:
    suma+=n
  return suma

print("Estas son las ventas", total(ventas))

#1) Tengo una lista de numeros y tengo que sacar el promedio
#2) sumar la longitud de los numeros
#3) sumar el contenido de los numeros de la lista
#4) dividirlo por la longitud
#ventas=[100,200,75,300]

def promedio(v):

  if len(v) == 0:  #len(v)==0
    lonVentas=len(v)
    res=0
    for ventas in v:
      res=res+ventas
    return res/lonVentas
  else:
    return ValueError("Lista vacia")


print(promedio(ventas))

#----------------------Resto de clase 1-----------------

clientes=[
  { "nombre":"Beto", "Monto":250 },
  { "nombre":"Robert", "Monto":342 },
  { "nombre":"Ana", "Monto":150 }
]

def cliente_top(c):
  mayor=c[0].get("Monto")
  for monto in c:
    if monto["Monto"] > mayor:
      mayor=monto["Monto"]
      nombre=monto["nombre"]
  print("El mayor monto es ", mayor, "Y el nombre es:", nombre)
  return mayor

cliente_top(clientes)