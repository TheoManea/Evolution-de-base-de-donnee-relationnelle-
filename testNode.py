
class noeud:
    def __init__(self,valeur):
        self.valeur = valeur
        self.fils = []
        self.pere = None

    def set_pere(self,papa):
        self.pere = papa


class SolveProblem:

    def __init__(self,init,objectif,val):
        self.init = init
        self.objectif = objectif
        self.vals_poss = val

    def printNTree(self,x,flag,depth,isLast):
        if x == None:
            return
           
        for i in range(1, depth):
            if flag[i]:
                print("| ","", "", "", end = "")
               
            else:
                print(" ", "", "", "", end = "")
           
        if depth == 0:
            print(x.valeur)
           
        elif isLast:
            print("+---", x.valeur)
               
            flag[depth] = False
        else:
            print("+---", x.valeur)
       
        it = 0
        for i in x.fils:
            it+=1
           
            self.printNTree(i, flag, depth + 1, it == (len(x.fils) - 1))
        flag[depth] = True

    def construit_chemin(self,noeud_atteint):

        chemin = []

        try:
            chemin.append(noeud_atteint.valeur)
            dad = noeud_atteint.pere

            while dad.pere is not None:

                chemin.append(dad.valeur)
                dad = dad.pere
            
            chemin.append(dad.valeur)
            chemin.reverse()

            path = ""

            for noeud in chemin:
                path+=f"->{noeud}"

            print(path)

        except:
            print("Erreur ici")
        

    def construitArbre(self,init,objectif,vals_poss):

        hauteur = 1 
        fac_br = len(vals_poss)
        val_calcule = [init]
        noeud_liste = []
        racine = noeud(init)
        noeud_liste.append(racine)

        atteint = False
        noeud_succes = None
        poursuite = True

        i = 0

        while poursuite:

            val_sur_une_prof = []

            if(hauteur - 2 <= 0):

                    if hauteur == 1:

                        for val in vals_poss:
                            tmp = init - val 
                            tmp_noeud = noeud(tmp)
                            tmp_noeud.set_pere(noeud_liste[0])
                            val_calcule.append(tmp)
                            val_sur_une_prof.append(tmp)
                            noeud_liste[0].fils.append(tmp_noeud)
                            noeud_liste.append(tmp_noeud)

                            if tmp == objectif and atteint == False:
                                atteint = True
                                noeud_succes = tmp_noeud
                
                    elif hauteur == 2:

                        for i in range(1,3):
                        
                            for val in vals_poss:
                                tmp = val_calcule[i] - val
                                tmp_noeud = noeud(tmp)
                                tmp_noeud.set_pere(noeud_liste[i])
                                val_calcule.append(tmp)
                                val_sur_une_prof.append(tmp)
                                noeud_liste[i].fils.append(tmp_noeud)
                                noeud_liste.append(tmp_noeud)

                                print(tmp)

                                if tmp == objectif and atteint == False:
                                    atteint = True
                                    noeud_succes = tmp_noeud
            else:

                nb_noeud_dev_avant_pere = fac_br**(hauteur-1) - 1 
                inf = nb_noeud_dev_avant_pere 
                sup = len(val_calcule) 

                for val in vals_poss:

                    for i in range(inf,sup):
                        tmp = val_calcule[i] - val
                        tmp_noeud = noeud(tmp)
                        tmp_noeud.set_pere(noeud_liste[i])
                        val_calcule.append(tmp)
                        val_sur_une_prof.append(tmp)
                        noeud_liste[i].fils.append(tmp_noeud)
                        noeud_liste.append(tmp_noeud)

                        print(tmp)

                        if tmp == objectif and atteint == False:
                            atteint = True
                            noeud_succes = tmp_noeud

            hauteur+=1

            i+=1

            # on check si ça sert de continuer à chercher 
            tous_inf = all(i < self.objectif for i in val_sur_une_prof)

            if tous_inf:
                poursuite = False


        return noeud_liste,atteint,noeud_succes

    def solve(self):
        res = self.construitArbre(self.init,self.objectif,self.vals_poss)
        flag = [True]*(len(res[0])) 

        #print("===> L'arbre \n")
        #self.printNTree((res[0])[0], flag, 0, False)
        print("\n")
        print(f"Il existe un chemin qui mène à l'objectif ? {res[1]}")
        self.construit_chemin(res[2])        


if __name__ == '__main__':
    probleme = SolveProblem(2000,1700,[50,3])
    probleme.solve()