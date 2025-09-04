Perfect question 👍 let’s tie it directly to Ridge regression, since that’s where **α** (alpha) lives.

---

### 🔹 Hyperparameters

* In ML, **parameters** = things the model *learns from data* (like the coefficients $w, b$ in regression).
* **Hyperparameters** = things *you set before training* that control how the model learns or behaves.

For **Ridge Regression**:

* The main hyperparameter is **`alpha`** (regularization strength).

  * Big `alpha` → coefficients shrink more → less overfitting, but maybe underfitting.
  * Small `alpha` → closer to plain LinearRegression.

So here, `alpha` is a **hyperparameter**.

---

### 🔹 Grid Search

Grid Search is a method to **find the best hyperparameters** automatically:

1. You define a “grid” of possible values for hyperparameters.
   Example: $\alpha = [0.01, 0.1, 1, 10, 100]$
2. GridSearchCV trains the model for **every combination** and tests performance (via cross-validation).
3. It picks the hyperparameter values that give the best score.

---

### 🔹 Code Example with Ridge + Grid Search

```python
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV, train_test_split

# Example dataset
data = {
    "x1": [1, 2, 3, 4, 5],
    "x2": [2, 4, 6, 8, 10],
    "y":  [1.1, 2.0, 2.9, 4.2, 5.1]
}
df = pd.DataFrame(data)

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Grid of alpha values
param_grid = {"alpha": [0.01, 0.1, 1, 10, 100]}

ridge = Ridge()

# GridSearchCV to test each alpha
grid = GridSearchCV(ridge, param_grid, cv=3)
grid.fit(X_train, y_train)

print("Best alpha:", grid.best_params_)
print("Best score:", grid.best_score_)
print("Test set R^2:", grid.score(X_test, y_test))
```

---

👉 So in short:

* **Hyperparameters** = knobs you set before training (like `alpha`).
* **Grid search** = systematic way to try many knob values and pick the best one.

---

Do you want me to also show the difference between **GridSearchCV** and **RandomizedSearchCV** for this same Ridge case?
