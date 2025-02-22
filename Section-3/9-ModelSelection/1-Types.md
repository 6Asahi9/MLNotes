### 1️⃣ Stratified K-Fold (For Imbalanced Data)
* If your dataset has unequal class distribution (e.g., 90% cats, 10% dogs), normal K-Fold might create unbalanced splits.
* Stratified K-Fold ensures each fold has the same proportion of classes.

![1](/images/image_2025-02-22_214414598.png)

### 2️⃣ Leave-One-Out Cross-Validation (LOOCV)
* Instead of K folds, we make N folds (where N = total samples).
* Each fold has only one validation sample, and the rest are for training.
* Good for small datasets but very slow for large ones

![2](/images/image_2025-02-22_214512869.png)

### 3️⃣ Nested Cross-Validation (For Hyperparameter Tuning)
1. If you use K-Fold for model evaluation and GridSearchCV for tuning, you risk data leakage.
2. Nested CV solves this by using two levels of K-Fold:
* Outer K-Fold: Evaluates the final model.
* Inner K-Fold: Tunes hyperparameters inside each fold.

![](/images/image_2025-02-22_214622745.png)

### 4️⃣ Group K-Fold (For Grouped Data Like Patients, Users, etc.)
* If your dataset has groups (e.g., same user appears multiple times), normal K-Fold might leak data across folds.
* Group K-Fold ensures each user/group stays in only one fold

![](/images/image_2025-02-22_214734080.png)

### 5️⃣ Monte Carlo (Repeated K-Fold)
* Instead of using fixed splits, randomly split data multiple times and average results.
* Good for reducing variance in evaluation.

### 📝 Summary (Which One to Use?)

✔ Standard K-Fold → Default choice for most ML models

✔ Stratified K-Fold → Use if class distribution is imbalanced

✔ Leave-One-Out (LOOCV) → Use for tiny datasets, but slow

✔ Nested CV → Use when tuning hyperparameters to avoid data leakage

✔ Group K-Fold → Use when samples belong to groups (e.g., users, patients, etc.)

✔ Monte Carlo (Repeated K-Fold) → Use if you want randomized splits multiple times
