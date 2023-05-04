import pyodbc

# create a connection string
# cnxn_str = "Driver={SQL Server};Server=localhost;Database=PROD;Trusted_Connection=yes;"
cnxn_str = (
        "Driver={Devart ODBC Driver for xBase};"
        "DBFFormat=VisualFoxPro;"
        "CollatingSequence=general;"
        "UID='';"
        "PWD='';"
        "Database=C:/WinMAGI/DATA/;"
    )

# conexion y cursor VFP
cnxn = pyodbc.connect(cnxn_str)
cursor = cnxn.cursor()

# conexion y cursor SQL
conn = pyodbc.connect('DSN=OdooSQL;Trusted_Connection=yes;Database=PROD;')
cursorSQL = conn.cursor()

cursor.execute("SELECT * FROM momast") #NOMBRE DE LA TABLA EN winmagi
rows = cursor.fetchall()[:20]

cursorSQL.execute("TRUNCATE TABLE dbo.momast") #NOMBRE DE LA TABLA EN mssql
cursorSQL.commit()

# Nombres de los campos
# índices de las columnas que deseas recuperar
#indices = [1, 3, 5, 6]  
#columns = [cursor.description[i][0] for i in indices]

columns = [column[0] for column in cursor.description]
print(columns)

n=1
for row in rows:
    print("",n,"  -------------> ",row)
    cursorSQL.execute("INSERT INTO dbo.momast (mono,whse,motype,status,statdate,project,entrydate,comments,selected) VALUES (?,?,?,?,?,?,?,?,?)",row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
    # cursorSQL.execute("INSERT INTO dbo.momastt (mono) VALUES (?)",row[0])
    n+=1
cursorSQL.commit()

###########################    TABLA MOMAST    ###################################



# for r in sale_order:
#     cursor.execute("INSERT INTO sale_order (id,Number,CreationDate,Customer_id,Customer,Company_id,Company,Total,Status,DeliveryDate,ExpectedDate,Website,team_id,SalesTeam,UntaxedAmount,Taxes,InvoiceStatus) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",r["id"],r["name"],r["create_date"],r["partner_id"][0],r["partner_id"][1],r["company_id"][0],r["company_id"][1],r["amount_total"],r["state"],nz(r["commitment_date"],None),nz(r["expected_date"],None),r["website_id"],r["team_id"][0],r["team_id"][1],r["amount_untaxed"],r["amount_tax"],r["invoice_status"]) 
#     # print(r)
#     # print(nz(r["tag_ids"],None))
# cursor.commit()


# cerrar cursor y conexion SQL
cursorSQL.close()
conn.close()

# cerrar cursor y conexion VFP
cursor.close()
cnxn.close()


