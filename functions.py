import threading
from turtledemo.penrose import start

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


# Fonction pour calculer les coefficients du polynôme
def polycoef(X, Y, degre):
    A = np.vander(X, degre + 1)
    coeffs, _, _, _ = np.linalg.lstsq(A, Y, rcond=None)
    return coeffs


# Classe du polynôme
class Polynome:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __call__(self, x):
        y = np.zeros_like(x, dtype=float)
        for i, c in enumerate(self.coeffs):
            y += c * np.power(x, len(self.coeffs) - i - 1)
        return y


    # Fonction pour tracer le polynôme de régression
def plot_poly(filepath, degre):
    # Importer le fichier CSV
    df = pd.read_csv(filepath, sep=";")

    # Convertir les colonnes 'X' et 'Y' en numériques, en gérant les erreurs
    df['X'] = pd.to_numeric(df['X'], errors='coerce')
    df['Y'] = pd.to_numeric(df['Y'], errors='coerce')

    # Supprimer les lignes contenant des valeurs NaN (résultat des erreurs de conversion)
    df = df.dropna(subset=['X', 'Y'])

    # Transformer le DataFrame en array NumPy pour les colonnes X et Y
    array_numpy = df[['X', 'Y']].to_numpy()
    categories = array_numpy[:, 0]  # Colonne X (par exemple, Température)
    valeurs = array_numpy[:, 1]  # Colonne Y (par exemple, Effectivité)

    # Tracer l'histogramme existant
    plt.scatter(categories, valeurs, color='blue', label='Valeurs observées', s=50)

    # Calcul des coefficients du polynôme et création du modèle
    coeffs = polycoef(categories, valeurs, degre)
    poly = Polynome(coeffs)

    # Générer les points pour le polynôme
    x_poly = np.linspace(min(categories), max(categories), 500)
    y_poly = poly(x_poly)

    # Tracer le polynôme sur le graphique
    plt.plot(x_poly, y_poly, color='red', linestyle='-', linewidth=2, label=f'Ajustement Polynomial (deg={degre})')
    plt.title('Statistiques avec Régression Polynomial', fontsize=16, fontweight='bold')
    plt.xlabel('X', fontsize=14)
    plt.ylabel('Y', fontsize=14)
    plt.legend()
    plt.tight_layout()
    plt.savefig("regression.png")
    plt.close()

    return coeffs


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
    plt.savefig('points_plot.png')
    plt.close()


# Fonction pour tracer le plit en barre.
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
        plt.savefig('batons_plot.png')
        plt.close()

    except Exception as e:
        print(f"Error while plotting: {e}")


def polynomial_regression_sklearn(csv_file, degree):

    # Avoir les données
    data = pd.read_csv(csv_file, sep=";")
    X = data[['X']].values
    Y = data['Y'].values

    # Create polynomial features
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)

    # Configurer la regression
    model = LinearRegression()
    model.fit(X_poly, Y)

    # Afficher les coeffs
    print(f"Polynomial Coefficients: {model.coef_}")
    print(f"Intercept: {model.intercept_}")

    # Plot the data points
    plt.scatter(X, Y, color='blue', label='Data Points')

    # Generer prédictions
    X_plot = np.linspace(min(X), max(X), 100).reshape(-1, 1)
    Y_plot = model.predict(poly.transform(X_plot))

    # Tracer la courbe
    plt.plot(X_plot, Y_plot, color='red', label=f'Polynomial Fit (Degree {degree})')

    # Personnaliser
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Polynomial Regression')
    plt.legend()
    plt.tight_layout()
    plt.savefig("regression.png")
    plt.close()

    coeffs = []
    coeffs = coeffs + model.coef_.tolist() + [model.intercept_]
    # Retourner les coefficients et l'intercept
    return coeffs







