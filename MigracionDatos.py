import dbfread
import pyodbc

# Conectarse a SQL Server
server = 'localhost'
database = 'PROD'
username = ''
password = ''
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

 
 

# Leer los datos del archivo DBF
tabla_dbf = 'C:\WinMAGI\Data\modet.dbf'

datos_dbf = dbfread.DBF(tabla_dbf, encoding='iso-8859-1')

datos = []

for fila in datos_dbf:
    datos.append(dict(fila))
print(datos)

# Crear una consulta SQL para insertar los datos en SQL Server
tabla_sql = 'modet'

campos = datos[0].keys()

consulta_sql = 'INSERT INTO ' + tabla_sql + ' (' + ','.join(campos) + ') VALUES (' + ','.join('?' * len(campos)) + ')'

# Ejecutar la consulta SQL y pasar los datos a SQL Server
cursor = conn.cursor()

for fila in datos:
    valores = tuple(fila.values())
    if valores=='':
     continue
    if fila.values=='':
     continue
    
    
    cursor.execute(consulta_sql, valores)

conn.commit()

cursor.close()
conn.close()