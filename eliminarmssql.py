import pyodbc 
#soyDani haciendo pruebas

# Conectarse a la base de datos
server = 'localhost'
database = 'PROD'
username = ''
password = ''
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)


# Crear un objeto cursor
cursor = conn.cursor()

# Ejecutar la consulta SQL para eliminar la tabla
cursor.execute('DROP TABLE alumnos')

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

# se crearon las ramas

#Uriel elimino la clase creaciónPdfyQr que estaba en la rama MAIN y creo la clase pdCreacion en la rama QR 