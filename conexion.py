import pyodbc

server = 'localhost'
database = 'modet'
username = 'matorresr'
password = ''

conn = pyodbc.connect('DRIVER={WinMAGI};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Ejecutar consultas a la base de datos
cursor = conn.cursor()
cursor.execute('SELECT * FROM modet')

# Obtener los resultados de la consulta
results = cursor.fetchall()
for row in results:
    print(row)
    
# Cerrar la conexión a la base de datos
conn.close()