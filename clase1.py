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
    return 0


print(promedio(ventas))
