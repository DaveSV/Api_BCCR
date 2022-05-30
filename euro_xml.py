import requests
from xml.etree import ElementTree as ET

datos = requests.get("https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx/ObtenerIndicadoresEconomicos?Indicador=333&FechaInicio=22/03/2022&FechaFinal=24/03/2022&Nombre=Dave&SubNiveles=N&CorreoElectronico=alb.saenz@gmail.com&Token=IL7CLLIAAL")

tree = ET.fromstring(datos.content)

print(datos)
print('Total de datos:', len(tree))

lst = tree.findall("Datos_de_INGC011_CAT_INDICADORECONOMIC/INGC011_CAT_INDICADORECONOMIC")
print(lst)
print('Lista de datos:', len(lst))
for item in lst:
    print('Fecha: ', item.find('DES_FECHA').text)
    print('Valor: ', item.find('NUM_VALOR').text)
    print('Atributo', item.get('diffgr:id'))
