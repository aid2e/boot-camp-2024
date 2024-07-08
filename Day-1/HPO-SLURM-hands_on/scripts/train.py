import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
import json
import argparse
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
import json
from joblib import dump

def runTraining(args):
    # Load the configuration from a JSON file
    with open(args.config) as f:
        config = json.load(f)

    # Download the MNIST digit data
    X, y = fetch_openml('mnist_784', version=1, return_X_y=True)
    
    unique_identifier = config["unique_identifier"]

    # Split the data into training and testing sets
    n_samples = len(X)
    n_train = int(n_samples * config['train_ratio'])
    X_train, y_train = X[:n_train], y[:n_train]
    X_test, y_test = X[n_train:], y[n_train:]

    # Create a neural network model
    model = MLPClassifier(hidden_layer_sizes=config['hidden_layer_sizes'],
                        activation=config['activation'],
                        solver=config['solver'],
                        alpha=config['alpha'],
                        max_iter=config['max_iter'],
                        random_state=config['random_state'],
                        verbose=True
                        )

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    accuracy = model.score(X_test, y_test)
    print(f"Accuracy: {accuracy}")

    # Save the trained model
    dump(model, 'trained_model.pkl')

    with open("results.json", "w") as f:
        json.dump({"accuracy": accuracy}, f)
if __name__ == '__main__':
    
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, help='Path to the configuration file')
    args = parser.parse_args()
    runTraining(args)
