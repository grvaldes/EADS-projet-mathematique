import copy
from ClassMap import Map
from two_opt import two_opt
from nearest_neighbors import nearest_neighbors
from plotting_functions import *

# map = Map()
# map = Map(file="matrix.csv")
map = Map(file="Data/berlin52.tsp")
# Map.generate_map()

print(map.matrix)

nearest_neighbors(map)
print(map.visit_order)
print(map.total_distance)

map2 = copy.deepcopy(map)

two_opt(map2)
print(map2.visit_order)
print(map2.total_distance)

fig = plt.figure(figsize=(12,6))
ax1 = plt.subplot(1,2,1)
ax2 = plt.subplot(1,2,2)
ax1.grid(True)
ax2.grid(True)
plot_directed_graph(map.coords, map.visit_order, embedded=True, axis=ax1)
plot_directed_graph(map2.coords, map2.visit_order, embedded=True, axis=ax2)
ax1.set_aspect('equal', 'box')
ax1.autoscale()
ax2.set_aspect('equal', 'box')
ax2.autoscale()
plt.show()