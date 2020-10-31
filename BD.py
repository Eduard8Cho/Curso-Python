#SMBD: SQLite, MySQL, MariaDB, SQLServer, Postgress, etc.

import sqlite3

cxn = sqlite3.connect('alumnos.db')
cur = cxn.cursor()

#CREATE TABLE Alumnos()

#SELECT 
#INSERT
#UPDATE
#DELETE


#sql = 'CREATE TABLE Alumnos(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(30), edad INTEGER, carrera VARCHAR(20), promedio DECIMAL)'

#sql="""INSERT INTO Alumnos VALUES(NULL,'Pedro',20,'IBIO',9)"""

#id=2
#sql="""DELETE FROM Alumnos WHERE  id={}""".format(id)

id=1
sql="""UPDATE Alumnos SET nombre='Antonio' WHERE  id={}""".format(id)



cur.execute(sql)
cxn.commit()

cur.close()
cxn.close()
