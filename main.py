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
        'Taux livraison à temps': (data['commandes_livrees_a_temps'] / data['commandes']) * 100,
        'Taux commandes parfaites': (data['commandes_parfaites'] / data['commandes']) * 100,
        'Rotation des stocks': data['cout_biens_vendus'] / data['stock_moyen'],
        'Coût transport/tonne': data['cout_total_transport'] / data['tonnage_total'],
        'Taux fiabilité fournisseurs': sum(data['delais_fournisseurs']) / len(data['delais_fournisseurs']) * 100,
        'Marge brute': (1 - (data['cout_biens_vendus'] / data['ventes_net'])) * 100
    }
    return kpi


# --- Partie 3 : Visualisation Radar avec valeurs annotées ---
def radar_plot(kpi):
    """Génère un diagramme radar comparatif avec annotations"""
    # Configuration des données
    categories = ['Livraison\ntemps', 'Commandes\nparfaites', 'Rotation\nstocks',
                  'Coût\ntransport', 'Fiabilité\nfourn.', 'Marge\nbrute']

    # Références sectorielles (benchmarks)
    references = {
        'Taux livraison à temps': 85,
        'Taux commandes parfaites': 80,
        'Rotation des stocks': 3.75,
        'Coût transport/tonne': 50,
        'Taux fiabilité fournisseurs': 80,
        'Taux marge brute': 22
    }

    # Préparation des données
    kpi_values = [kpi['Taux livraison à temps'] / 100,
                  kpi['Taux commandes parfaites'] / 100,
                  kpi['Rotation des stocks'] / 4,
                  1 - (kpi['Coût transport/tonne'] - 40) / 30,  # Inversion échelle
                  kpi['Taux fiabilité fournisseurs'] / 100,
                  kpi['Marge brute'] / 30]

    ref_values = [references['Taux livraison à temps'] / 100,
                  references['Taux commandes parfaites'] / 100,
                  references['Rotation des stocks'] / 4,
                  1 - (references['Coût transport/tonne'] - 40) / 30,
                  references['Taux fiabilité fournisseurs'] / 100,
                  references['Taux marge brute'] / 30]

    # Configuration du graphique
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, polar=True)

    # Angles pour chaque catégorie
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))

    # Tracé des données
    kpi_values += kpi_values[:1]
    ref_values += ref_values[:1]

    # Création du radar plot
    ax.plot(angles, kpi_values, 'o-', linewidth=2, label='Vos KPI', color='#FFA07A')  # Orange
    ax.fill(angles, kpi_values, alpha=0.25, color='#FFA07A')
    ax.plot(angles, ref_values, 'o-', linewidth=2, label='Référence secteur', color='#E2789F')  # Rose foncé

    # Annotations des valeurs
    for i, (angle, kpi_val, ref_val) in enumerate(zip(angles[:-1], kpi_values[:-1], ref_values[:-1])):
        # Annotation des KPI
        ax.annotate(f"{list(kpi.values())[i]:.1f}" + ('%' if i != 2 and i != 3 else ''),
                    xy=(angle, kpi_val), xytext=(10, 10), textcoords='offset points',
                    bbox=dict(boxstyle='round,pad=0.5', fc='#FFA07A', alpha=0.8),
                    color='white')

        # Annotation des références
        ax.annotate(f"{list(references.values())[i]:.1f}" + ('%' if i != 2 and i != 3 else ''),
                    xy=(angle, ref_val), xytext=(10, -20), textcoords='offset points',
                    bbox=dict(boxstyle='round,pad=0.5', fc='#E2789F', alpha=0.8),
                    color='white')

    # Personnalisation
    ax.set_thetagrids(angles[:-1] * 180 / np.pi, categories)
    ax.set_ylim(0, 1)
    ax.set_rgrids([0.2, 0.4, 0.6, 0.8], angle=45)
    plt.title('Comparaison des KPI logistiques avec les références sectorielles\n(valeurs affichées en chiffres)',
              y=1.15, fontsize=14)
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
    formatted_kpi = {
        'Taux livraison à temps': f"{kpi['Taux livraison à temps']:.1f}%",
        'Taux commandes parfaites': f"{kpi['Taux commandes parfaites']:.1f}%",
        'Rotation des stocks': f"{kpi['Rotation des stocks']:.2f}",
        'Coût transport/tonne': f"{kpi['Coût transport/tonne']:.2f} €/t",
        'Taux fiabilité fournisseurs': f"{kpi['Taux fiabilité fournisseurs']:.1f}%",
        'Marge brute': f"{kpi['Marge brute']:.1f}%"
    }

    for nom, valeur in formatted_kpi.items():
        print(f"- {nom:<25}: {valeur:>10}")

    # 4. Visualisation radar
    radar_plot(kpi)


# Lancement de l'analyse
analyse_complete()
