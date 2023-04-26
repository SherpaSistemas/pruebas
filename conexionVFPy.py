from dbfread import DBF

# Especificar la ruta del archivo DBF
dbf_path = 'C:\WinMAGI\Data\modet.dbf'

# Abrir el archivo DBF y cargar los datos en una lista de diccionarios
table = DBF(dbf_path)
data = []
for record in table:
    data.append(dict(record))

# Mostrar los datos cargados
print(data)




   