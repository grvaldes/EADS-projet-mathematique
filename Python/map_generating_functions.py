import random
import numpy as np
import pandas as pd

# Fonction pour générer matrices de distance aléatoires
# Entrées: - n_cities : nombre de villes dans la réseau
#          - min_dist : distance minimale entre deux villes
#          - max_dist : distance maximale entre deux villes
#          - export : true si l'on veux exporter la matrice dans un fichier
#          - file : nom du fichier de sortie
# Sorties: - matrix : matrice de distances
def generate_map(n_cities = 10, min_dist = 10, max_dist = 100, export = True, file = "matrix.csv"):
    matrix = np.zeros((n_cities, n_cities), dtype=int)

    # Pour chaque ville, on choisit une distance avec les autres villes
    for i in range(n_cities):
        # On assume distances symétriques, donc on parcours juste le triangle supérieur
        for j in range(i + 1, n_cities):
            dist = random.randint(min_dist, max_dist)
            matrix[i][j] = dist
            matrix[j][i] = dist

    # Si l'on veut exporter la matrice, on utilise pandas pour l'écrire dans un fichier csv
    # Si non, on retourne la matrice
    if export:
        df = pd.DataFrame(matrix)
        city_labels = [f'City{i}' for i in range(len(matrix))]
        df.index = city_labels
        df.columns = city_labels
        df.to_csv(file)
    else:
        return matrix