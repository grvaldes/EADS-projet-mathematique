import random
import math
import matplotlib.pyplot as plt

# Longueur d’un chemin
# Calcul la somme des distances entre chaque ville
def longueur_chemin(chemin, matrice_distances):
    return sum(
        matrice_distances[chemin[i]][chemin[i + 1]]
        for i in range(len(chemin) - 1)
    )


# Génération d’un voisin

def gen_voisin(chemin):
   
    a, b = random.sample(range(1, len(chemin) - 2), 2) # CHoisit deux positions aléatoires 
    voisin = chemin[:]
    voisin[a], voisin[b] = voisin[b], voisin[a] # On échange les deux villes
    return voisin


# Recuit simulé

def recuit_simule(matrice_distances, chemin_initial, temperature_initiale=5000, alpha=0.999, iterations_max=20000): # Chemin initial = heuristique de départ, temp. initiale = contrôle la proba. d'accepter des mauvaises solutions, alpha = diminue la temp.
    courant = chemin_initial[:] # On copie le chemin actuel
    meilleur = courant[:] # Meilleure solution 
    distance_courante = longueur_chemin(courant, matrice_distances)
    meilleure_distance = distance_courante
    temperature = temperature_initiale

    for _ in range(iterations_max):
        voisin = gen_voisin(courant) # Génère une solution voisine
        distance_voisin = longueur_chemin(voisin, matrice_distances)
        delta = distance_voisin - distance_courante

        if delta < 0 or random.random() < math.exp(-delta / temperature): # Si la solution est meilleure, on l'accepte sinon, on peut l'accepter selon la température
            courant = voisin
            distance_courante = distance_voisin
            if distance_voisin < meilleure_distance:
                meilleur = voisin
                meilleure_distance = distance_voisin

        temperature *= alpha # On réduit la température
        if temperature < 1e-3:
            break # On arrête si la température est trop basse

    return meilleur, meilleure_distance


# Affichage du chemin

def afficher_chemin(villes, chemin):
    x = [villes[i][0] for i in chemin]
    y = [villes[i][1] for i in chemin]

    plt.figure(figsize=(10, 8))
    plt.plot(x, y, 'o-')
    for i, idx in enumerate(chemin):
        plt.text(villes[idx][0], villes[idx][1], str(idx), fontsize=9, ha='right')
    plt.title("Recuit Simulé")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.axis("equal")
    plt.show()


chemin_rs, distance_rs = recuit_simule(matrice, chemin_initial)
print("Distance après recuit simulé :", round(distance_rs, 2))
if chemin_rs == chemin_initial:
    print("Le recuit n’a rien amélioré.")
else:
    print("Le chemin a été amélioré.")

afficher_chemin(villes, chemin_rs)
