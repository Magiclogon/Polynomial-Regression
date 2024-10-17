import importlib.util
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger dynamiquement le module test1.py
path_to_test1 = r'C:\Users\HP\Desktop\prj\test1.py'
spec = importlib.util.spec_from_file_location("test1", path_to_test1)
test1 = importlib.util.module_from_spec(spec)
sys.modules["test1"] = test1
spec.loader.exec_module(test1)

# Maintenant, vous pouvez utiliser les fonctions et classes de test1.py
polycoef = test1.polycoef
polynome = test1.polynome

# Spécifiez le chemin du fichier Excel
fichier_excel = r"C:\Users\HP\Desktop\prj\test.xlsx"

# Importer le fichier Excel
df = pd.read_excel(fichier_excel)

# Afficher les premières lignes du fichier pour vérifier l'importation
print(df.head())

# Transformer le DataFrame en array NumPy
array_numpy = df[['tempurature', 'effective']].to_numpy()

# Séparer les catégories et les valeurs
categories = array_numpy[:, 0]  # Colonne des catégories
valeurs = array_numpy[:, 1].astype(float)  # Colonne des valeurs (en tant que float)

print(array_numpy)
print(categories)
print(valeurs)

# Créer un graphique à bâtons
plt.stem(categories, valeurs, basefmt=" ", use_line_collection=True, linefmt='b-', markerfmt='bo')

# Ajouter des annotations pour les valeurs au-dessus de chaque bâton
for i in range(len(valeurs)):
    plt.annotate(f'{valeurs[i]:.0f}',  # Valeur sans décimale
                 xy=(categories[i], valeurs[i]),  # Position du texte au sommet du bâton
                 xytext=(0, 3),  # Décalage vertical pour que le texte soit au-dessus des bâtons
                 textcoords="offset points",  # Coordonnées relatives
                 ha='center', va='bottom', fontsize=10, fontweight='bold')  # Style du texte

# Ajouter un titre et des étiquettes avec des polices plus grandes et plus claires
plt.title('Statistiques par Catégorie (Graphique à Bâtons)', fontsize=16, fontweight='bold')
plt.xlabel('Température', fontsize=14)
plt.ylabel('Valeur', fontsize=14)

# Personnaliser les graduations (ticks) des axes
plt.xticks(fontsize=12, fontweight='bold')
plt.yticks(fontsize=12)

# Supprimer les bordures superflues pour un style plus épuré
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Afficher une grille légère sur l'axe Y pour améliorer la lisibilité
plt.grid(axis='y', linestyle='--', alpha=0.7)

# === Tracer le polynôme ===
# Ajustement polynomial de degré n
n = int(input("Taper le degré du polynome n = "))
poly = polynome(polycoef(categories, valeurs, n))

# Générer des points pour tracer le polynôme lissé
x_poly = np.linspace(min(categories), max(categories), 500)
y_poly = poly(x_poly)

# Tracer le polynôme sur le même graphique
plt.plot(x_poly, y_poly, color='red', linestyle='-', linewidth=2, label=f'Ajustement Polynomial (deg={n})')

# Ajouter une légende pour indiquer la courbe polynomiale
plt.legend()

# Afficher le graphique final
plt.tight_layout()
plt.show()




