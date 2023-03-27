import sqlite3# se importa el modulo sqlite3 
con=sqlite3.connect('C:\\piña\\sqlite-tools\\db\\pythondb.db')#se establece una conexión con la base de datos SQLite ubicada en la ruta especificada ('C:\piña\sqlite-tools\db\pythondb.db'). La función connect() devuelve un objeto Connection, que se asigna a la variable con.

print(type(con)) # se imprime el tipo de objeto de la variable con, que en este caso debería ser <class 'sqlite3.Connection'>.
micursor=con.cursor()#se crea un objeto Cursor que permite ejecutar consultas SQL en la base de datos. El cursor se crea a través del método cursor() del objeto Connection y se asigna a la variable micursor.
print(type(micursor)) #se imprime el tipo de objeto de la variable micursor, que en este caso debería ser <class 'sqlite3.Cursor'>.
new_sql="SELECT * from Persona;"#se define una variable new_sql que contiene una consulta SQL para seleccionar todas las filas y columnas de la tabla Persona.
micursor.execute(new_sql)#se ejecuta la consulta SQL definida en la variable new_sql a través del método execute() del objeto Cursor.
lista=micursor.fetchall()#se recuperan todas las filas seleccionadas por la consulta SQL ejecutada y se asignan a la variable lista. El método fetchall() devuelve una lista de tuplas, donde cada tupla representa una fila de la tabla y cada elemento de la tupla representa un valor en una columna.
for fila in lista:#se itera sobre la lista de tuplas lista utilizando un bucle for. En cada iteración, se asigna una tupla que representa una fila de la tabla a la variable fila.
    print(fila[0])#se imprimen los valores de los primeros cuatro elementos de la tupla fila, que corresponden a los valores de las primeras cuatro columnas de la tabla.
    print(fila[1])
    print(fila[2])
    print(fila[3])
    print('*'*50)

