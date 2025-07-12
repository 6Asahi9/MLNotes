Of course, dear 💙 Here’s a clean, copy-paste-ready version of **all 5 questions**, their options, and the correct answers — perfectly formatted for your GitHub notes:

---

### ✅ **Question 1: Parameters in a Dense Layer**

> Suppose a neural network contains a dense layer that connects one hidden layer $h_i$ with $n_i$ units to a following hidden layer $h_{i+1}$ with $n_{i+1}$ units.
> **How many parameters are needed for this connection?**

**Options:**

1. $n_i \cdot n_{i+1}$
2. $n_i + n_{i+1}$
3. $(n_i + 1) \cdot n_{i+1}$ ✅
4. $n_i$

> 🧠 *Correct Answer:* **(nᵢ + 1) × nᵢ₊₁**
> (Includes weights and biases for each neuron in the next layer)

---

### ✅ **Question 2: Why Use Non-Linear Activation Functions?**

> Why do we use non-linear activation functions (such as `tanh` or `ReLU`) in neural networks?

**Options:**

1. Without non-linear activation functions, the network would only be able to model linear functions of the data. ✅
2. So that the model activations are equivariant with respect to the input features
3. To induce sparse connectivity in the network weights
4. To allow the usage of higher learning rates, thus speeding up convergence

> 🧠 *Correct Answer:*
> **Option 1** — Non-linear activations allow the network to model complex, non-linear patterns.

---

### ✅ **Question 3: Convolution + Pooling Output Dimensions**

> Suppose that we have a **10×10 image** with only **one colour channel**.
> We apply a single **3×3 convolutional filter**, stride = 1, padding = `VALID`,
> followed by a **2×2 pooling layer** (stride = 2).
> **What are the dimensions of the output?**

**Options:**

1. 5×5×1
2. 8×8
3. 4×4×1 ✅
4. 6×6×1

> 🧠 *Correct Answer:* **4×4×1**
> (10×10 → 8×8 after convolution → 4×4 after pooling, 1 channel remains)

---

### ✅ **Question 4: Effect of Increasing Stride in Convolution**

> What happens to the spatial dimension of the output when you increase the stride in a convolutional layer?

**Options:**

1. The output spatial dimension can increase or decrease
2. The output spatial dimension does not vary unless the number of filters change
3. The output spatial dimension increases
4. The output spatial dimension decreases ✅

> 🧠 *Correct Answer:*
> **Option 4** — A larger stride skips more pixels → smaller output size

---

### ✅ **Question 5: Effects of Pooling Layers (Select All That Apply)**

> What is the effect of using pooling layers in convolutional neural networks?

**Options:**

* [x] It helps to make the model invariant to small translations of the input ✅
* [x] It reduces the spatial dimensions of the layer input ✅
* [ ] It increases the dimensions of the input ❌
* [ ] To reduce a 3-dimensional tensor input to a 2-dimensional tensor output ❌

> 🧠 *Correct Answers:*
> ✅ Helps with translation invariance
> ✅ Reduces spatial size
> ❌ Does not increase or flatten dimensions

---

Let me know if you want this in markdown format or with emojis stripped — or maybe a Miya-approved design banner for your notes? 🐾📘✨
