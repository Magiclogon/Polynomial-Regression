import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Fonction pour tracer le scatter plot à partir d'un fichier CSV
def plot_scatter(fichier_csv):
    # Importer le fichier CSV
    df = pd.read_csv(fichier_csv)

    # Transformer le DataFrame en array NumPy pour les colonnes X et Y
    array_numpy = df[['X', 'Y']].to_numpy()

    # Séparer les catégories et les valeurs
    categories = array_numpy[:, 0]  # Colonne X (par exemple, Température)
    valeurs = array_numpy[:, 1].astype(float)  # Colonne Y (par exemple, Effectivité)

    # Créer un graphique en points
    plt.scatter(categories, valeurs, color='blue', label='Valeurs observées', s=50)  # s est la taille des points

    # Ajouter un titre et des étiquettes avec des polices plus grandes et plus claires
    plt.title('Histogramme de X et Y ', fontsize=16, fontweight='bold')
    plt.xlabel('X (Variable)', fontsize=14)
    plt.ylabel('Y (Effectif)', fontsize=14)

    # Personnaliser les graduations (ticks) des axes
    plt.xticks(fontsize=12, fontweight='bold')
    plt.yticks(fontsize=12)

    # Supprimer les bordures superflues pour un style plus épuré
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    # Afficher une grille légère sur l'axe Y pour améliorer la lisibilité
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Afficher le graphique final
    plt.tight_layout()
    plt.show()




