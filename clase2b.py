registros = [
    {"Nombre": "Morales", "Calendario": "JUEVES",  "TiemAsist": 11.9, "OT": 2.9},
    {"Nombre": "Robert", "Calendario": "SÁBADO",  "TiemAsist": 13.6, "OT": 4.8},
    {"Nombre": "Perez",   "Calendario": "LUNES",   "TiemAsist": 8.0,  "OT": 0.0},
    {"Nombre": "Perez",   "Calendario": "DOMINGO", "TiemAsist": 8.7,  "OT": 0.0},
]

timeAsist=[r["TiemAsist"] for r in registros]
finSemana=[r["Calendario"] for r in registros if r["Calendario"] in ("SÁBADO","DOMINGO") ]
horasExtras=[r["Nombre"] for r in registros if r["OT"] > 0]
totalHoras=sum([r["TiemAsist"] for r in registros])
