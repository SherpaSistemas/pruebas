
import dbfread
# Ruta del archivo .dbf
ruta_dbf = "C:/WinMAGI/DATA/momast.dbf"

# Leer el archivo .dbf
tabla_dbf = dbfread.DBF(ruta_dbf)

# Ruta del archivo .txt
ruta_txt = "C:/momast.txt"  # Cambiar la ruta de salida a la misma carpeta que el .dbf

# Abrir el archivo .txt en modo escritura
archivo_txt = open(ruta_txt, "w")

# Escribir los datos del archivo .dbf en el archivo .txt
for registro in tabla_dbf:
    linea = "\t".join(str(valor) for valor in registro.values())
    archivo_txt.write(linea + "\n")

# Cerrar los archivos
print("se creo el txt momast.txt ")
archivo_txt.close()
