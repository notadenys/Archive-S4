
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
        self.sommets += [sommet_t(val)];
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
    Sortie : liste des sommets noirs
    Effectue un DFS"""

    noirs = list()

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
        noirs.append(s.id)

        if len(P) == 0:#Parcours complet : si la pile est vide mais qu'il reste des sommets blancs, on en ajoute un.
            for v in G.get_sommets():
                if v.couleur == 0:
                    P.append(v)
                    break
    
    return noirs

def DFS_incomplet(G,id):
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

def DFS_ordre(G, ord):
    connexes = [[]]
    i = 0

    #On fixe les couleurs à blanc
    for v in G.sommets:
        v.couleur = 0

    P = [G.get_sommet_by_id(ord[0])]

    #Tant qu'il reste des gris
    while len(P) > 0:
        s = P.pop(len(P)-1) #le premier de la liste : pop lit et enlève
        for g in G.succs[s.id]:#On ajoute tous les successeurs blands
            if g.couleur == 0:
                g.couleur = 1#coloriage en gris
                P.append(g)

        s.couleur = 2#Coloriage en noir et ajout dans la liste des noirs
        connexes[i].append(s.id)

        if len(P) == 0:#Parcours complet : si la pile est vide mais qu'il reste des sommets blancs, on en ajoute un.
            for id in ord:
                if G.get_sommet_by_id(id).couleur == 0:
                    P.append(G.get_sommet_by_id(id))
                    connexes.append([])
                    i += 1
                    break
    
    return connexes

def isRacine(G, id) -> bool:
    for e in G.get_aretes():
        if e[1] == G.get_sommet_by_id(id):
            return False
        
    DFS_incomplet(G, id)
    for s in G.sommets:
        if s.couleur != 2:
            return False
    
    return True

def existsRacine(G) -> int:
    for v in G.sommets:
        if isRacine(G, v.id):
            return v.id
    return -1

def mirroir(G) -> graphe_t:
    Gm = graphe_t()
    for v in G.sommets:
        Gm.ajouter_sommet(v.val)
    
    for e in G.get_aretes():
        Gm.ajouter_arete(e[1].id, e[0].id)
    
    return Gm

def kosaraju(G):
    Gm = mirroir(G)
    ordre = DFS(G, 0)
    return DFS_ordre(Gm, ordre)

G = graphe_t()#Graphe sans racine
for i in range(0,6):
    G.ajouter_sommet(i)

G.ajouter_arete(0,1)
G.ajouter_arete(0,2)
G.ajouter_arete(2,4)
G.ajouter_arete(4,3)
G.ajouter_arete(3,2)

H = graphe_t()#Graphe sans racine
for i in range(0,5):
    H.ajouter_sommet(i)

H.ajouter_arete(0,1)
H.ajouter_arete(0,2)
H.ajouter_arete(2,3)
H.ajouter_arete(3,4)
H.ajouter_arete(4,0)

I = graphe_t()#Graphe avec racine
for i in range(0,5):
    I.ajouter_sommet(i)

I.ajouter_arete(0,1)
I.ajouter_arete(0,2)
I.ajouter_arete(0,3)
I.ajouter_arete(3,4)
I.ajouter_arete(4,2)

print("Racine de G : ", existsRacine(G))
print("Racine de H : ", existsRacine(H))
print("Racine de I : ", existsRacine(I))

N = graphe_t()
for i in range(0,9):
    N.ajouter_sommet(i)

N.ajouter_arete(0,1)
N.ajouter_arete(0,3)
N.ajouter_arete(1,2)
N.ajouter_arete(2,5)
N.ajouter_arete(5,4)
N.ajouter_arete(4,1)
N.ajouter_arete(3,4)
N.ajouter_arete(3,6)
N.ajouter_arete(6,0)
N.ajouter_arete(7,8)

print("Composantes fortement connexes de N : ", kosaraju(N))
