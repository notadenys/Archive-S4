class sommet_t:
    def __init__(self, val):
        global ID
        self.val = val
        self.id = ID
        self.successeurs = []
        self.couleur = "blanc"
        ID+=1
    
    def ajouter_succ(self, sommet):
        self.successeurs.append(sommet)

class graphe_t:
    def __init__(self):
        self.sommets = []
        global ID
        ID = 0

    def ajouter_sommet(self,val):
        self.sommets += [sommet_t(val)]

    def get_sommet_by_id(self,id) -> sommet_t:
        return self.sommets[id]

    def ajouter_arete(self, id1, id2):
        self.get_sommet_by_id(id1).ajouter_succ(self.get_sommet_by_id(id2))

def DFS(G,id):
    for a in G.sommets:
        a.couleur = "blanc"

    P = [G.get_sommet_by_id(id)]


    while len(P) > 0:
        s = P.pop(len(P)-1)
        for g in s.successeurs:
            if g.couleur == "blanc":
                g.couleur = "gris"
                print(g.id," => ", g.couleur)
                P.append(g)

        s.couleur = "noir"
        print(s.id, " => ", s.couleur)

        if len(P) == 0:
            for v in G.sommets:
                if v.couleur == "blanc":
                    P.append(v)
                    print("|")
                    break

    for somm in G.sommets:
        somm.couleur = "blanc"

def BFS(G,id):
    F = [G.get_sommet_by_id(id)]
    while len(F) > 0:
        s = F.pop(0)
        for g in s.successeurs:
            if g.couleur == "blanc":
                g.couleur = "gris"
                print(g.id," => ", g.couleur)
                F.append(g)
        s.couleur = "noir"
        print(s.id, " => ", s.couleur)

if __name__ == "__main__":
    ID = 0
    # G = graphe_t()
    # G.ajouter_sommet(1)
    # G.ajouter_sommet(3)
    # G.ajouter_sommet(3)
    # G.ajouter_sommet(3)
    # G.ajouter_sommet(3)

    # G.ajouter_arete(0,1)
    # G.ajouter_arete(1,2)
    # G.ajouter_arete(2,3)
    # G.ajouter_arete(1,4)

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

    print("Sommets")
    for s in G.sommets:
        print(s.id)

    print("DFS")
    DFS(G,0)
    print("BFS")
    BFS(G,0)
