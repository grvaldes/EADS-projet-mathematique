import random
import math
import matplotlib.pyplot as plt

# Générer villes

def gen_villes(n, largeur = 100, hauteur = 100, seed = 42):
    random.seed(seed)
    return [(random.uniform(0, largeur), random.uniform(0, hauteur)) for _ in range(n)]

# Calcul distances

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def constr_matrice_distances(villes):
    n = len(villes)
    matrice = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(villes[i], villes[j])
            matrice[i][j] = d
            matrice[j][i] = d
    return matrice


# Heuristique d'Insertion

def heuristique_insert(villes, matrice_distances):
    
    n = len(villes)
    non_visitees = list(range(n))
    
    chemin = non_visitees[:3]
    non_visitees = non_visitees[3:]
    chemin.append(chemin[0])  # fermer le cycle

    while non_visitees:
        meilleur_cout = float('inf')
        meilleure_ville = None
        meilleure_position = None

        for ville in non_visitees:
            for i in range(1, len(chemin)):
                a = chemin[i - 1]
                b = chemin[i]
                cout = (
                    matrice_distances[a][ville] +
                    matrice_distances[ville][b] -
                    matrice_distances[a][b]
                )
                if cout < meilleur_cout:
                    meilleur_cout = cout
                    meilleure_ville = ville
                    meilleure_position = i

        chemin.insert(meilleure_position, meilleure_ville)
        non_visitees.remove(meilleure_ville)

    distance_totale = 0.0
    for i in range(len(chemin) - 1):
        distance_totale += matrice_distances[chemin[i]][chemin[i + 1]]

    return chemin, distance_totale


# Affichage du chemin

def afficher_chemin(villes, chemin):
    x = [villes[i][0] for i in chemin]
    y = [villes[i][1] for i in chemin]

    plt.figure(figsize=(10, 8))
    plt.plot(x, y, 'o-')
    for i, idx in enumerate(chemin):
        plt.text(villes[idx][0], villes[idx][1], str(idx), fontsize=9, ha='right')
    plt.title("Heuristique d'Insertion")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()

villes = gen_villes(20)
matrice = constr_matrice_distances(villes)
chemin, distance_totale = heuristique_insert(villes, matrice)

print("Distance totale :", round(distance_totale, 2))
afficher_chemin(villes, chemin)
