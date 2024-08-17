# MySQL
# Para interactuar con bases de datos MySQL, puedes usar bibliotecas como mysql-connector-python.
import mysql.connector

conexion = mysql.connector.connect(user='usuario', password='contraseña', host='localhost', database='mi_base')
cursor = conexion.cursor()
cursor.execute("SELECT * FROM mi_tabla")
for fila in cursor.fetchall():
    print(fila)
conexion.close()
