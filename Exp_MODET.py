import pandas as pd
import pyodbc
import dbfread


import dbfread
# Ruta del archivo .dbf
ruta_dbf = "C:/WinMAGI/DATA/modet.dbf"

# Leer el archivo .dbf
tabla_dbf = dbfread.DBF(ruta_dbf)

# Ruta del archivo .txt
ruta_txt = "C:/TEST/PROD/Data_Export/modet.txt"  # Cambiar la ruta de salida a la misma carpeta que el .dbf

# Abrir el archivo .txt en modo escritura
archivo_txt = open(ruta_txt, "w")

# Escribir los datos del archivo .dbf en el archivo .txt
for registro in tabla_dbf:
    #linea = "\t".join(str(valor) for valor in registro.values())
    linea = ",".join(str(valor) for valor in registro.values())
    archivo_txt.write(linea + "\n")

# Cerrar los archivos
print("----------------------Se creo el txt modet.txt--------------------------- ")
archivo_txt.close()



# def importa_txt_a_sql():
# Conectarse a SQL Server
server = 'localhost'
database = 'PROD'
username = ''
password = ''
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

cursor = conn.cursor()
#cursor.execute("DROP TABLE modet")

create_table_sql = '''
create table modet (
    id INT IDENTITY(1,1) PRIMARY KEY,
    mono VARCHAR(50),
    lineitem VARCHAR(50),
    pn VARCHAR(50),
    descr VARCHAR(50),
    duedate VARCHAR(50),
    qtyord VARCHAR(50),
    qtyrcd VARCHAR(50),
    statuss VARCHAR(50)
);
'''
cursor.execute(create_table_sql)




       

data = pd.read_csv('C:/TEST/PROD/Data_Export/modet.txt', encoding='ISO-8859-1')

  
df = pd.DataFrame(data)
df = df.where(df.notnull(), None)
# df = df.sort_index(ascending=True)
print(df)

 
    
    
#for row in df.head(999).itertuples():
for row in df.itertuples():
    try:
       cursor.execute("INSERT INTO modet (mono,lineitem,pn,descr,duedate,qtyord,qtyrcd,statuss) VALUES (?,?,?,?,?,?,?,?)",(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
       conn.commit()
    except pyodbc.Error as ex:
        print(ex)
        continue
conn.commit()

 
# conn.commit()
print("-----------------------Terminado-----------------------------------")
cursor.close()
conn.close()

# importa_txt_a_sql()