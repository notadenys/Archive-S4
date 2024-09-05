class sommet_t:
    def __init__(self, val):
        global ID
        self.couleur = 0#0 = blanc, 1 = gris, 2 = noir
        self.val = val;  #Pur affichage, ne sert à rien
        self.id = ID; #Les id commencent à 0
        ID+=1

class graphe_t:
    def __init__(self):
        global ID  #Initialise l'ID des sommets à chaque graphe : attention ne pas intercaler la création de deux graphes
        ID = 0
        self.sommets = []
        self.succs = [[]]

    def ajouter_sommet(self,val):
        """Entrée : un entier, la valeur d'affichage d'un graphe
        Ajoute un graphe, avec la plus petite ID disponible (si le graphe contient les sommets d'id 0,1,2,3, il ajoutera un sommet d'id 4)"""
        self.sommets += [sommet_t(val)]
        self.succs += [[]]

    def ajouter_arete(self, id1, id2):
        """Entrée : deux entiers, des id de sommets existant
        Ajoute l'arête entre les sommets d'id id1 et id2. Arête orienté"""
        self.succs[id1].append(self.sommets[id2])

    def get_sommet_by_id(self,id):
        """Entrée : un entier, un id de sommet existant
        Sortie : le sommet correspondant à l'id"""
        return self.sommets[id]

    def get_sommets(self):
        """Entrée : rien
        Sortie: liste de sommet_t
        renvoie la liste des sommets (pas des id, des sommet_t)"""
        return self.sommets

    def get_aretes(self):
        """Entrée : rien
        Sortie : liste de couples {sommet_t, sommet_t}
        Renvoie la liste des arêtes sous forme de couple de sommet_t"""
        aretes = []
        for v in self.sommets:
            for w in self.succs[v.id]:
                aretes += [[v,w]]
        return aretes


def DFS(G,id):
    """Entrée : un graphe_t et un entier, l'id d'un sommet
    Sortie : rien
    Effectue un DFS"""
    #On fixe les couleurs à blanc
    for v in G.sommets:
        v.couleur = 0

    P = [G.get_sommet_by_id(id)]

    #Tant qu'il reste des gris
    while len(P) > 0:
        s = P.pop(len(P)-1) #le premier de la liste : pop lit et enlève
        for g in G.succs[s.id]:#On ajoute tous les successeurs blands
            if g.couleur == 0:
                g.couleur = 1#coloriage en gris
                P.append(g)

        s.couleur = 2#Coloriage en noir et ajout dans la liste des noirs

        if len(P) == 0:#Parcours complet : si la pile est vide mais qu'il reste des sommets blancs, on en ajoute un.
            for v in G.get_sommets():
                if v.couleur == 0:
                    print("|")
                    P.append(v)
                    break
    





G = graphe_t()
for i in range(0,9):
    G.ajouter_sommet(i)

G.ajouter_arete(0,1)
G.ajouter_arete(0,3)
G.ajouter_arete(1,2)
G.ajouter_arete(2,5)
G.ajouter_arete(5,4)
G.ajouter_arete(4,1)
G.ajouter_arete(3,4)
G.ajouter_arete(3,6)
G.ajouter_arete(6,0)
G.ajouter_arete(7,8)

N = DFS(G,0)

print(N)
