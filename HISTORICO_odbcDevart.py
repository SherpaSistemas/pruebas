import pyodbc

# Configurar la cadena de conexión
conn_str = 'Driver={SQL Server};Server=localhost;Database=PROD;Trusted_Connection=yes;'

# Establecer la conexión
conn = pyodbc.connect(conn_str)

# Crear cursores para las dos bases de datos
cursor_origen = conn.cursor()  # Cursor para la base de datos de origen
cursor_destino = conn.cursor()  # Cursor para la base de datos de destino

# Consulta de selección en la tabla de origen
cursor_origen.execute('SELECT * FROM ltxnhist')

# Recuperar los datos de la tabla de origen
datos_origen = cursor_origen.fetchall()[:5]
cursor_origen.execute("TRUNCATE TABLE historico")#NOMBRE DE LA TABLA EN mssql
cursor_origen.commit()

# Insertar los datos en la tabla de destino
for fila in datos_origen:
    cursor_destino.execute('INSERT INTO historico (clock,logondate,logoffdate,date,shift,mono,lineitem,pn,opnseq,actsu,actrun,actlab,pieces,scrap,wc,wcmach,opndesc,cslab,csfod,csvod,cspsvc,labcode,direct,complete,userid,rate,flushlab,pursvc,manual,source,moldid,entrytype,remarks,glbatch,posted,dateposted,costreval,transno,acctdiv,txndate,rcptno,setup,labmulti,labmutype,lot) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                           fila.clock, fila.logondate, fila.logoffdate,fila.date, fila.shift, fila.mono, fila.lineitem, fila.pn, fila.opnseq, fila.actsu, fila.actrun, fila.actlab, fila.pieces, fila.scrap, fila.wc, fila.wcmach, fila.opndesc, fila.cslab, fila.csfod, fila.csvod, fila.cspsvc, fila.labcode, fila.direct, fila.complete, fila.userid, fila.rate, fila.flushlab, fila.pursvc, fila.manual, fila.source, fila.moldid, fila.entrytype, fila.remarks, fila.glbatch, fila.posted, fila.dateposted, fila.costreval, fila.transno, fila.acctdiv, fila.txndate, fila.rcptno, fila.setup, fila.labmulti, fila.labmutype, fila.lot)

# Confirmar los cambios en la base de datos de destino
conn.commit()

# Cerrar los cursores y la conexión
cursor_origen.close()
cursor_destino.close()
conn.close()