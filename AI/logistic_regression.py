import numpy as np
import matplotlib.pyplot as plt

nbr_class = 20
col = 2

def init_variables():
    weights = np.random.normal(size=col)
    bias = 0
    # print("Weights:", weights)
    return weights, bias

def get_dataset():
    # Générer des données pour la classe "malade"
    sick = -np.abs(np.random.randn(nbr_class, col))
    # Générer des données pour la classe "en bonne santé"
    healthy = np.abs(np.random.randn(nbr_class, col))
    
    # print("Données pour la classe malade:", sick)
    # print("Données pour la classe en bonne santé:", healthy)

    # Concaténer les inputs/features
    inputs = np.vstack([sick, healthy])
    
    # Créer les cibles (targets)
    targets = np.concatenate((np.zeros(nbr_class), np.zeros(nbr_class) + 1))
    
    print("Inputs (inputs):", inputs)
    print("Targets:", targets)
    return inputs, targets

def pre_activation(inputs, weights, bias):
    # Calcul de la pré-activation (somme pondérée)
    z = np.dot(inputs, weights) + bias
    # print("Pre activation:", z)
    return z

def activation(z):
    # Activation/Sigmoid
    a = 1 / (1 + np.exp(-z))
    # print("Activation:", a)
    return a

def derivative_activation(z):
    return activation(z) * (1 - activation(z))

def cost(predictions, targets):
    # cost => taux d'erreur
    return np.mean((predictions - targets) ** 2)

def predict(inputs, weights, bias):
    z = pre_activation(inputs, weights, bias)
    y = activation(z)
    p = np.round(y) # envoie soit 0 ou 1
    print("prediction:", p)
    return p


def train(inputs, targets, weights, bias):
    epochs = 100 # nombre d'entraînement
    learning_rate = 0.1 # pourcentage d'avancement vers la bonne solution

    # Print current Accuracy
    predictions = predict(inputs, weights, bias)
    print("Accuracy = %s" % np.mean(predictions == targets))

    # Plot points
    plt.scatter(inputs[:, 0], inputs[:, 1], s=40, c=targets, cmap=plt.cm.Spectral)
    plt.show()

    for epoch in range(epochs):
        # Compute and display the cost every 10 epoch
        if epoch % 10 == 0:
            predictions = activation(pre_activation(inputs, weights, bias))
            print("Current cost = %s" % cost(predictions, targets))
        # Init gradients
        weights_gradients = np.zeros(weights.shape)
        bias_gradient = 0.
        # Go through each row
        for feature, target in zip(inputs, targets):
            # Compute prediction
            z = pre_activation(feature, weights, bias)
            y = activation(z)
            # Update gradients
            weights_gradients += (y - target) * derivative_activation(z) * feature
            bias_gradient += (y - target) * derivative_activation(z)
        # Update variables
        weights = weights - (learning_rate * weights_gradients)
        bias = bias - (learning_rate * bias_gradient)
    # Print current Accuracy
    predictions = predict(inputs, weights, bias)
    print("Accuracy = %s" % np.mean(predictions == targets))    

if __name__ == "__main__":
    # Dataset
    inputs, targets = get_dataset()
    # Variables
    weights, bias = init_variables()
    # Calcul de pre activation
    # z = pre_activation(inputs, weights, bias)
    # Calcul de activation
    # a = activation(z)
    train(inputs, targets, weights, bias)