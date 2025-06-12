# Algorithme des voisins plus proches
# Entrées: - map objet de réseau de villes
def nearest_neighbors(map):
    # On cree une variable auxiliaire que vérifie si tous les villes ont été visitées
	all_visited = False
 
	# Si l'on a pas visité tous les villes, on continue
	while not all_visited:
		# On choisit la ville actuelle
		curr_city = map.cities[map.current]
		best_distance = float('inf')
		best_neighbor_ind = None

		# On compare tous les voisins, chaque fois que la distance est inférieure, on
		# actualise le voisin
		for neighbor_index, distance in zip(curr_city.neighbors, curr_city.distances):
			if not map.visited[neighbor_index] and distance < best_distance:
				best_distance = distance
				best_neighbor_ind = neighbor_index

		# Après vérification de tous les voisins, on ajoute le voisin plus proche à
		# la liste et le marque comme visité. On met à jour l'indice actuel
		map.total_distance += best_distance
		map.visit_order.append(best_neighbor_ind)
		map.visited[best_neighbor_ind] = True
		map.cities[best_neighbor_ind].visited = True
		map.current = best_neighbor_ind
		
		# Si tous les villes sont visitées, on marque la variable comme vrai pour sortir
		# le boucle
		if all(map.visited):
			all_visited = True
   
	# Pour finir, on ajoute la première ville a la fin de la liste, pour fermer le parcours
	map.total_distance += map.matrix[map.current][map.first]
	map.visit_order.append(map.first)
	map.current = map.first