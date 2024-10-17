import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Fonction pour tracer le scatter plot à partir d'un fichier CSV
def plot_scatter(fichier_csv):
    # Importer le fichier CSV
    df = pd.read_csv(fichier_csv, sep=";")

    # Transformer le DataFrame en array NumPy pour les colonnes X et Y
    array_numpy = df[['X', 'Y']].to_numpy()

    # Séparer les catégories et les valeurs
    categories = array_numpy[:, 0]  # Colonne X (par exemple, Température)
    valeurs = array_numpy[:, 1].astype(float)  # Colonne Y (par exemple, Effectivité)

    # Créer un graphique en points
    plt.scatter(categories, valeurs, color='blue', label='Valeurs observées', s=30)  # s est la taille des points

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


def plot_stem(path_file):
    try:
        # Importer le fichier CSV
        df = pd.read_csv(path_file, sep=";")

        # Transformer le DataFrame en array NumPy pour les colonnes X et Y
        array_numpy = df[['X', 'Y']].to_numpy()

        # Séparer les catégories et les valeurs
        categories = array_numpy[:, 0]  # Colonne X (par exemple, Température)
        valeurs = array_numpy[:, 1].astype(float)  # Colonne Y (par exemple, Effectivité)

        # Convert categories to numeric if possible
        try:
            categories = categories.astype(float)  # Ensure X values are numeric
        except ValueError:
            print("Warning: X values could not be converted to numeric.")

        # Créer un graphique à bâtons sans `use_line_collection`
        plt.stem(categories, valeurs, linefmt='b-', markerfmt='bo', basefmt=' ')

        # Ajouter des annotations pour les valeurs au-dessus de chaque bâton
        for i in range(len(valeurs)):
            plt.annotate(f'{valeurs[i]:.0f}',  # Valeur sans décimale
                         xy=(categories[i], valeurs[i]),  # Position du texte au sommet du bâton
                         xytext=(0, 3),  # Décalage vertical pour que le texte soit au-dessus des bâtons
                         textcoords="offset points",  # Coordonnées relatives
                         ha='center', va='bottom', fontsize=10, fontweight='bold')  # Style du texte

        # Ajouter un titre et des étiquettes
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

    except Exception as e:
        print(f"Error while plotting: {e}")




