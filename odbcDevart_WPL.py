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
conn = pyodbc.connect('DSN=OdooSQL;Trusted_Connection=yes;')
cursorSQL = conn.cursor()

cursor.execute("SELECT * FROM wpl") #NOMBRE DE LA TABLA EN winmagi
rows = cursor.fetchall()#[:10]

cursorSQL.execute("TRUNCATE TABLE dbo.wpl") #NOMBRE DE LA TABLA EN mssql
cursorSQL.commit()

# Nombres de los campos
columns = [column[0] for column in cursor.description]
print(columns)

n=1
for row in rows:
    # print(row)
    cursorSQL.execute("INSERT INTO dbo.wpl (STATUS,MONO,LINEITEM,OPNSEQ,DUEDATE,AVAILDATE,BEGDATE,ENDDATE,WC,WCMACH,SUHR,RUNHR,PN,LOGONDATE,SCHDMACH,QTYORD,QTYRCD,QTYSCRP,LOGONMACH,FIRMSCHD,COMPLETE,TOOLING,AVAILABLE,OPN,OPNDESC,EXTDESC,RESREQ,ACTSU,ACTRUN,ACTLAB,FSLAB,FSFOD,FSVOD,FSPSVC,EFFICIENCY,RESOURCES,PURSVC,VENDOR,PURSVCPN,PURSVCLT,PURSVCMULT,PURSVCPO,PURSVCPL,MOLDID,REMARKS,LABHR,RUNQTY,FLUSHLAB,RUNAHEAD,COIL,DIE,USERID,LOGOFFDATE,SCHEDULED,PSVCPONO,PURSVCHIST,PSVCPACKD,RUNAHEADQT,PURSVCPREM,SELECTED,MAXLOGON,LABCODE,LEVEL,SHIPID,TESTCODE,OPTYPE,MOVETOWC,  ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",n,
                      row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8], row[9], row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19], row[20], row[21], row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30], row[31], row[32], row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40],row[41], row[42],row[43],row[44],row[45],row[46],row[47],row[48],row[49],row[50], row[51], row[52],row[53],row[54],row[55],row[56],row[57],row[58],row[59],row[60],row[61], row[62], row[63], row[64],row[65],row[66])
    # cursorSQL.execute("INSERT INTO dbo.momast (id,mono) VALUES (?,?)",n,row[0])

    
    #cursorSQL.execute("INSERT INTO dbo.wpl (status,mono,lineitem,opnseq,duedate,availdate,begdate,enddate,wc,wcmach,suhr,runhr,pn,logondate,schdmach,qtyord,qtyrcd,qtyscrp,logonmach,firmschd,complete,tooling,available,opn,opndesc,extdesc,resreq,actsu,actrun,actlab,fslab,fsfod,fsvod,fspsvc,efficiency,resources,pursvc,vendor,pursvcpn,pursvclt,pursvcmult,pursvcpo,pursvcpl,moldid,remarks,labhr,runqty,flushlab,runahead,coil,die,userid,logoffdate,scheduled,psvcpono,pursvchist,psvcpackd,runaheadqt,pursvcprem,selected,maxlogon,labcode,level,shipid,testcode,optype,movetowc,    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",n,
       



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


