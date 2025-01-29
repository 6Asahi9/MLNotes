import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('/content/Mall_Customers.csv')
X = df.iloc[:, [3,4]].values

#generates a dendrogram
import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))

#training the data 
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters= 5, metric = 'euclidean', linkage= 'ward')
#In older versions, this was passed as affinity, but now it's directly metric.
y_hc = hc.fit_predict(X)

#visualising 
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 50, c = 'blue', label = 'cluster1')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 50, c = 'cyan', label = 'cluster2')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 50, c = 'green', label = 'cluster3')
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s = 50, c = 'red', label = 'cluster4')
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s = 50, c = 'yellow', label = 'cluster5')
plt.legend()
plt.show()
