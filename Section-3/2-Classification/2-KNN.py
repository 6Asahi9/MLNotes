import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Social_Network_Ads.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#KNN fitting
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)
#[[64  4]
#[ 3 29]]
#0.93

#---------------------------------------------------------------------------------------------------------------
#mix data / PCA included 

from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

# Apply PCA to reduce the features to 2 dimensions
pca = PCA(n_components=2)
X_train_reduced = pca.fit_transform(X_train)
X_test_reduced = pca.transform(X_test)

# Train the classifier with the reduced data
classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
classifier.fit(X_train_reduced, y_train)
y_pred = classifier.predict(X_test_reduced)

# Plotting decision boundary
x_min, x_max = X_train_reduced[:, 0].min() - 1, X_train_reduced[:, 0].max() + 1
y_min, y_max = X_train_reduced[:, 1].min() - 1, X_train_reduced[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

# Predict the class for each point in the meshgrid (on reduced features)
Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the decision boundary
plt.contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.coolwarm)

# Plot the training points
train_scatter = plt.scatter(X_train_reduced[:, 0], X_train_reduced[:, 1], c=y_train, marker='o', edgecolor='k', cmap=plt.cm.coolwarm, label="0")

# Plot the test points
test_scatter = plt.scatter(X_test_reduced[:, 0], X_test_reduced[:, 1], c=y_pred, marker='o', edgecolor='k', cmap=plt.cm.coolwarm, label="1")

#modify the numbers on the x and y axes
plt.xticks(ticks=np.linspace(x_min, x_max, 6), labels=[10, 20, 30, 40, 50, 60])
plt.yticks(ticks=np.linspace(y_min, y_max, 7), labels=["20k", "40k", "60k", "80k", "100k", "120k", "140k"])

# Add a legend for clearer interpretation
plt.legend(handles=[train_scatter, test_scatter], labels=['NO', 'yes'], title="Class Categories")

# Set labels and title
plt.title('KNN Classifier Decision Boundary (PCA Reduced)')
plt.xlabel('Salary')
plt.ylabel('age')
plt.show()

#---------------------------------------------------------------------------------------------------------------

#training set
# Apply PCA to reduce the features to 2 dimensions
pca = PCA(n_components=2)
X_train_reduced = pca.fit_transform(X_train)
X_test_reduced = pca.transform(X_test)

# Train the classifier with the reduced data
classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
classifier.fit(X_train_reduced, y_train)

# Predict the class for each point in the meshgrid (on reduced features)
x_min, x_max = X_train_reduced[:, 0].min() - 1, X_train_reduced[:, 0].max() + 1
y_min, y_max = X_train_reduced[:, 1].min() - 1, X_train_reduced[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# PLOT 1: Training data only
plt.figure(figsize=(10, 5))

# Plot the decision boundary
plt.contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.coolwarm)

# Plot the training points
scatter = plt.scatter(X_train_reduced[:, 0], X_train_reduced[:, 1], c=y_train, marker='o', edgecolor='k', cmap=plt.cm.coolwarm, label="Train Data")

# Modify the numbers on the x and y axes
plt.xticks(ticks=np.linspace(x_min, x_max, 6), labels=[10, 20, 30, 40, 50, 60])
plt.yticks(ticks=np.linspace(y_min, y_max, 7), labels=["20k", "40k", "60k", "80k", "100k", "120k", "140k"])

# Set labels and title
plt.title('KNN Classifier Decision Boundary (Training Data)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(handles=scatter.legend_elements()[0], labels=['No', 'Yes'], title="Car Purchase Decision")
plt.show()

#---------------------------------------------------------------------------------------------------------------
#test set
# PLOT 2: Test data only
y_pred = classifier.predict(X_test_reduced)

plt.figure(figsize=(10, 5))

# Plot the decision boundary
plt.contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.coolwarm)

# Plot the test points
scatter = plt.scatter(X_test_reduced[:, 0], X_test_reduced[:, 1], c=y_pred, marker='o', edgecolor='k', cmap=plt.cm.coolwarm, label="Test Data")

# Modify the numbers on the x and y axes
plt.xticks(ticks=np.linspace(x_min, x_max, 6), labels=[10, 20, 30, 40, 50, 60])
plt.yticks(ticks=np.linspace(y_min, y_max, 7), labels=["20k", "40k", "60k", "80k", "100k", "120k", "140k"])

# Set labels and title
plt.title('KNN Classifier Decision Boundary (Test Data)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(handles=scatter.legend_elements()[0], labels=['No', 'Yes'], title="Car Purchase Decision")
plt.show()

#---------------------------------------------------------------------------------------------------------------
#original training (HEAVY)
from matplotlib.colors import ListedColormap
X_set, y_set = sc.inverse_transform(X_train), y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 10, stop = X_set[:, 0].max() + 10, step = 0.5),
                     np.arange(start = X_set[:, 1].min() - 1000, stop = X_set[:, 1].max() + 1000, step = 0.5))
plt.contourf(X1, X2, classifier.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(['#FA8072', '#1E90FF']))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], c = ListedColormap(['#FA8072', '#1E90FF'])(i), label = j)
plt.title('K-NN (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

#---------------------------------------------------------------------------------------------------------------
#original test (HEAVY)
from matplotlib.colors import ListedColormap
X_set, y_set = sc.inverse_transform(X_test), y_test
# Create a grid of points
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.5),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.5)
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
plt.title('K-NN (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
