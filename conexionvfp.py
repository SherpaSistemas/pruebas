import sqlalchemy as db

# Crear la cadena de conexión
connection_string = "DRIVER={Microsoft Visual FoxPro Driver};SourceType=DBF;SourceDB=./modet.dbf;Exclusive=No"

# Conectarse a la base de datos
engine = db.create_engine("mssql+pyodbc:///?odbc_connect={}".format(connection_string))
connection = engine.connect()

# Ejecutar una consulta
query = "SELECT * FROM miTabla"
results = connection.execute(query)

# Recuperar los resultados
for row in results:
    print(row)

# Cerrar la conexión
connection.close()