# affiche l'instance de la base

import sqlite3 as lite
import sys



def getValue(table_name):
    print(f"\n\n-------- {table_name} --------\n\n")
    cur.execute(f"SELECT * FROM {table_name}")
    res = cur.fetchall()

    for raw in res:

        taille = len(raw)

        for i in range(0,taille):
            print(f"{raw[i]}|",end="")
        print("")


def get_posts():
    with conn:
        getValue("Client")
        getValue("Village")
        getValue("Sejour")


if len(sys.argv) == 2:
    conn = lite.connect(sys.argv[1])
    cur = conn.cursor()
    get_posts()
else:
    print("Usage : display.py <chemin_de_la_base>")