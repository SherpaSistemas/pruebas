import pyodbc

# Configuración de la conexión a la base de datos
server = 'rdsh-0'
database = 'PROD'
username = ''
password = ''

# Crear cadena de conexión
connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password

# Establecer conexión con la base de datos
connection = pyodbc.connect(connection_string)

# Crear un cursor para ejecutar comandos SQL
cursor = connection.cursor()

# Ejecutar una consulta SELECT para obtener los datos de la tabla origen
select_query = 'SELECT clock,logondate,logoffdate,date,shift,mono,lineitem,pn,opnseq,actsu,actrun,actlab,pieces,scrap,wc,wcmach,opndesc,cslab,csfod,csvod,cspsvc,labcode,direct,complete,userid,rate,flushlab,pursvc,manual,source,moldid,entrytype,remarks,glbatch,posted,dateposted,costreval,transno,acctdiv,txndate,rcptno,setup,labmulti,labmutype,lot,FROM dbo.ltxnhist'
cursor.execute(select_query)

# Recuperar los resultados
resultados = cursor.fetchall()

# Iterar por los resultados y ejecutar una consulta INSERT para insertarlos en la tabla destino
for resultado in resultados:

    clock = resultado[0]
    logondate= resultado[1]
    logoffdate= resultado[2]
    date= resultado[3]
    shift= resultado[4]
    mono= resultado[5]
    lineitem= resultado[6]
    pn= resultado[7]
    opnseq= resultado[8]
    actsu= resultado[9]
    actrun= resultado[10]
    actlab= resultado[11]
    pieces= resultado[12]
    scrap= resultado[13]
    wc= resultado[14]
    wcmach= resultado[15]
    opndesc= resultado[16]
    cslab= resultado[17]
    csfod= resultado[18]
    csvod= resultado[19]
    cspsvc= resultado[20]
    labcode= resultado[21]
    direct= resultado[22]
    complete= resultado[23]
    userid= resultado[24]
    rate= resultado[25]
    flushlab= resultado[26]
    pursvc= resultado[27]
    manual= resultado[28]
    source= resultado[29]
    moldid= resultado[30]
    entrytype= resultado[31]
    remarks= resultado[32]
    glbatch= resultado[33]
    posted= resultado[34]
    dateposted= resultado[35]
    costreval= resultado[36]
    transno= resultado[37]
    acctdiv= resultado[38]
    txndate= resultado[39]
    rcptno= resultado[40]
    setup= resultado[41]
    labmulti= resultado[42]
    labmutype= resultado[43]
    lot= resultado[44]
    

    insert_query = 'INSERT INTO dbo.historico (clock,logondate,logoffdate,date,shift,mono,lineitem,pn,opnseq,actsu,actrun,actlab,pieces,scrap,wc,wcmach,opndesc,cslab,csfod,csvod,cspsvc,labcode,direct,complete,userid,rate,flushlab,pursvc,manual,source,moldid,entrytype,remarks,glbatch,posted,dateposted,costreval,transno,acctdiv,txndate,rcptno,setup,labmulti,labmutype,lot) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
    cursor.execute(insert_query, clock,logondate,logoffdate,date,shift,mono,lineitem,pn,opnseq,actsu,actrun,actlab,pieces,scrap,wc,wcmach,opndesc,cslab,csfod,csvod,cspsvc,labcode,direct,complete,userid,rate,flushlab,pursvc,manual,source,moldid,entrytype,remarks,glbatch,posted,dateposted,costreval,transno,acctdiv,txndate,rcptno,setup,labmulti,labmutype,lot)

# Guardar los cambios
connection.commit()

# Cerrar el cursor y la conexión a la base de datos
cursor.close()
connection.close()
