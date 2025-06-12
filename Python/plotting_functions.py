import matplotlib.pyplot as plt

# Fonction pour dessiner un graph
# Entrées: - coords : matrice de coordonnées des villes
#          - radius : taille du point dans le graph
#          - connected : décide si l'on ajoute les lignes
#          - embedded : décide si le graph est un image indépendant
#          - axis : axe à remplir si embedded est vrai
# Sorties: - l'image du graph
def plot_graph(coords, radius=10, connected=True, embedded=False, axis=None):
    # Si l'image est indépendant on cree la figure et ses axes
    if not embedded:
        fig, axis = plt.subplots()
    
    # On ajoute chaque ville au graph
    for i in range(coords.shape[0]):
        circle = plt.Circle((coords[i,0], coords[i,1]), radius, color='blue', fill=True)
        axis.add_patch(circle)
    
        # Si connecté, on ajoute les lignes entre villes
        if connected:
            for j in range(i + 1, coords.shape[0]):
                x_values = [coords[i,0], coords[j,0]]
                y_values = [coords[i,1], coords[j,1]]
                axis.plot(x_values, y_values, color='black', linestyle='-')
    
    # Si l'image est indépendant on choisit ses propriétés
    if not embedded:
        axis.set_aspect('equal', 'box')
        axis.autoscale()
        plt.grid(True)
        plt.show()


# Fonction pour dessiner un graph orienté
# Entrées: - coords : matrice de coordonnées des villes
#          - order : ordre de parcours des villes
#          - radius : taille du point dans le graph
#          - embedded : décide si le graph est un image indépendant
#          - axis : axe à remplir si embedded est vrai
# Sorties: - l'image du graph
def plot_directed_graph(coords, order, radius=10, embedded=False, axis=None):
    # Si l'image est indépendant on cree la figure et ses axes
    if not embedded:
        fig, axis = plt.subplots()
    
    # On ajoute chaque ville au graph. La première ville on ajoute en rouge
    for i in range(coords.shape[0]):
        if i == 0:
            circle = plt.Circle((coords[i,0], coords[i,1]), radius, color='red', fill=True)
        else:
            circle = plt.Circle((coords[i,0], coords[i,1]), radius, color='blue', fill=True)
        axis.add_patch(circle)
    
    # Pour chaque ville, on ajoute une flèche connectant le parcours
    for j in range(len(order)-1):
        x_values = [coords[order[j],0], coords[order[j+1],0]]
        y_values = [coords[order[j],1], coords[order[j+1],1]]
        axis.annotate("", xytext=(coords[order[j],0], coords[order[j],1]), xy=(coords[order[j+1],0], coords[order[j+1],1]), arrowprops=dict(arrowstyle="->"))
    
    # Si l'image est indépendant on choisit ses propriétés
    if not embedded:
        axis.set_aspect('equal', 'box')
        axis.autoscale()
        plt.grid(True)
        plt.show()