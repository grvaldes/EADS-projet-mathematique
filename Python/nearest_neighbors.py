def nearest_neighbors(map):
	all_visited = False
 
	while not all_visited:
		curr_city = map.cities[map.current]
		best_distance = float('inf')
		best_neighbor_ind = None

		for neighbor_index, distance in zip(curr_city.neighbors, curr_city.distances):
			if not map.visited[neighbor_index] and distance < best_distance:
				best_distance = distance
				best_neighbor_ind = neighbor_index

		if best_neighbor_ind is None:
			print("Il n'y a plus de villes pour visiter depuis la ville {map.current}.")
			break

		map.total_distance += best_distance
		map.visit_order.append(best_neighbor_ind)
		map.visited[best_neighbor_ind] = True
		map.cities[best_neighbor_ind].visited = True
		map.current = best_neighbor_ind
		
		if all(map.visited):
			all_visited = True
   
	for i in reversed(range(len(map.cities))):
		if map.matrix[map.current][map.first] > 0:
			map.total_distance += map.matrix[map.current][map.first]
			map.visit_order.append(map.first)
			map.current = map.first
			break
		else:
			map.total_distance += map.matrix[map.current][map.visit_order[i-1]]
			map.visit_order.append(map.visit_order[i-1])
			map.current = map.visit_order[i-1]