import numpy as np
import numbers

# Fonction pour importer des réseaux de villes en format tsp. Les fichiers sont
# la propriété intellectuelle de l'Université de Heidelberg :
# http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/
# Entrées: - filename : nom de fichier a importer
# Sorties: - dist_matrix : matrice de distances entre villes
#          - coords : coordonnées des villes
def import_tsplib(filename):
    coords = []
    
    # On vérifie chaque ligne du fichier. Si commence par un nombre,
    # on importe la coordonnée de la ville i.
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            parts = line.split()
            
            if isinstance(parts[0], numbers.Number):
                coords.append([float(parts[1]), float(parts[2])])
            elif line == "EOF":
                break

    coords = np.array(coords)
    dist_matrix = np.zeros((len(coords), len(coords)))
    
    # On calcule la distance euclidienne entre deux villes 
    # et remplit la matrice des distances.
    for i in range(len(coords)):
        for j in range(len(coords)):
            if i != j:
                dist_matrix[i,j] = np.linalg.norm(coords[i,:] - coords[j,:])
                
    return dist_matrix, coords