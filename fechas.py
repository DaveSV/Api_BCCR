from datetime import date
from datetime import datetime

#Día actual
today = date.today()

#Fecha actual
now = datetime.now()

print(today)
print(now)
print("\n")
dia = format(today.day)
mes = format(today.month)
año = format(today.year)
print("\n")
fecha_formateada = dia + "/" + mes + "/" + año
print(fecha_formateada)
