# Fonction auxiliaire pour calculer la distance parcouru
# Entrées: - matrix : matrice de distance
#          - order : ordre de visite
# Sorties: - distance : distance parcouru
def compute_total_distance(matrix, order):
    distance = 0
    
    for i in range(len(order) - 1):
        distance += matrix[order[i], order[i+1]]
        
    return distance

# Algorithme 2-opt pour optimizer voisins proches
# Entrées: - map : objet de réseau de villes
def two_opt(map):
    # On considère l'état actuel comme la solution optimale
    best_distance = map.total_distance
    new_order = map.visit_order[:-1]
    n = len(new_order)
    improved = True

    # On cherche des séquences à optimiser
    while improved:
        improved = False
        
        # À partir de chaque noeud on prendre de chaînes
        for i in range(1, n - 1):
            # Pour chaque chaîne on fait le échange avec son inverse
            for j in range(i + 1, n):
                flipped_order = new_order[:i] + new_order[i:j+1][::-1] + new_order[j+1:]
                new_distance = compute_total_distance(map.matrix, flipped_order + [flipped_order[0]])

                # Si le chemin parcouru est moins avec le chemin inversé, on le mettre à jour
                if new_distance < best_distance:
                    new_order = flipped_order
                    best_distance = new_distance
                    improved = True
                    break
                
            if improved:
                break

    # Mis a jour du réseau
    map.visit_order = new_order + [new_order[0]]
    map.total_distance = best_distance