import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('Social_Network_Ads.csv')
print(df)

X = df.iloc[:,:-1].values
y = df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
print(X_train, X_test)

#--------------------------------------------------------------------------------------

#fitting the logistic Regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

prediction = classifier.predict(sc.transform([[30, 87000]]))
print(prediction) #answer is no or 0

y_pred = classifier.predict(X_test).reshape(-1,1)
print(np.concatenate((y_pred, y_test.reshape(-1,1)),1))

#--------------------------------------------------------------------------------------

#lets test the accuracy
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
#Accuracy: 92.50%

#or you can use them
from sklearn.metrics import precision_score, recall_score, f1_score

# Calculate Precision, Recall, F1-score
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Print the results
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1-Score: {f1:.2f}')

#Precision: 0.94
#Recall: 0.77
#F1-Score: 0.85

#making confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

#57 corret predictions of class 0 but 1 incorrect of class 1 and
#17 correct predictions of class 1 but 5 incorrect of class 0

#--------------------------------------------------------------------------------------

# Visualizing the training set

from matplotlib.colors import ListedColormap

# Reverse scaling to bring data back to its original scale
X_set, y_set = sc.inverse_transform(X_train), y_train

# Create a grid of points to cover the feature space
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 10, stop=X_set[:, 0].max() + 10, step=0.25),  # Grid for feature 1 (e.g., Age)
    np.arange(start=X_set[:, 1].min() - 1000, stop=X_set[:, 1].max() + 1000, step=0.25)  # Grid for feature 2 (e.g., Salary)
)

# Predict classifications for each point in the grid (creates decision boundary)
plt.contourf(
    X1, X2,  # Grid points
    classifier.predict(
        sc.transform(
            np.array([X1.ravel(), X2.ravel()]).T  # Transform flattened grid points using the same scaler
        )
    ).reshape(X1.shape),  # Reshape predictions to match grid shape
    alpha=0.75,  # Transparency for the filled contour plot
    cmap=ListedColormap(['#FA8072', '#1E90FF'])  # Color map for classes (e.g., Salmon for 0, Blue for 1)
)

# Set axis limits to fit the grid
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

# Scatter the original training points on the plot
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0], X_set[y_set == j, 1],  # Points belonging to class j
        c=ListedColormap(['#FA8072', '#1E90FF'])(i),  # Color for the class
        label=j  # Class label (e.g., 0 or 1)
    )

# Add title, labels, and legend to the plot
plt.title('Logistic Regression (Training set)')  # Plot title
plt.xlabel('Age')  # X-axis label
plt.ylabel('Estimated Salary')  # Y-axis label
plt.legend()  # Display legend
plt.show()  # Show the plot

#--------------------------------------------------------------------------------------

#visualising test set
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
plt.title('Logistic Regression (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

#--------------------------------------------------------------------------------------

#or can use this
from mlxtend.plotting import plot_decision_regions

# Plotting decision regions
plt.figure(figsize=(8, 6))  # Adjust figure size
plot_decision_regions(X_train, y_train, clf=classifier, legend=2)

# Overlay points as circles with custom colors
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='coolwarm', edgecolor='k', s=80)

# Add labels and title
plt.title("Logistic Regression (Training Set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.tight_layout()
plt.show()
