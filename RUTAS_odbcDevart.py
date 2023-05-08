import pyodbc

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

# conexion y cursor VFP
cnxn = pyodbc.connect(cnxn_str)
cursor = cnxn.cursor()

# conexion y cursor SQL
conn = pyodbc.connect('DSN=OdooSQL;Trusted_Connection=yes;Database=PROD;')
cursorSQL = conn.cursor()

cursor.execute("SELECT * FROM rtg") #NOMBRE DE LA TABLA EN winmagi
rows = cursor.fetchall()[:15]

cursorSQL.execute("TRUNCATE TABLE dbo.rutas") #NOMBRE DE LA TABLA EN mssql
cursorSQL.commit()

# Nombres de los campos
columns = [column[0] for column in cursor.description]
print(columns)

n=1
for row in rows:
     print("",n,"  -------------> ",row)
     cursorSQL.execute("INSERT INTO dbo.rutas(pn,opndesc,rtgid,opnseq,opn,wc,suhr,runhr,efficiency,extdesc,resources,revin,effin,revout,effout,tooling,pursvc,pursvcpn,pursvclt,pursvcmult,pursvcpl,pursvcpo,vendor,shipper,moldid,systemgen,runqty,labhr,flushlab,runahead,runaheadqt,coproddisc,pursvcprem,maxlogon,updatedby,updateon,labcode,wcmach,rtgctlcode,shipid,movetowc,testcode) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8], row[9], row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19], row[20], row[21], row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30], row[31], row[32], row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40],row[41])
     # cursorSQL.execute("INSERT INTO dbo.rtg (pn) VALUES (?)",row[0])
     n+=1
cursorSQL.commit()



# cerrar cursor y conexion SQL
cursorSQL.close()
conn.close()

# cerrar cursor y conexion VFP
cursor.close()
cnxn.close()