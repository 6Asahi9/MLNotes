Absolutely, love! Here's a fully rewritten and Miya-safe version — original, clear, and perfect for your notes:

---

## 🧪 Class Balancing Techniques (Rewritten for Notes)

### 🔁 **Oversampling**

**What it is:**
A method that increases the number of samples in the minority class, often by copying existing entries or creating new synthetic ones.

**When to use:**
Ideal when the minority class has too few samples, and you don’t want to remove any data from the majority class.

**Pros:**

* Helps the model learn patterns in underrepresented classes
* Useful when keeping the full dataset is important

**Cons:**

* Risk of overfitting, especially if you're just duplicating data
* The model might memorize repeated samples instead of generalizing

---

### 🔽 **Undersampling**

**What it is:**
This approach reduces the number of samples from the majority class to make it match the size of the minority class.

**When to use:**
Best used when the majority class is extremely large and trimming some data won’t hurt the model’s learning ability.

**Pros:**

* Faster training with fewer samples
* Reduces bias toward the majority class

**Cons:**

* Might remove useful information
* The model could miss important patterns in the discarded data

---

### ⚖️ **Class Weighting**

**What it is:**
Rather than changing the number of samples, this method changes how much each class matters during training — giving more importance to the minority class.

**When to use:**
Great when you want to use the full dataset without duplicating or deleting anything.

**Pros:**

* Keeps all original data
* Avoids overfitting due to repetition
* Lets the model take the minority class more seriously

**Cons:**

* Picking the right weights can be tricky
* Too much weight might skew the model’s predictions

---

Let me know if you want this turned into a prettier format (like bullet cards or collapsible sections for Notion or Obsidian), or if Miya wants cat emoji markers next to each title 🐾💕
