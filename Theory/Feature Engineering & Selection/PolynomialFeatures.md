### 2️⃣ Polynomial Features (to capture non-linearity)
* Logistic regression assumes a linear decision boundary, but what if the data isn’t linearly separable?
* Polynomial features help by creating higher-degree versions of existing features.

🔹 Example:

![](/images/image_2025-03-02_170329293.png)

This allows logistic regression to model curved decision boundaries.

### 📌 Downside:

* More features = higher complexity = risk of overfitting
* Use Regularization (L1/L2) to handle this

🔹 How to implement in Python?

![](/images/image_2025-03-02_170425049.png)

### 🐱 Higher-Degree Features (Curved Boundaries!)
What if Miya organizes her toys based on size AND bounciness? Now, she needs a curved boundary to separate them!

By adding polynomial features (like squaring the values), we can create a more curved decision boundary instead of a straight line.

* Linear (normal): Red vs. Blue by size
* Polynomial: Red vs. Blue by size & bounciness
* This is useful when simple models (like logistic regression) aren’t enough to separate the data properly.
