import sqlite3 
import sys

# BD = (S,T) où S est le schèma et T un ensemble de programme 
# ici T = {t1,t2,t3,t4,t5}



class SolveSequence:

    def __init__(self,depart,arrive,epsilon):
        self.depart = depart
        self.arrive = arrive
        self.epsilon = epsilon
        self.chemin = []
        self.atteignable = False

    def solve(self):
        self.epsilon.sort()
        self.epsilon.reverse()

        dep_aux = self.depart

        while True:
            try:
                tmp = dep_aux - self.epsilon[0]

                if tmp < self.arrive:
                    self.epsilon.remove(self.epsilon[0])
                else:
                    dep_aux = tmp 
                    self.chemin.append(self.epsilon[0])

            except:
                pass

            

            if len(self.epsilon) == 0:
                break

        if dep_aux == self.arrive:
            self.atteignable = True
        
        return self.chemin,self.atteignable

    

def lire_client():

        path = ""

        cur.execute("SELECT * FROM Client")

        rows = cur.fetchall()

        cpt = 0

        for row in rows:
                cpt+=1

                taille = len(row)
                avoir = row[3]
                avoir_target.append(avoir)

                if path == "":
                    path+="t1"
                else:
                    path+="->t1"

        #print("------------------- ETAPE 1 -------------------\n")
        #print(f"{cpt} appel(s) à Traitement 1\n")

        return path

def lire_village():

        path = ""

        cur.execute("SELECT * FROM Village")
        rows = cur.fetchall()
        cpt1 = 0

        for row in rows:
            cpt1+=1
            path+="->t2"

            val = row[3]

            if val not in poss_val_sejour:
                    poss_val_sejour.append(val)

        #print("------------------- ETAPE 2 -------------------\n")
        #print(f"{cpt1} appel(s) à Traitement 2\n")

        return path


def somme_prix_sejour(idc):

    cur.execute(f"SELECT prix FROM Sejour,Village WHERE idc = {idc}")
    rows = cur.fetchall()

    somme = 0 

    for row in rows:
        somme+=row[0]

    return somme

def check_if_gap(avoir_final,somme_sejour):

    if avoir_final + somme_sejour != 2000:
        return True,(2000-(avoir_final+somme_sejour))
    else:
        return False,0

def analyse_sejours(val):

        #print("------------------- ETAPE 3 -------------------\n")
        cur.execute("SELECT * FROM Client")
        rows = cur.fetchall()
        copie_val = val.copy()
        bool_tab = []


        for row in rows:

            check = check_if_gap(row[3],somme_prix_sejour(row[0]))
            #print(f"Des séjours ont été supprimés ? : {check[0]}, manque : {check[1]} ")
            

            if check[0] :
                pb = SolveSequence(2000,row[3],copie_val)
                res_tmp = pb.solve()
                bool_tab.append(res_tmp[1])
                #print(f"    séquence atteignable ? : {res_tmp[1]}")
                if res_tmp[1]:
                    #print(f"    chemin : {res_tmp[0]}")
                    pass

            else:
                #print("     séquence atteignable ? : True")
                pass

        return bool_tab

if len(sys.argv) == 2:
    conn = sqlite3.connect(sys.argv[1])
    cur = conn.cursor()


    chemin = ""

    poss_val_sejour = []
    avoir_target = []     


    if __name__ == '__main__':
        
        # on fetch les values
        chemin+=lire_client()
        chemin+=lire_village()
        bool_atteignable = analyse_sejours(poss_val_sejour)
        if all(isinstance(i,bool) for i in bool_atteignable):
            print("L'instance est atteignable")
        else:
            print("L'instance n'est pas atteignable")
else:
    print("Usage : bruteforce.py <chemin_de_la_base>")


