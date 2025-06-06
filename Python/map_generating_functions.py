import random
import numpy as np
import pandas as pd

def generate_map(n_cities = 10, percentage = 1, symmetric = True, min_dist = 10, max_dist = 100, export = True, file = "matrix.csv"):
  matrix = np.zeros((n_cities, n_cities), dtype=int)

  for i in range(n_cities):
      for j in range(i + 1, n_cities) if symmetric else range(n_cities):
          if i == j:
              continue
          if random.random() <= percentage:
              dist = random.randint(min_dist, max_dist)
              matrix[i][j] = dist
              if symmetric:
                  matrix[j][i] = dist
          elif not symmetric:
              matrix[i][j] = 0

  if export:
    df = pd.DataFrame(matrix)
    city_labels = [f'City{i}' for i in range(len(matrix))]
    df.index = city_labels
    df.columns = city_labels
    df.to_csv(file)
  else:
    return matrix