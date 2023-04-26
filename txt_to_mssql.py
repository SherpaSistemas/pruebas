import pyodbc
import pandas as pd
import os

# Especifica los datos de conexión a la base de datos
server = 'localhost'
database = 'PROD'
username = ''
password = ''
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

 

# Especifica la ruta del archivo de texto
ruta_archivo = 'C:\WinMAGI\DDMRPDATOS\momastprb.txt'

# Lee los datos del archivo de texto y crea una tabla temporal en la base de datos
tabla_temporal = 'momast_datos'
df = pd.read_sql_table(tabla_temporal, conn, schema='<schema_name>', coerce_float=False, parse_dates={...})

df = pd.read_csv(ruta_archivo, sep=',', header=0, names=['mono', 'whse', 'motype', 'status'])
df.to_sql(tabla_temporal, conn, if_exists='replace', index=False)

# Especifica la ruta del archivo de formato momastformato.fmt
ruta_formato = 'C:\WinMAGI\DDMRPDATOS\momastformato.fmt'

# Importa los datos de la tabla temporal a la tabla final utilizando bcp
comando_bcp = 'bcp base_datos.dbo.tabla_final in ' + ruta_archivo + ' -S ' + server + ' -U ' + username + ' -P ' + password + ' -F 2 -f ' + ruta_formato

os.system(comando_bcp)




import pandas as pd
import pyodbc

 
# Configurar la conexión a la base de datos
server = 'localhost'
database = 'PROD'
username = ''
password = ''
driver = '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect(f"DRIVER={driver};"
                      f"SERVER={server};"
                      f"DATABASE={database};"
                      f"UID={username};"
                      f"PWD={password}")

# Definir el nombre y formato del archivo
ruta_archivo = 'C:\WinMAGI\DDMRPDATOS\momastprb.txt'
formato = 'mono,whse,motype,status,statdate,project,entrydate,selected,prefix,approver,requestor,acctdiv,enteredby'

# Leer el archivo en un DataFrame
df = pd.read_csv(ruta_archivo, delimiter=',', header=None, names=formato.split(','))

# Crear tabla temporal con el mismo nombre del archivo
tabla_temporal = ruta_archivo.split('/')[-1].split('.')[0]  # obtener nombre del archivo sin extension
df.to_sql(tabla_temporal, conn, schema='<dbo>', if_exists='replace', index=False)

# Consultar la tabla temporal
df_temporal = pd.read_sql_table(tabla_temporal, conn, schema='<dbo>', coerce_float=False, parse_dates={
    'statdate': '%m/%d/%Y',
    'entrydate': '%m/%d/%Y'
})

# Hacer lo que necesites con el DataFrame temporal
print(df_temporal)

# Cerrar la conexión a la base de datos
conn.close()