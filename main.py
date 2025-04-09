import random
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

# --- Configuration des couleurs ---
COLOR_KPI = '#FFA07A'  # Orange
COLOR_REF = '#E2789F'  # Rose bonbon
COLOR_CRITICAL = '#FF6B6B'  # Rouge pour les indicateurs critiques


# --- Partie 1 : Génération des données ---
def generer_donnees_logistiques():
    """Génère des données logistiques simulées avec cohérence interne"""
    return {
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


# --- Partie 2 : Calcul des KPI ---
def calculer_kpi(data):
    """Calcule les indicateurs clés de performance"""
    return {
        'Taux livraison à temps': (data['commandes_livrees_a_temps'] / data['commandes']) * 100,
        'Taux commandes parfaites': (data['commandes_parfaites'] / data['commandes']) * 100,
        'Rotation des stocks': data['cout_biens_vendus'] / data['stock_moyen'],
        'Coût transport/tonne': data['cout_total_transport'] / data['tonnage_total'],
        'Taux fiabilité fournisseurs': sum(data['delais_fournisseurs']) / len(data['delais_fournisseurs']) * 100,
        'Marge brute': (1 - (data['cout_biens_vendus'] / data['ventes_net'])) * 100
    }


# --- Partie 3 : Analyse critique ---
def analyser_performance(kpi):
    """Identifie les points critiques et génère des recommandations"""
    references = {
        'Taux livraison à temps': 85,
        'Taux commandes parfaites': 80,
        'Rotation des stocks': 3.75,
        'Coût transport/tonne': 50,
        'Taux fiabilité fournisseurs': 80,
        'Marge brute': 22
    }

    # 1. Identification des indicateurs critiques
    critiques = []
    for nom, valeur in kpi.items():
        ecart = valeur - references[nom]
        if ecart < -5:  # Seuil à 5% en dessous de la référence
            critiques.append({
                'indicateur': nom,
                'valeur': valeur,
                'reference': references[nom],
                'ecart': abs(ecart)
            })

    # 2. Recommandations génériques
    recommandations = [
        "Optimiser les routes de livraison et renégocier les contrats transport",
        "Mettre en place un système de suivi des fournisseurs avec indicateurs clés",
        "Réaliser une analyse ABC des stocks pour améliorer la rotation",
        "Automatiser les processus de commande pour réduire les erreurs",
        "Négocier des remises volume avec les principaux fournisseurs"
    ]

    return critiques, recommandations


# --- Partie 4 : Visualisation complète ---
def visualisation_complete(kpi):
    """Génère le graphique radar et l'analyse complète"""
    # Configuration
    categories = ['Livraison\ntemps', 'Commandes\nparfaites', 'Rotation\nstocks',
                  'Coût\ntransport', 'Fiabilité\nfourn.', 'Marge\nbrute']
    references = {
        'Taux livraison à temps': 85,
        'Taux commandes parfaites': 80,
        'Rotation des stocks': 3.75,
        'Coût transport/tonne': 50,
        'Taux fiabilité fournisseurs': 80,
        'Marge brute': 22
    }

    # Préparation données radar
    kpi_values = [kpi['Taux livraison à temps'] / 100,
                  kpi['Taux commandes parfaites'] / 100,
                  kpi['Rotation des stocks'] / 4,
                  1 - (kpi['Coût transport/tonne'] - 40) / 30,
                  kpi['Taux fiabilité fournisseurs'] / 100,
                  kpi['Marge brute'] / 30]

    ref_values = [references['Taux livraison à temps'] / 100,
                  references['Taux commandes parfaites'] / 100,
                  references['Rotation des stocks'] / 4,
                  1 - (references['Coût transport/tonne'] - 40) / 30,
                  references['Taux fiabilité fournisseurs'] / 100,
                  references['Marge brute'] / 30]

    # Création figure
    plt.figure(figsize=(12, 16))

    # --- Graphique Radar ---
    ax_radar = plt.subplot2grid((5, 1), (0, 0), rowspan=3, polar=True)
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))

    kpi_values += kpi_values[:1]
    ref_values += ref_values[:1]

    ax_radar.plot(angles, kpi_values, 'o-', linewidth=2, label='Vos KPI', color=COLOR_KPI)
    ax_radar.fill(angles, kpi_values, alpha=0.25, color=COLOR_KPI)
    ax_radar.plot(angles, ref_values, 'o-', linewidth=2, label='Référence secteur', color=COLOR_REF)

    # Annotations
    for i, (angle, kpi_val, ref_val) in enumerate(zip(angles[:-1], kpi_values[:-1], ref_values[:-1])):
        ax_radar.annotate(f"{list(kpi.values())[i]:.1f}" + ('%' if i != 2 and i != 3 else ''),
                          xy=(angle, kpi_val), xytext=(10, 10), textcoords='offset points',
                          bbox=dict(boxstyle='round,pad=0.5', fc=COLOR_KPI, alpha=0.8),
                          color='white')
        ax_radar.annotate(f"{list(references.values())[i]:.1f}" + ('%' if i != 2 and i != 3 else ''),
                          xy=(angle, ref_val), xytext=(10, -20), textcoords='offset points',
                          bbox=dict(boxstyle='round,pad=0.5', fc=COLOR_REF, alpha=0.8),
                          color='white')

    ax_radar.set_thetagrids(angles[:-1] * 180 / np.pi, categories)
    ax_radar.set_ylim(0, 1)
    ax_radar.set_title('Comparaison des KPI logistiques\n', pad=20, fontsize=14)
    ax_radar.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

    # --- Analyse Textuelle ---
    ax_text = plt.subplot2grid((5, 1), (3, 0), rowspan=2)
    ax_text.axis('off')

    critiques, recommandations = analyser_performance(kpi)

    # 1. Indicateurs critiques
    text_content = "ANALYSE DES PERFORMANCES\n\n"
    text_content += "🔍 INDICATEURS CRITIQUES :\n\n"

    if critiques:
        for crit in critiques:
            text_content += (f"• {crit['indicateur']}: {crit['valeur']:.1f} vs {crit['reference']:.1f} "
                             f"(écart: -{crit['ecart']:.1f})\n")
    else:
        text_content += "Aucun indicateur critique identifié\n"

    # 2. Recommandations
    text_content += "\n💡 RECOMMANDATIONS :\n\n"
    for i, reco in enumerate(recommandations, 1):
        text_content += f"{i}. {reco}\n"

    # 3. Suggestions de visualisations
    text_content += "\n📊 VISUALISATIONS COMPLÉMENTAIRES SUGGÉRÉES :\n"
    text_content += "- Diagramme en barres comparatif par KPI\n"
    text_content += "- Graphique d'évolution temporelle des indicateurs\n"
    text_content += "- Carte thermique des écarts par rapport aux références\n"

    ax_text.text(0.02, 0.98, text_content, ha='left', va='top', fontsize=12)

    plt.tight_layout()
    plt.show()


# --- Exécution ---
def executer_analyse():
    print(f"\n{' ANALYSE LOGISTIQUE ':=^60}")
    print(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")

    data = generer_donnees_logistiques()
    kpi = calculer_kpi(data)

    print("Indicateurs calculés:")
    for nom, valeur in kpi.items():
        print(f"- {nom:<25}: {valeur:.1f}{'%' if nom != 'Coût transport/tonne' else ' €/t'}")

    visualisation_complete(kpi)


executer_analyse()
