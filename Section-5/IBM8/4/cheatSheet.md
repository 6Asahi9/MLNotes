Ahhh, darling 😽💖 I can totally rewrite that in **my own words** for you, keeping it ADHD-friendly and Miya-approved, so it’s not copyrighted:

---

## **Cheat Sheet: Unsupervised Learning Models**

### **Dimensionality Reduction Methods**

**1️⃣ PCA (Principal Component Analysis)**

* **What it does:** Reduces data dimensions linearly by keeping the directions with most variance.
* **Pros:** Easy to understand, removes noise.
* **Cons:** Can miss nonlinear patterns.
* **Uses:** Feature extraction, compressing data.
* **Key parameters:**

  * `n_components` → how many dimensions to keep
  * `whiten` → scale components if needed
* **Code example:**

```python
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
```

---

**2️⃣ t-SNE**

* **What it does:** Nonlinear dimensionality reduction, emphasizes **local clusters**.
* **Pros:** Great for visualizing complex, high-dimensional data.
* **Cons:** Slow on large datasets, distances between clusters aren’t reliable.
* **Uses:** Visualization, anomaly detection.
* **Key parameters:**

  * `n_components` → output dimensions (usually 2 or 3)
  * `perplexity` → balances local/global attention
  * `learning_rate` → step size during optimization
* **Code example:**

```python
from sklearn.manifold import TSNE
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200)
```

---

**3️⃣ UMAP (Uniform Manifold Approximation and Projection)**

* **What it does:** Nonlinear reduction that preserves **both local and global structure**.
* **Pros:** Fast, works well on large datasets.
* **Cons:** Sensitive to parameters.
* **Uses:** Visualization, feature extraction.
* **Key parameters:**

  * `n_neighbors` → size of local neighborhood
  * `min_dist` → how close points can be in reduced space
  * `n_components` → number of dimensions to keep
* **Code example:**

```python
from umap.umap_ import UMAP
umap = UMAP(n_neighbors=15, min_dist=0.1, n_components=2)
```

---

### **Clustering Algorithms**

**1️⃣ K-Means**

* **How it works:** Groups points into `k` clusters based on centroids.
* **Pros:** Fast, simple.
* **Cons:** Sensitive to starting centroids.
* **Uses:** Customer segmentation, pattern recognition.
* **Key parameters:**

  * `n_clusters` → number of clusters
  * `init` → method for initializing centroids
  * `n_init` → times to repeat with different seeds
* **Code example:**

```python
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
```

**2️⃣ DBSCAN**

* **How it works:** Density-based clustering, detects outliers automatically.
* **Pros:** No need to specify number of clusters.
* **Cons:** Struggles with clusters of varying density.
* **Uses:** Anomaly detection, spatial data clustering.
* **Key parameters:**

  * `eps` → max distance to consider neighbors
  * `min_samples` → minimum points to form a cluster
* **Code example:**

```python
from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
```

**3️⃣ HDBSCAN**

* **How it works:** Hierarchical version of DBSCAN, better for varying densities.
* **Pros:** Handles complex clusters well.
* **Cons:** Slower than DBSCAN.
* **Uses:** Large datasets, complex clustering problems.
* **Key parameters:**

  * `min_cluster_size` → smallest cluster size
  * `min_samples` → minimum samples for a cluster
* **Code example:**

```python
import hdbscan
clusterer = hdbscan.HDBSCAN(min_cluster_size=5)
```

---

### **Associated Functions / Utilities**

* **make\_blobs** → create synthetic Gaussian clusters

```python
from sklearn.datasets import make_blobs
X, y = make_blobs(n_samples=100, centers=2, random_state=42)
```

* **multivariate\_normal** → generate samples from a multivariate normal distribution

```python
from numpy.random import multivariate_normal
samples = multivariate_normal(mean=[0,0], cov=[[1,0],[0,1]], size=100)
```

* **Plotly 3D Scatter** → for visualizing 3D data

```python
import plotly.express as px
fig = px.scatter_3d(df, x='x', y='y', z='z')
fig.show()
```

* **GeoPandas / Contextily** → spatial data handling and basemaps

```python
import geopandas as gpd
import contextily as ctx

gdf = gpd.GeoDataFrame(df, geometry='geometry')
gdf = gdf.to_crs(epsg=3857)
ax = gdf.plot(figsize=(10,10))
ctx.add_basemap(ax)
```

* **Explained variance in PCA** → check how much variance each component keeps

```python
pca.fit(X)
variance_ratio = pca.explained_variance_ratio_
```

---

If you want, I can **also make this into a super ADHD/Miya-style visual cheat sheet** with little icons and “paw-approved tips” for each method so you can glance and instantly know when to use PCA vs UMAP vs t-SNE vs clustering.

Do you want me to do that? 🐾✨
