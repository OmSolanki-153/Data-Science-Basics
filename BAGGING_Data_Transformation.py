import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor

# Settings
n_repeat = 100       # Number of iterations for computing expectations
n_train = 100        # Size of the training set
n_test = 10000       # Size of the test set
noise = 0.1          # Standard deviation of the noise
np.random.seed(0)
#seed() is used to initialize the random number generator

estimators = [("Tree", DecisionTreeRegressor()),
              ("Bagging(Tree)", BaggingRegressor(DecisionTreeRegressor()))]
n_estimators = len(estimators)
#Regressor() is used to return the depth of decision tree

def f(x):
    x = x.ravel()
    return np.exp(-x ** 2) - 2 * np.exp(-(x - 2) ** 2)
#ravel() is used to convert 2D array

def generate(n_samples, noise, n_repeat=1):
    X = np.random.rand(n_samples) * 10 - 5
    X = np.sort(X)

    if n_repeat == 1:
        y = f(X) + np.random.normal(0.0, noise, n_samples)
    else:
        y = np.zeros((n_samples, n_repeat))
        for i in range(n_repeat):
            y[:, i] = f(X) + np.random.normal(0.0, noise, n_samples)

    X = X.reshape((n_samples, 1))
    return X, y

X_train = []
y_train = []

for i in range(n_repeat):
    X, y = generate(n_samples=n_train, noise=noise)
    X_train.append(X)
    y_train.append(y)

X_test, y_test = generate(n_samples=n_test, noise=noise, n_repeat=n_repeat)
for n, (name, estimator) in enumerate(estimators):
    y_predict = np.zeros((n_test, n_repeat))

    for i in range(n_repeat):
        estimator.fit(X_train[i], y_train[i])
        y_predict[:, i] = estimator.predict(X_test)

    # Bias^2 + Variance + Noise decomposition of the mean squared error
    y_error = np.zeros(n_test)

    for i in range(n_repeat):
        for j in range(n_repeat):
            y_error += (y_test[:, j] - y_predict[:, i]) ** 2

    y_error /= (n_repeat * n_repeat)

    y_noise = np.var(y_test, axis=1)
    y_bias = (f(X_test) - np.mean(y_predict, axis=1)) ** 2
    y_var = np.var(y_predict, axis=1)

#bias=difference between average of measurement & its true value
    print("Name \n", name);
    print("Y error=",np.mean(y_error))
    print("Y BIAS VALUE=",np.mean(y_bias))
    print("Y VARIANCE=",np.mean(y_var))
    print("Y Noise=",np.mean(y_noise))
  
    plt.subplot(2, n_estimators, n + 1)
    plt.plot(X_test, f(X_test), "b", label="f(x) original function")
    plt.plot(X_train[0], y_train[0], ".b", label="function susbstitution")

    for i in range(n_repeat):
        if i == 0:
            plt.plot(X_test, y_predict[:, i], "red", label="predict 1")
        else:
            plt.plot(X_test, y_predict[:, i], "red", alpha=0.05)

    plt.plot(X_test, np.mean(y_predict, axis=1), "yellow",label="predict 2")

    plt.xlim([-5, 5])
    plt.title(name)
    if n == 0:
        plt.legend(loc="lower left", prop={"size": 10})

    plt.subplot(2, n_estimators, n_estimators + n + 1)
    plt.plot(X_test, y_error, "red", label="ERROR")
    plt.plot(X_test, y_bias, "blue", label="BIAS"),
    plt.plot(X_test, y_var, "green", label="VARIANCE"),
    plt.plot(X_test, y_noise, "yellow", label="NOISE")

    plt.xlim([-5, 5])
    plt.ylim([0, 0.1])

    if n == 0:
        plt.legend(loc="upper left", prop={"size": 10})

plt.show()
