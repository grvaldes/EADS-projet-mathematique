import numpy as np

def import_tsplib(filename):
    coords = []
    with open(filename, 'r') as file:
        dimension = None
        in_node_section = False

        for line in file:
            line = line.strip()
            if line.startswith("DIMENSION"):
                dimension = int(line.split(":")[1])
            elif line.startswith("NODE_COORD_SECTION"):
                in_node_section = True
            elif line == "EOF":
                break
            elif in_node_section:
                parts = line.split()
                if len(parts) >= 3:
                    coords.append([float(parts[1]), float(parts[2])])

    if len(coords) != dimension:
        raise ValueError("Mismatch between declared dimension and number of coordinates.")

    coords = np.array(coords)
    dist_matrix = np.zeros((len(coords), len(coords)))
    
    for i in range(len(coords)):
        for j in range(len(coords)):
            if i != j:
                dist_matrix[i,j] = np.linalg.norm(coords[i,:] - coords[j,:])
                
    return dist_matrix, coords