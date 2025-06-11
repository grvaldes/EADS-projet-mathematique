def compute_total_distance(matrix, order):
    distance = 0
    
    for i in range(len(order) - 1):
        distance += matrix[order[i], order[i+1]]
        
    return distance


def two_opt(map):
    best_distance = map.total_distance
    new_order = map.visit_order[:-1]
    n = len(new_order)
    improved = True

    while improved:
        improved = False
        
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                flipped_order = new_order[:i] + new_order[i:j+1][::-1] + new_order[j+1:]
                new_distance = compute_total_distance(map.matrix, flipped_order + [flipped_order[0]])

                if new_distance < best_distance:
                    new_order = flipped_order
                    best_distance = new_distance
                    improved = True
                    break
                
            if improved:
                break

    # Finalize
    map.visit_order = new_order + [new_order[0]]
    map.total_distance = best_distance