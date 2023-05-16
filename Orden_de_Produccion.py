import pyodbc

# Configurar la cadena de conexión
conn_str = 'Driver={SQL Server};Server=localhost;Database=PROD;Trusted_Connection=yes;'

# Establecer la conexión
conn = pyodbc.connect(conn_str)

# Crear cursores para las dos bases de datos
cursor_origen = conn.cursor()  # Cursor para la base de datos de origen
cursor_destino = conn.cursor()  # Cursor para la base de datos de destino

# Consulta de selección en la tabla de origen
cursor_origen.execute('SELECT * FROM modet')

# Recuperar los datos de la tabla de origen
datos_origen = cursor_origen.fetchall()[:3]
cursor_origen.execute("TRUNCATE TABLE orden_de_produccion")#NOMBRE DE LA TABLA EN mssql
cursor_origen.commit()

# Insertar los datos en la tabla de destino
for fila in datos_origen:
    cursor_destino.execute('INSERT INTO orden_de_produccion (mono) VALUES (?)',
                           fila.mono)

# Confirmar los cambios en la base de datos de destino
conn.commit()

# Cerrar los cursores y la conexión
cursor_origen.close()
cursor_destino.close()
conn.close()
