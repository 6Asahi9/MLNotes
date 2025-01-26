import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('/content/Social_Network_Ads.csv')
X = df.iloc[:,:-1].values
y = df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state = 0, test_size=0.2)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=10, criterion="entropy", random_state=0)
classifier.fit(X_train,y_train)

y_pred = classifier.predict(X_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)
#0.9125

# Step 1: Create a function to plot the decision boundary
def plot_decision_boundary(X, y, classifier, ax, title=""):
    # Create a grid of points for the decision boundary
    X_set, y_set = X, y
    X1, X2 = np.meshgrid(np.arange(X_set[:, 0].min() - 1, X_set[:, 0].max() + 1, 1),
                         np.arange(X_set[:, 1].min() - 1, X_set[:, 1].max() + 1, 1))
    # Predict the classifier’s result on the grid
    Z = classifier.predict(np.array([X1.ravel(), X2.ravel()]).T)
    Z = Z.reshape(X1.shape)

    # Plot the contour and training points
    ax.contourf(X1, X2, Z, alpha=0.75, cmap=plt.cm.coolwarm)
    scatter = ax.scatter(X_set[:, 0], X_set[:, 1], c=y_set, cmap=plt.cm.coolwarm, edgecolors='k', s=20)
    ax.set_title(title)
    ax.legend(*scatter.legend_elements(), title="Classes")

# Step 2: Plotting for the training set
plt.figure(figsize=(7, 6))
plot_decision_boundary(X_train, y_train, classifier, plt.gca(), title="Decision Boundary (Training set)")
plt.tight_layout()
plt.show()

# Step 3: Plotting for the test set
plt.figure(figsize=(7, 6))
plot_decision_boundary(X_test, y_test, classifier, plt.gca(), title="Decision Boundary (Test set)")
plt.tight_layout()
plt.show()
