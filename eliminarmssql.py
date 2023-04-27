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

<<<<<<< HEAD
#ksdfksd<fks<dkdsfkh
=======
#hola soy daniela
>>>>>>> 5dc7d5492a4bc4fe137674ec070c021738cdb548
