import sqlite3
import sys

if len(sys.argv) == 2:

	conn = sqlite3.connect(sys.argv[1])

	print("Base ouverte avec succés")

	conn.execute("""
		INSERT INTO Client (idc,nom,age,avoir)
		VALUES (1,'Riton',23,1700)
		""")

	conn.execute("""
		INSERT INTO Village(idv,ville,activite,prix,capacite)
		VALUES (10,'Rio','kitesurf',50,250)
		""")

	conn.execute("""
		INSERT INTO Sejour(ids,idc,idv,jour)
		VALUES (100,2,11,365)
		""")

	conn.commit()

	print("Insertion faites .. ")
	conn.close()

else:

	print("Usage : insertRandomValue.py <chemin_bd")