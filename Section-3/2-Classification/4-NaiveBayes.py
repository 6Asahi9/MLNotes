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

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
np.concatenate((y_pred.reshape(-1, 1), y_test.reshape(-1, 1)), axis=1)

from sklearn.metrics import accuracy_score
accuracy_score(y_pred, y_test)
#0.9125

#-----------------------------------------------------------------------------------------------------------
#smooth train set
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_train_2d = pca.fit_transform(X_train)

classifier = GaussianNB()
classifier.fit(X_train_2d, y_train)

# Create a meshgrid for plotting decision boundary
x_min, x_max = X_train_2d[:, 0].min() - 1, X_train_2d[:, 0].max() + 1
y_min, y_max = X_train_2d[:, 1].min() - 1, X_train_2d[:, 1].max() + 1
h = 0.02  # Step size for meshgrid
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Predict the class for each point in the meshgrid
Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the decision boundary and data points
plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.RdBu)

# Plot also the training points
scatter = plt.scatter(X_train_2d[:, 0], X_train_2d[:, 1], c=y_train, edgecolors='k', cmap=plt.cm.RdBu, marker='o', s=80)

# Label the axes and show the plot
plt.title('SVC with RBF Kernel - Decision Boundary (PCA Reduced Data)', fontsize=14)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(scatter, label='Class')
plt.show()

#-----------------------------------------------------------------------------------------------------------
#smooth test set
X_test_2d = pca.transform(X_test)  # Apply PCA to test data as well

# Create a meshgrid for plotting decision boundary
x_min, x_max = X_test_2d[:, 0].min() - 1, X_test_2d[:, 0].max() + 1
y_min, y_max = X_test_2d[:, 1].min() - 1, X_test_2d[:, 1].max() + 1
h = 0.02  # Step size for meshgrid
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Predict the class for each point in the meshgrid
Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the decision boundary for the test set
plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.RdBu)

# Plot only test points
scatter_test = plt.scatter(X_test_2d[:, 0], X_test_2d[:, 1], c=y_test, edgecolors='k', cmap=plt.cm.spring, marker='o', s=80)

# Label the axes and show the plot
plt.title('SVC with RBF Kernel - Decision Boundary (Test Set Only, PCA Reduced Data)', fontsize=14)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(scatter_test, label='Test Class')
plt.show()

#-----------------------------------------------------------------------------------------------------------
#less pixelated 
from matplotlib.colors import ListedColormap

# Adjust meshgrid step size for faster computation
step_size = 1.0  # Increase from 0.25 to 1.0 to reduce computation
X_set, y_set = sc.inverse_transform(X_train), y_train
X1, X2 = np.meshgrid(np.arange(start=X_set[:, 0].min() - 10, stop=X_set[:, 0].max() + 10, step=step_size),
                     np.arange(start=X_set[:, 1].min() - 1000, stop=X_set[:, 1].max() + 1000, step=step_size))

# Reduce the precision of predictions
Z = classifier.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape)

# Plot contour with lighter alpha for smooth display
plt.contourf(X1, X2, Z, alpha=0.6, cmap=ListedColormap(['#FA8072', '#1E90FF']))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

# Downsample scatter points if dataset is too large
for i, j in enumerate(np.unique(y_set)):
    mask = y_set == j
    if mask.sum() > 100:  # Downsample if more than 100 points
        idx = np.random.choice(np.where(mask)[0], size=100, replace=False)  # Random sample
        plt.scatter(X_set[idx, 0], X_set[idx, 1], c=ListedColormap(['#FA8072', '#1E90FF'])(i), label=j)
    else:
        plt.scatter(X_set[mask, 0], X_set[mask, 1], c=ListedColormap(['#FA8072', '#1E90FF'])(i), label=j)

# Add labels and title
plt.title('Kernel SVM (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
