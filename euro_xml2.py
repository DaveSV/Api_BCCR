
from urllib.request import urlopen
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, tostring

var_url = urlopen('https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx/ObtenerIndicadoresEconomicos?Indicador=333&FechaInicio=22/03/2022&FechaFinal=24/03/2022&Nombre=Dave&SubNiveles=N&CorreoElectronico=alb.saenz@gmail.com&Token=IL7CLLIAAL')
xmldoc = parse(var_url)


myfile = open("indicadores.xml", "w")
myfile.write(xmldoc)
xml = tostring(xmldoc)
print(xmldoc)

