import dbfread
import pyodbc

# Conectarse a SQL Server
server = 'localhost'
database = 'PROD'
username = ''
password = ''
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

#crear cursor 
cursor= conn.cursor()

 

# Definir el SQL para crear la tabla
create_table_sql = '''
create table momast (
id int IDENTITY(1,1) PRIMARY KEY,
mono varchar(50),
whse varchar(50),
motype varchar(50),
statuss varchar(50),
statdate varchar(50),
project varchar(50)
);
'''

# Ejecutar el SQL para crear la tabla
cursor.execute(create_table_sql)


# Leer los datos del archivo DBF
tabla_dbf = 'C:\TEST\COSAS_COMPARTIDAS\pruebas\momast.dbf'

datos_dbf = dbfread.DBF(tabla_dbf, encoding='iso-8859-1')

datos = []

for fila in datos_dbf:
    datos.append(dict(fila))

# Crear una consulta SQL para insertar los datos en SQL Server
tabla_sql = 'momast'

campos = datos[0].keys()

consulta_sql = 'INSERT INTO ' + tabla_sql + ' (' + ','.join(campos) + ') VALUES (' + ','.join('?' * len(campos)) + ')'

# Ejecutar la consulta SQL y pasar los datos a SQL Server
cursor = conn.cursor()

for fila in datos:
    valores = tuple(fila.values())
    cursor.execute(consulta_sql, valores)

conn.commit()

cursor.close()
conn.close()