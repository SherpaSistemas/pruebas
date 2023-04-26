 
import pyodbc

# def importa_txt_a_sql():
# Conectarse a SQL Server
server = 'localhost'
database = 'PROD'
username = ''
password = ''
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

cursor = conn.cursor()




cnxn_str = (
        "Driver={Devart ODBC Driver for xBase};"
        "DBFFormat=VisualFoxPro;"
        "CollatingSequence=general;"
        "UID='';"
        "PWD='';"
        "Database=C:/WinMAGI/DATA/;"
    )

# establish a connection
cnxn = pyodbc.connect(cnxn_str)

# create a cursor
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM momast")
# fetch the results
rows = cursor.fetchall()

# print the results with row number
for i, row in enumerate(rows):
    print(f"{i+1}. {row}")
 
    

print("termina de imprimir")
  
for i in range(10):
    row = rows[i]
    try:
        cursor.execute("INSERT INTO momast (mono,status,statdate,entrydate) VALUES (?,?,?,?)",row[0],row[3],row[4],row[6])
        conn.commit()
    except pyodbc.Error as ex:
        print("eror--------->"+str(ex))
        continue
conn.commit()

# cursor.execute("SELECT * FROM momast ORDER BY id")
# conn.commit()

cursor.close()
conn.close()

 