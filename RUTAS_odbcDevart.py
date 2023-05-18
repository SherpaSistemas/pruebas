import pyodbc

# Configurar la cadena de conexión
conn_str = 'Driver={SQL Server};Server=localhost;Database=PROD;Trusted_Connection=yes;'

# Establecer la conexión
conn = pyodbc.connect(conn_str)

# Crear cursores para las dos bases de datos
cursor_origen = conn.cursor()  # Cursor para la base de datos de origen
cursor_destino = conn.cursor()  # Cursor para la base de datos de destino

# Consulta de selección en la tabla de origen
cursor_origen.execute('SELECT * FROM rtg')

# Recuperar los datos de la tabla de origen
datos_origen = cursor_origen.fetchall()[:5]
cursor_origen.execute("TRUNCATE TABLE rutas")#NOMBRE DE LA TABLA EN mssql
cursor_origen.commit()

# Insertar los datos en la tabla de destino
for fila in datos_origen:
    cursor_destino.execute('INSERT INTO rutas(pn,opndesc,rtgid,opnseq,opn,wc,suhr,runhr,efficiency,extdesc,resources,revin,effin,revout,effout,tooling,pursvc,[pursvcpn],pursvclt,pursvcmult,pursvcpl,pursvcpo,vendor,shipper,moldid,systemgen,runqty,labhr,flushlab,runahead,runaheadqt,coproddisc,pursvcprem,maxlogon,updatedby,updateon,labcode,wcmach,rtgctlcode,shipid,movetowc,testcode) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                           fila.pn, fila.opndesc, fila.rtgid, fila.opnseq, fila.opn, fila.wc, fila.suhr, fila.runhr, fila.efficiency, fila.extdesc, fila.resources, fila.revin, fila.effin, fila.revout, fila.effout, fila.tooling, fila.pursvc, fila.pursvcpn, fila.pursvclt, fila.pursvcmult, fila.pursvcpl, fila.pursvcpo, fila.vendor, fila.shipper, fila.moldid, fila.systemgen, fila.runqty, fila.labhr, fila.flushlab, fila.runahead, fila.runaheadqt, fila.coproddisc, fila.pursvcprem, fila.maxlogon, fila.updatedby, fila.updateon, fila.labcode, fila.wcmach, fila.rtgctlcode, fila.shipid, fila.movetowc, fila.testcode)

# Confirmar los cambios en la base de datos de destino
conn.commit()

# Cerrar los cursores y la conexión
cursor_origen.close()
cursor_destino.close()
conn.close()