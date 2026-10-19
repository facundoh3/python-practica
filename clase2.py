clientes=[
  { "nombre":"Beto", "Monto":250 },
  { "nombre":"Robert", "Monto":342 },
  { "nombre":"Ana", "Monto":150 }
]

cliente=max(clientes, key=lambda c: c["Monto"])
print("El cliente que mas gasto fue ",cliente.get("nombre"))
montoOrdenado=sorted(clientes, key=lambda n: n["Monto"], reverse=True)
print(montoOrdenado)