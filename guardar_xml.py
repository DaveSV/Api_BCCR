from urllib.request import urlopen

r = urlopen("https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx/ObtenerIndicadoresEconomicos?Indicador=333&FechaInicio=11/4/2022&FechaFinal=11/4/2022&Nombre=Dave&SubNiveles=N&CorreoElectronico=alb.saenz@gmail.com&Token=IL7CLLIAAL")
with open("indicadores.xml", "wb") as f:
    f.write(r.read())
r.close()