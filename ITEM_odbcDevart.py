import pyodbc

# create a connection string luki
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

cursor.execute("SELECT * FROM inv") #NOMBRE DE LA TABLA EN winmagi
rows = cursor.fetchall()[:10]

cursorSQL.execute("TRUNCATE TABLE dbo.item")#NOMBRE DE LA TABLA EN mssql
cursorSQL.commit()

# Nombres de los campos
columns = [column[0] for column in cursor.description]
print(columns)

n=1
for row in rows:
     print("",n,"  -------------> ",row)
     cursorSQL.execute("INSERT INTO dbo.item (pn,[desc],bolcode,schdfore,schdback,fcstman,um,qacodes,type,drawing,mbcode,invcat,engstatus,prerel,engdate,engdesc,blueprt,llcd,wgt,insp,lotctl,datectl,reminsp,acctman,engineer,rop,eoq,min,max,mul,sscode,ss,abc,lt,ltprep,ltrect,maxcumlt,ltsales,mouse,sfact,mrpop,mrpcheck,mrpreplan,mrppos,country,cycflag,mrpposnum,filterin,mrpms,filterout,mrptype,autoded,whse,location,fcstuse,forecast,fcstmanual,fcstexpctl,fcstimplod,yield,planner,cubes,cycdays,acctno,costlotsz,freezecst,fsmat,fslab,fsfod,fsvod,fsscrp,fspsvc,fsdate,csmat,cslab,csfod,csvod,csscrp,cspsvc,csdate,cycdate,amat,alab,afod,avod,ascrp,apsvc,adate,smmat,smlab,smfod,smvod,smscrp,smpsvc,smdate,lamat,lalab,lafod,lavod,client,invplan,makefor,prodline,tolerance,warntdays,modifydate,stockmth,modifyby,naftahcode,autopoctl,ltoffset,mktcode1,mktcode2,brand,cofcreqd,lapsvc,sourcepn,lascrp,revision,revctl,ssalone,pctbuy,pctbuymin,ladate,lyfmat,lyflab,lyffod,lyfvod,lyfscrp,lyfpsvc,lyfdate,comdty,price,vendor,buyer,prodclass,catalog,mlpcode,bfmaterial,mlpqty,shiplt,qtypkg,palletpkg,systemgen,aveprice,configrev,mktdesc,nxtcfgseq,automfg,taxable,gdrawing,cstcheck,rempo,remco,remmo,lselect,catnum,manualloc,nonstock,picture,serialctl,costmethod,optdisp,opthist,wipidlbl,prodidlbl,reportid,mtrlcost,mrpdemctl,mrpfcstctl,warntgrp,bomplace)VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8], row[9], row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19], row[20], row[21], row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30], row[31], row[32], row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40],row[41], row[42],row[43],row[44],row[45],row[46],row[47],row[48],row[49],row[50], row[51], row[52],row[53],row[54],row[55],row[56],row[57],row[58],row[59],row[60],row[61], row[62], row[63], row[64],row[65],row[66],row[67],row[68],row[69],row[70],row[71],row[72], row[73], row[74], row[75],row[76],row[77],row[78],row[79],row[80],row[81],row[82],row[83], row[84],row[85],row[86],row[87],row[88],row[89],row[90],row[91],row[92], row[93], row[94],row[95],row[96],row[97],row[98],row[99],row[100],row[101],row[102],row[103], row[104], row[105], row[106],row[107],row[108],row[109],row[110],row[111],row[112],row[113],row[114], row[115], row[116], row[117],row[118],row[119],row[120],row[121],row[122],row[123],row[124],row[125],row[126],row[127],row[128],row[129],row[130],row[131],row[132],row[133],row[134], row[135], row[136],row[137],row[138],row[139],row[140],row[141],row[142],row[143],row[144],row[145], row[146], row[147], row[148],row[149],row[150],row[151],row[152],row[153],row[154],row[155],row[156], row[157], row[158], row[159],row[160],row[161],row[162],row[163],row[164],row[165],row[166],row[167],row[168],row[169],row[170],row[171])
    
   
     # cursorSQL.execute("INSERT INTO dbo.inv (pn) VALUES (?)",row[0])
     n+=1
cursorSQL.commit()

# cerrar cursor y conexion SQL
cursorSQL.close()
conn.close()

# cerrar cursor y conexion VFP
cursor.close()
cnxn.close()

 #milton agrego git 