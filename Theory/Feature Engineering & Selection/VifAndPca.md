### 3️⃣ Variance Inflation Factor (VIF) - Detecting Multicollinearity
* Multicollinearity happens when two or more features are highly correlated, making logistic regression unstable.
* VIF measures how much a feature is correlated with others.

![](/images/image_2025-03-02_170745255.png)

![](/images/image_2025-03-02_170815246.png)

### 📌 If VIF is high, you can:

* Remove one of the highly correlated features
* Use PCA (Principal Component Analysis)
* Apply Regularization (L1/L2)

### 🐱 What is Multicollinearity? (Similar Features Confusing Miya!)
Imagine you tell Miya:

* 1️⃣ "Check the softness of the ball!"
* 2️⃣ "Check the squishiness of the ball!"

Both features mean almost the same thing, right? 🤔

This redundancy is called Multicollinearity—when features are too similar and confuse the model.

### 📌 Why is it bad?

* Logistic regression struggles to decide which feature is important.
* It makes coefficients unstable (changing too much).
### 📌 Solution?

* Use VIF (Variance Inflation Factor) to detect this.
* If VIF is high, remove one of the similar features.

### Principal Component Analysis (PCA)
* Reduces dimensions by creating new uncorrelated features.
* Transforms data into principal components (PCs) that maximize variance.

Formula (eigen decomposition of covariance matrix):

𝑋′ = XW 

W contains eigenvectors of the covariance matrix.
