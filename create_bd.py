import sqlite3
import sys

if len(sys.argv) == 2:

	conn = sqlite3.connect(sys.argv[1])
	c = conn.cursor()

	c.execute('''

		CREATE TABLE IF NOT EXISTS Client
		(

			idc INTEGER NOT NULL PRIMARY KEY ,
			nom TEXT NOT NULL,
			age INTEGER NOT NULL,
			avoir INTEGER NOT NULL
		)

		''')

	c.execute('''

		CREATE TABLE IF NOT EXISTS Village
		(
			idv INTEGER PRIMARY KEY NOT NULL,
			ville TEXT NOT NULL,
			activite TEXT NOT NULL,
			prix INTEGER NOT NULL,
			capacite INTEGER NOT NULL
		)

		''')

	c.execute('''

		CREATE TABLE IF NOT EXISTS Sejour
		(
			ids INTEGER PRIMARY KEY,
			idc INTEGER NOT NULL,
			idv INTEGER NOT NULL,
			jour DATE NOT NULL,
			FOREIGN KEY(idc) REFERENCES Client(idc),
			FOREIGN KEY(idv) REFERENCES Village(idv)
		)

		''')


	print("---- Base créée avec succés ----")

	conn.close()

else:
	print("Usage : create_bd.py <chemin_bd>")