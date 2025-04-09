import random
from datetime import datetime


def generer_et_afficher_kpi():
    """Génère des données logistiques et affiche les KPI sous forme de ratios/percentages"""

    # Génération des données de base (simulées)
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

    # Calcul des KPI
    kpi = {
        'Taux livraison à temps': f"{(data['commandes_livrees_a_temps'] / data['commandes']) * 100:.1f}%",
        'Taux commandes parfaites': f"{(data['commandes_parfaites'] / data['commandes']) * 100:.1f}%",
        'Rotation des stocks': f"{data['cout_biens_vendus'] / data['stock_moyen']:.2f}",
        'Coût transport/tonne': f"{data['cout_total_transport'] / data['tonnage_total']:.2f} €/t",
        'Taux fiabilité fournisseurs': f"{sum(data['delais_fournisseurs']) / len(data['delais_fournisseurs']) * 100:.1f}%",
        'Marge brute': f"{(1 - (data['cout_biens_vendus'] / data['ventes_net'])) * 100:.1f}%"
    }

    # Affichage formaté
    print(f"\n{' KPI LOGISTIQUES ':=^60}")
    print(f"Date d'analyse: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")

    print("Principaux indicateurs:")
    for nom, valeur in kpi.items():
        print(f"- {nom:<25}: {valeur:>10}")

    print("\n" + " Détails des calculs ".center(60, '-'))
    print(f"Commandes totales: {data['commandes']}")
    print(f"Commandes livrées à temps: {data['commandes_livrees_a_temps']}")
    print(f"Commandes parfaites: {data['commandes_parfaites']}")
    print(f"Fiabilité fournisseurs: {sum(data['delais_fournisseurs'])}/10 livraisons dans les temps")


# Exécution
generer_et_afficher_kpi()