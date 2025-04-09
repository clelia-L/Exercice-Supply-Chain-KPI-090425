import random
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


# --- Partie 1 : Génération des données ---
def generer_donnees_logistiques():
    """Génère des données logistiques simulées avec cohérence interne"""
    data = {
        'commandes': random.randint(480, 520),
        'commandes_livrees_a_temps': random.randint(400, 450),
        'stock_moyen': random.randint(115000, 125000),
        'ventes_net': random.randint(580000, 620000),
        'cout_biens_vendus': random.randint(430000, 470000),
        'commandes_parfaites': random.randint(370, 400),
        'cout_total_transport': random.randint(70000, 80000),
        'tonnage_total': random.randint(1450, 1550),
        'delais_fournisseurs': [random.random() < 0.7 for _ in range(10)]
    }
    return data


# --- Partie 2 : Calcul des KPI ---
def calculer_kpi(data):
    """Calcule les indicateurs clés de performance"""
    kpi = {
        'Taux livraison à temps': f"{(data['commandes_livrees_a_temps'] / data['commandes']) * 100:.1f}%",
        'Taux commandes parfaites': f"{(data['commandes_parfaites'] / data['commandes']) * 100:.1f}%",
        'Rotation des stocks': f"{data['cout_biens_vendus'] / data['stock_moyen']:.2f}",
        'Coût transport/tonne': f"{data['cout_total_transport'] / data['tonnage_total']:.2f} €/t",
        'Taux fiabilité fournisseurs': f"{sum(data['delais_fournisseurs']) / len(data['delais_fournisseurs']) * 100:.1f}%",
        'Marge brute': f"{(1 - (data['cout_biens_vendus'] / data['ventes_net'])) * 100:.1f}%"
    }
    return kpi


# --- Partie 3 : Visualisation Radar ---
def radar_plot(kpi):
    """Génère un diagramme radar comparatif"""
    # Configuration des données
    categories = ['Livraison\ntemps', 'Commandes\nparfaites', 'Rotation\nstocks',
                  'Coût\ntransport', 'Fiabilité\nfourn.', 'Marge\nbrute']

    # Extraction et normalisation des valeurs
    valeurs = [
        float(kpi['Taux livraison à temps'].strip('%')) / 100,
        float(kpi['Taux commandes parfaites'].strip('%')) / 100,
        float(kpi['Rotation des stocks']) / 4,  # Normalisation
        1 - (float(kpi['Coût transport/tonne'].split()[0]) - 40) / 30,  # Inversion échelle
        float(kpi['Taux fiabilité fournisseurs'].strip('%')) / 100,
        float(kpi['Marge brute'].strip('%')) / 30  # Normalisation
    ]

    references = [0.85, 0.80, 0.75, 0.70, 0.80, 0.25]  # Benchmarks sectoriels

    # Configuration du graphique
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, polar=True)

    # Angles pour chaque catégorie
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))

    # Tracé des données
    valeurs += valeurs[:1]
    references += references[:1]

    ax.plot(angles, valeurs, 'o-', linewidth=2, label='Vos KPI')
    ax.fill(angles, valeurs, alpha=0.25)
    ax.plot(angles, references, 'o-', linewidth=2, label='Référence secteur', color='green')

    # Personnalisation
    ax.set_thetagrids(angles[:-1] * 180 / np.pi, categories)
    ax.set_ylim(0, 1)
    ax.set_rgrids([0.2, 0.4, 0.6, 0.8], angle=45)
    plt.title('Comparaison des KPI logistiques\navec les références sectorielles', y=1.1)
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()
    plt.show()


# --- Partie 4 : Exécution complète ---
def analyse_complete():
    """Exécute l'ensemble du processus"""
    # 1. Génération des données
    data = generer_donnees_logistiques()

    # 2. Calcul des KPI
    kpi = calculer_kpi(data)

    # 3. Affichage console
    print(f"\n{' KPI LOGISTIQUES ':=^60}")
    print(f"Date d'analyse: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")

    print("Principaux indicateurs:")
    for nom, valeur in kpi.items():
        print(f"- {nom:<25}: {valeur:>10}")

    # 4. Visualisation radar
    radar_plot(kpi)


# Lancement de l'analyse
analyse_complete()
