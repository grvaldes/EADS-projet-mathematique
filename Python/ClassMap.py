from map_generating_functions import generate_map
from import_tsplib import import_tsplib
import numpy as np
import pandas as pd

# Classe pour représenter le réseau de villes
# Membres: - matrix : matrice de distance entre villes
#          - cities : liste des objets type Ville dans la réseau
#          - first : indice de la première ville
#          - current : indice de la ville actuelle pendant l'algorithme
#          - visit_order : liste d'indices des villes parcourues
#          - total_distance : distance totale parcouru
#          - visited : liste de booleans pour marquer les villes déjà visitées
#
# Méthodes: - add_visited_city(index) : ajoute un ville visité dans la liste visit_ordre
#                                       et change l'indice actuel
class Map():
	def __init__(self, file = None, n_cities = 10, min_dist = 10, max_dist = 100, index_first = 0):
		# On vérifie si un fichier à été donné. Si oui, on importe le fichier.
  		# Si non, on genere un matrice de distance aléatoire.
		if file == None:
			self.matrix = generate_map(n_cities, min_dist, max_dist, export = False)
		else:
			if file.split('.')[-1] == "csv":
				self.matrix = pd.read_csv(file, index_col=0).to_numpy()
			elif file.split('.')[-1] == "tsp":
				self.matrix, self.coords = import_tsplib(file)
			 
		# On crée les villes dans le réseau et les ajoute à la liste.
		self.cities = []
		
		for i in np.arange(self.matrix.shape[0]):
			self.cities.append(City(self.matrix[i,:], i))
		
		# On marque la première ville dans le réseau. Par défaut est la première ville
		# ajoutée, mais on peut choisir.
		self.first = index_first
		self.current = index_first
		self.visit_order = [index_first]
		self.total_distance = 0
		self.visited = [c.visited for c in self.cities]
		self.visited[self.first] = True
		
	# Méthode pour ajouter les villes dans la liste ordonnée.
	def add_visited_city(self, index):
		self.visit_order.append(index)
		self.current = index


# Classe pour représenter une ville
# Membres: - visited : boolean pour marque si la ville est déjà visitée
#          - index : indice de la ville (indice de la file de la matrice de distance)
#          - neighbors : liste d'indices des voisins
#          - distances : distance vers les voisins
#
# Méthodes: - is_visited() : retourne self.visited
#           - mark_visited() : marque la ville comme visitée
class City():
	def __init__(self, row, index):
		self.visited = False
		self.index = index
		self.neighbors = np.nonzero(row)[0]
		self.distances = row[self.neighbors]
		
	def is_visited(self):
		return self.visited
	
	def mark_visited(self):
		self.visited = True
		
	