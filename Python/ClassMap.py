from map_generating_functions import generate_map
import numpy as np
import pandas as pd

class Map():
  def __init__(self, file = None, n_cities = 10, percentage = 1, symmetric = True, min_dist = 10, max_dist = 100, index_first = 0):
    if file == None:
      self.matrix = generate_map(n_cities, percentage, symmetric, min_dist, max_dist, export = False)
    else:
      self.matrix = pd.read_csv(file, index_col=0).to_numpy()
            
    self.cities = []
    
    for i in np.arange(self.matrix.shape[0]):
      self.cities.append(City(self.matrix[i,:], i))
    
    self.first = index_first
    self.current = index_first
    self.visit_order = [index_first]
    self.total_distance = 0
    self.visited = [c.visited for c in self.cities]
    self.visited[self.first] = True
    
  def add_visited_city(self, index):
    self.visit_order.append(index)
    self.current = index


class City():
  def __init__(self, row, index):
    self.visited = False
    self.index = index
    self.neighbors = np.nonzero(row)[0]
    self.distances = row[self.neighbors]
    
  def is_visited(self):
    return self.visited
  
  def closest_neighbor(self):
    ind = np.argmin(self.distances)
    return self.neighbors[ind]
  
  def mark_visited(self):
    self.visited = True
    
  