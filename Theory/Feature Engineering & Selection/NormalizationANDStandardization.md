### 1️⃣ Min-Max Scaling vs. Z-Score Normalization
🔹 Min-Max Scaling (Normalization)

These are two ways to scale numerical features so that models like logistic regression perform better.

![](/images/image_2025-03-02_165335535.png)

🔹 Z-Score Normalization (Standardization)

![](/images/image_2025-03-02_165448912.png)

### 💡 Which one to use?

* If your data has many outliers → Z-score (Standardization)
* If your data is bounded & needs a fixed range → Min-Max Scaling

### 🐱 Miya and the Magical Heights of Jumping
Miya loves jumping onto different surfaces—your lap, the table, the window, and even the highest shelf! Let’s say you measure the heights she jumps in centimeters:

Miya’s jump heights:

30 cm 

50 cm

70 cm

90 cm

But now, Miya’s cousin, a tiny kitten, wants to compete, and their jumps are in millimeters (300 mm, 500 mm, etc.). Since their numbers are much larger, it makes comparison difficult!

###  📌 What is Normalization (Min-Max Scaling)?
Think of Normalization as converting all jump heights into a common scale between 0 and 1.

This way, Miya’s highest jump is 1 (100%), and her lowest is 0 (0%).

𝑋min = lowest jump (30 cm)

𝑋max = highest jump (90 cm)

After applying this:

30 cm → 0

50 cm → 0.33

70 cm → 0.66

90 cm → 1

Now everything is scaled between [0,1], making it easier to compare!

### 🐾 When to use?

* When you need values between 0 and 1 (e.g., images, percentages).
* But! It is sensitive to outliers (we’ll see what that means soon).
