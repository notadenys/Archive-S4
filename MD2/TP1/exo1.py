from graphe_V1 import *


G = graphe_t()
for i in range(15):
    G.ajouter_sommet(1)

for s in G.sommets:
        print(s.id)

G.ajouter_arete(0, 1)
G.ajouter_arete(0, 5)
G.ajouter_arete(1, 2)
G.ajouter_arete(1, 6)
G.ajouter_arete(2, 5)
G.ajouter_arete(2, 7)
G.ajouter_arete(3, 2)
G.ajouter_arete(3, 4)
G.ajouter_arete(3, 8)
G.ajouter_arete(4, 5)
G.ajouter_arete(4, 9)
G.ajouter_arete(5, 6)
G.ajouter_arete(5, 9)
G.ajouter_arete(6, 7)
G.ajouter_arete(8, 5)
G.ajouter_arete(8, 9)
G.ajouter_arete(9, 7)
G.ajouter_arete(9, 10)
G.ajouter_arete(10, 8)
G.ajouter_arete(11, 12)
G.ajouter_arete(12, 13)
G.ajouter_arete(13, 14)

print("\nDFS")
DFS(G,0)

print("\nBFS")
BFS(G,0)
