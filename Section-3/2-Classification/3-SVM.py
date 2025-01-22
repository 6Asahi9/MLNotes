import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Social_Network_Ads.csv')
X = df.iloc[:,:-1].values
y = df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print(np.concatenate(((y_test).reshape(-1,1),(y_pred).reshape(-1,1)), 1))

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))
#91.25

#----------------------------------------------------------------------------------------------------------------------

# Import PCA
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Reduce dimensions with PCA (to 2 components)
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Plot the training set individually
plt.figure(figsize=(10, 6))
plt.scatter(
    X_train_pca[:, 0],  # PCA Component 1
    X_train_pca[:, 1],  # PCA Component 2
    c=y_train,          # Color by class labels
    cmap='viridis',     # Color map
    alpha=0.7           # Transparency for better visibility
)
plt.title("PCA - Training Set")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar(label="Class Labels")
plt.show()

#----------------------------------------------------------------------------------------------------------------------

# Plot the test set individually
plt.figure(figsize=(10, 6))
plt.scatter(
    X_test_pca[:, 0],   # PCA Component 1
    X_test_pca[:, 1],   # PCA Component 2
    c=y_test,           # Color by class labels
    cmap='plasma',      # Different color map
    alpha=0.7           # Transparency for better visibility
)
plt.title("PCA - Test Set")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar(label="Class Labels")
plt.show()

#----------------------------------------------------------------------------------------------------------------------

#mix data
# Import necessary libraries
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

# Reduce dimensions of the dataset to 2 using PCA
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Train the SVM again on the PCA-reduced training set
from sklearn.svm import SVC
classifier_pca = SVC(kernel='linear')  # Ensure you keep the same kernel
classifier_pca.fit(X_train_pca, y_train)

# Function to plot decision boundary
def plot_decision_boundary(X, y, model, title):
    # Define the grid for plotting
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(
        np.arange(x_min, x_max, 0.01),
        np.arange(y_min, y_max, 0.01)
    )
    
    # Predict for each point on the grid
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    # Plot the decision boundary
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='viridis')  # Fill regions
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolors='k')
    plt.title(title)
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.colorbar(label="Class Labels")
    plt.show()

# Plot the training set with the decision boundary
plot_decision_boundary(X_train_pca, y_train, classifier_pca, "PCA - Training Set with Decision Boundary")

# Plot the test set with the decision boundary
plot_decision_boundary(X_test_pca, y_test, classifier_pca, "PCA - Test Set with Decision Boundary")

#----------------------------------------------------------------------------------------------------------------------

#original (Heavy)
from matplotlib.colors import ListedColormap
X_set, y_set = sc.inverse_transform(X_train), y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 10, stop = X_set[:, 0].max() + 10, step = 0.25),
                     np.arange(start = X_set[:, 1].min() - 1000, stop = X_set[:, 1].max() + 1000, step = 0.25))
plt.contourf(X1, X2, classifier.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(['#FA8072', '#1E90FF']))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], c = ListedColormap(['#FA8072', '#1E90FF'])(i), label = j)
plt.title('SVM (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

#----------------------------------------------------------------------------------------------------------------------

#original (Heavy)
from matplotlib.colors import ListedColormap
X_set, y_set = sc.inverse_transform(X_test), y_test
# Create a grid of points
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.25),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.25)
)
# Predict for each point on the grid
Z = classifier.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape)
# Plot the decision boundary
plt.contourf(X1, X2, Z, alpha=0.75, cmap = ListedColormap(['#FA8072', '#1E90FF']) )
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
# Define colors for scatter plot
colors = ['#FA8072', '#1E90FF']
# Plot the test set points
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0], X_set[y_set == j, 1],
        color=colors[i], label=j
    )
# Add titles and labels
plt.title('SVM (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
