import numpy as np
import matplotlib.pyplot as plt
import numpy as np


def polycoef(X, Y, degre):
    # Créer la matrice de Vandermonde à partir de X
    A = np.vander(X, degre + 1)

    # Résoudre l'équation A * coeffs = Y pour obtenir les coefficients du polynôme

    # Utilisation de l'inversion des moindres carrés
    coeffs, _, _, _ = np.linalg.lstsq(A, Y, rcond=None)

    return coeffs

class polynome:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __call__(self, x):
        # Évaluer le polynôme pour une ou plusieurs valeurs de x
        y = np.zeros_like(x, dtype=float)
        for i, c in enumerate(self.coeffs):
            y += c * np.power(x, len(self.coeffs) - i - 1)
        return y

# Exemple d'utilisation
X = np.array([1, 2, 3, 4, 5])
Y = np.array([1, 4, 9, 16, 25])
degre = 2

coeffs = polycoef(X, Y, degre)
print("Coefficients:", coeffs)



# Exemple d'utilisation
p = polynome(coeffs)

# Évaluer le polynôme pour une gamme de valeurs de X
X_test = np.array([1, 2, 3, 4, 5])
Y_test = p(X_test)
print("Valeurs prédictes:", Y_test)
# Calcul de la MSE
def calculate_mse(Y, Y_test):
    return np.mean((Y - Y_test) ** 2)

# Exemple d'utilisation
mse = calculate_mse(Y, Y_test)
print("Erreur quadratique moyenne (MSE):", mse)