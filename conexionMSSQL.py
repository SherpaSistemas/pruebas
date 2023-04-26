import pyodbc       

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=PROD;UID=;PWD=')


cursor = conn.cursor()

cursor.execute('SELECT * FROM alumnos')
for row in cursor:
    print(row)