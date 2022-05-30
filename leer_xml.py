from xml.dom import minidom
from urllib.request import urlopen

r = urlopen("https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx/ObtenerIndicadoresEconomicos?Indicador=333&FechaInicio=11/4/2022&FechaFinal=11/4/2022&Nombre=Dave&SubNiveles=N&CorreoElectronico=alb.saenz@gmail.com&Token=IL7CLLIAAL")
with open("indicadores.xml", "wb") as f:
    f.write(r.read())
r.close()

# parse an xml file by name
mydoc = minidom.parse('indicadores.xml')

fechas = mydoc.getElementsByTagName('DES_FECHA')
valores = mydoc.getElementsByTagName('NUM_VALOR')

print('\nDatos_de_INGC011_CAT_INDICADORECONOMIC (Fechas, Euro):')
for elem in fechas:
    print(elem.firstChild.data)

print('\nDatos_de_INGC011_CAT_INDICADORECONOMIC (Valores, Euro):')
for elem in valores:
    print(elem.firstChild.data)