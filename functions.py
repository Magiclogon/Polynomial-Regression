import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('large.csv', delimiter=";")
X = data['X'].astype(float).values.reshape(-1, 1)
y = data['Y'].astype(float).values


def create_matrix(X, order):
    matrix = np.ones((X.shape[0], 1))
    for i in range(1, order + 1):
        matrix = np.hstack((matrix, X ** i))
    return matrix


def polynomial_regression(X, y, degree):
    matrix = create_matrix(X, degree)
    alpha = np.linalg.inv(matrix.T.dot(matrix)).dot(matrix.T).dot(y)
    return alpha


def predict(X, alpha):
    matrix = create_matrix(X, len(alpha) - 1)
    return matrix.dot(alpha)


order = 10

alpha = polynomial_regression(X, y, order)
print("Model Coefficients:", alpha)

X_test = np.linspace(0, 50, 300).reshape(300, 1)
y_pred = predict(X_test, alpha)

plt.scatter(X, y)
plt.plot(X_test, y_pred)
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()



