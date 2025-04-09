import random
from datetime import datetime

# Configuration de la graine aléatoire pour reproductibilité
random.seed(42)


def generer_donnees_logistiques():
    """Génère des données logistiques simulées avec cohérence interne"""

    # Génération des valeurs de base
    commandes = random.randint(450, 550)
    taux_livraison = random.uniform(0.75, 0.90)
    commandes_livrees = int(commandes * taux_livraison)

    ventes_net = random.randint(550000, 650000)
    marge_brute = random.uniform(0.65, 0.75)
    cout_biens_vendus = int(ventes_net * (1 - marge_brute))

    # Calculs liés au stock
    rotation_stock = random.uniform(3.5, 4.5)
    stock_moyen = int(cout_biens_vendus / rotation_stock)

    # Métriques qualité
    taux_commandes_parfaites = random.uniform(0.70, 0.85)
    commandes_parfaites = int(commandes * taux_commandes_parfaites)

    # Données transport
    tonnage_total = random.randint(1300, 1700)
    cout_tonne = random.randint(45, 55)
    cout_transport = tonnage_total * cout_tonne

    # Fiabilité fournisseurs
    delais_fournisseurs = [random.random() < 0.7 for _ in range(10)]

    return {
        'date_generation': datetime(2025, 4, 9).strftime("%A, %d %B %Y, %I:%M %p %Z"),
        'commandes': commandes,
        'commandes_livrees_a_temps': commandes_livrees,
        'stock_moyen': stock_moyen,
        'ventes_net': ventes_net,
        'cout_biens_vendus': cout_biens_vendus,
        'taux_possession': round(random.uniform(0.2, 0.3), 2),
        'commandes_parfaites': commandes_parfaites,
        'cout_total_transport': cout_transport,
        'tonnage_total': tonnage_total,
        'delais_livraisons_fournisseurs': delais_fournisseurs
    }


# Exemple d'utilisation
donnees = generer_donnees_logistiques()

# Affichage formaté des résultats
print("Données générées le :", donnees['date_generation'])
print("\n=== Structure de données ===")
for key, value in donnees.items():
    if key != 'date_generation':
        print(f"{key}: {value}")
