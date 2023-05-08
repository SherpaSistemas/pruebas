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

cursor.execute("SELECT * FROM ltxnhist") #NOMBRE DE LA TABLA EN winmagi
rows = cursor.fetchall()[:5]

cursorSQL.execute("TRUNCATE TABLE dbo.historico")#NOMBRE DE LA TABLA EN mssql
cursorSQL.commit()

# Nombres de los campos
num_cols = 5  # número de columnas que deseas recuperar
columns = [column[0] for column in cursor.description[:num_cols]]
print("----------->",columns)

n=1
for row in rows:
     print("",n,"  -------------> ",row)
     cursorSQL.execute("INSERT INTO dbo.historico (CLOCK,LOGONDATE,LOGOFFDATE,DATE,SHIFT,MONO,LINEITEM,PN,OPNSEQ,ACTSU,ACTRUN,ACTLAB,PIECES,SCRAP,WC,WCMACH,OPNDESC,CSLAB,CSFOD,CSVOD,CSPSVC,LABCODE,DIRECT,COMPLETE,USERID,RATE,FLUSHLAB,PURSVC,MANUAL,SOURCE,MOLDID,ENTRYTYPE,REMARKS,GLBATCH,POSTED,DATEPOSTED,COSTREVAL,TRANSNO,ACCTDIV,TXNDATE,RCPTNO,SETUP,LABMULTI,LABMUTYPE,LOT) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8], row[9], row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19], row[20], row[21], row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30], row[31], row[32], row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40],row[41],row[42], row[43],row[44])
    
     #   cursorSQL.execute("INSERT INTO dbo.ltxnhist (clock,logondate,logoffdate,date,shift,mono,lineitem,pn,opnseq,actsu,actrun,actlab,pieces,scrap,wc,wcmach,opndesc,cslab,csfod,csvod,cspsvc,labcode,direct,complete,userid,rate,flushlab,pursvc,manual,source,moldid,entrytype,remarks,glbatch,posted,dateposted,costreval,transno,acctdiv,txndate,rcptno,setup,labmulti,labmutype,lot,    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",n,
     #                   row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8], row[9], row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19], row[20], row[21], row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30], row[31], row[32], row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40],row[41],row[42], row[43],row[44])
    
     
     # cursorSQL.execute("INSERT INTO dbo.ltxnhist (clock,logondate) VALUES (?,?)",row[0],row[1])
   
    
     n+=1
cursorSQL.commit()




# cerrar cursor y conexion SQL
cursorSQL.close()
conn.close()

# cerrar cursor y conexion VFP
cursor.close()
cnxn.close()