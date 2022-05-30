import pandas as pd



df = pd.DataFrame(columns=['Fecha', 'Tipo_Cambio'])
df= df.append({'Fecha': '2022-03-22T00:00:00-06:00', 'Tipo_Cambio': 1.10440000}, ignore_index=True)
print(df)

diccionario = {'euro1': ['2022-03-22T00:00:00-06:00',1.10440000], 'euro2': ['2022-03-23T00:00:00-06:00',1.09660000], 'euro3': ['2022-03-24T00:00:00-06:00',1.09760000] }
print(diccionario)
df2 = pd.DataFrame(diccionario, columns=['Fecha', 'Tipo_Cambio'])
print(df2)