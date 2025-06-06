from ClassMap import Map, City
from nearest_neighbors import nearest_neighbors

map = Map()
# map = Map(file="matrix.csv")
# Map.generate_map()

nearest_neighbors(map)

print(map.matrix)
print()
print()
print()
print()
print(map.visit_order)
print(map.total_distance)