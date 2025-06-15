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
    a, b = sorted(random.sample(range(1, len(chemin) - 1), 2))
    voisin = chemin[:a] + chemin[a:b][::-1] + chemin[b:]
    return voisin


# Recuit simulé

def recuit_simule(matrice_distances, chemin_initial, temperature_initiale=15000, alpha=0.9995, iterations_max=50000): # Chemin initial = heuristique de départ, temp. initiale = contrôle la proba. d'accepter des mauvaises solutions, alpha = diminue la temp.
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

villes = generer_villes(20)
matrice = construire_matrice_distances(villes)
chemin_init, _ = heuristique_insertion(villes, matrice)
# Utilisation du chrono 
start_rs = perf_counter()
chemin_rs, distance_rs = recuit_simule(matrice, chemin_init)
end_rs = perf_counter()
time_rs = end_rs - start_rs
print("Distance après recuit simulé :", round(distance_rs, 2))
print("Temps de calcul :", round(time_rs, 6), "secondes")
distance_init = longueur_chemin(chemin_init, matrice)
# Compare les distances pour vérifier que le recuit a fonctionné
if round(distance_rs, 2) >= round(distance_init, 2):
    print("Le recuit n’a pas amélioré la distance.")
else:
    print("Le recuit a amélioré la distance.")

afficher_chemin(villes, chemin_rs)
