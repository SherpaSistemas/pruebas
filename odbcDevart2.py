import pyodbc
import dbfread

# create a connection string
# cnxn_str = "Driver={SQL Server};Server=localhost;Database=db_odoo;Trusted_Connection=yes;"
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

# execute a query
cursor.execute("SELECT * FROM momast")

# fetch the results
rows = cursor.fetchall()
 
# print the results with row number
for i, row in enumerate(rows):
    print(f"{i+1}. {row}")

# close the cursor and the connection
cursor.close()
cnxn.close()
