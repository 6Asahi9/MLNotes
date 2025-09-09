Got it 🌙 — I’ll rewrite this in my own words so it’s still a **cheat sheet style**, but without copying directly. Here’s a clean version for you:

---

# 📌 Quick Guide: Common Supervised Learning Models

### One-vs-One Classifier (Logistic Regression)

* **Idea**: For *k* classes, build a separate model for every pair of classes.
* **When to use**: Works fine if number of classes is small.
* **Pros**: Can separate classes well.
* **Cons**: Gets heavy as classes increase (too many models).

```python
from sklearn.multiclass import OneVsOneClassifier
from sklearn.linear_model import LogisticRegression
model = OneVsOneClassifier(LogisticRegression())
```

---

### One-vs-All Classifier (Logistic Regression)

* **Idea**: For each class, train a model that says “this class” vs “all others.”
* **When to use**: Most common multiclass setup.
* **Pros**: Scales better than One-vs-One.
* **Cons**: Can struggle if classes are very imbalanced.

```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(multi_class='ovr')
```

---

### Decision Tree (Classifier)

* **Idea**: Splits data step-by-step using feature values until reaching a decision.
* **Pros**: Easy to visualize and explain.
* **Cons**: Easily overfits if not pruned.

```python
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth=5)
```

---

### Decision Tree (Regressor)

* **Idea**: Same tree concept, but predicts continuous numbers.
* **Pros**: Captures non-linear relationships.
* **Cons**: Overfits on noisy data.

```python
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor(max_depth=5)
```

---

### Linear SVM Classifier

* **Idea**: Finds a hyperplane that separates classes with maximum margin.
* **Key parameter**: `C` (regularization), `kernel` (linear, poly, rbf, etc.).
* **Pros**: Strong in high-dimensional data (like text).
* **Cons**: Struggles with huge datasets unless optimized.

```python
from sklearn.svm import SVC
model = SVC(kernel='linear', C=1.0)
```

---

### K-Nearest Neighbors (KNN)

* **Idea**: Classifies based on the majority vote of nearest data points.
* **Pros**: Very simple, no training needed.
* **Cons**: Prediction gets slow with big datasets.

```python
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5)
```

---

### Random Forest (Regressor)

* **Idea**: A collection of decision trees averaged together.
* **Pros**: Reduces overfitting compared to a single tree.
* **Cons**: Larger model size, less interpretable.

```python
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, max_depth=5)
```

---

### XGBoost (Regressor)

* **Idea**: Boosting method — builds trees one after another, fixing previous mistakes.
* **Pros**: Very accurate, performs great on large datasets.
* **Cons**: More complex to tune.

```python
import xgboost as xgb
model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5)
```

---

# 🔧 Useful Functions and Tools

* **OneHotEncoder** → turn categorical columns into numeric binary vectors.

```python
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(sparse=False)
encoded = encoder.fit_transform(data)
```

* **accuracy\_score** → measures classification accuracy.

```python
from sklearn.metrics import accuracy_score
accuracy_score(y_true, y_pred)
```

* **LabelEncoder** → convert string labels into integers.

```python
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(labels)
```

* **plot\_tree** → visualize decision trees.

```python
from sklearn.tree import plot_tree
plot_tree(model, filled=True)
```

* **normalize** → scale feature vectors to unit length.

```python
from sklearn.preprocessing import normalize
normalized = normalize(data, norm='l2')
```

* **compute\_sample\_weight** → handle class imbalance by assigning weights.

```python
from sklearn.utils.class_weight import compute_sample_weight
weights = compute_sample_weight(class_weight='balanced', y=y)
```

* **roc\_auc\_score** → evaluate binary classifiers using AUC-ROC.

```python
from sklearn.metrics import roc_auc_score
roc_auc_score(y_true, y_score)
```

---

This version is **rephrased in my own words**, keeps the structure tidy, and is easier to skim through.

Do you want me to also make you a **one-page visual summary (like a mini poster)** where all models are grouped by *classification* vs *regression* vs *ensemble*?
