Of course, Asahi 🌙💙! I’ll put everything we discussed into **one big, neat note** that you can directly put in your GitHub. I’ll include explanations, formulas, and the completed graded functions so it’s **self-contained**.

Here’s the full note:

---

# 📝 Neural Network Backpropagation Notes (3-Layer Network)

This note summarizes a manual implementation of a 3-layer fully connected neural network with forward pass, cost function, and gradients (Jacobians) for weights and biases.

---

## 1️⃣ Activation Function

We use **sigmoid** (σ) and its derivative:

```python
import numpy as np

# Sigmoid activation
sigma = lambda z: 1 / (1 + np.exp(-z))

# Derivative of sigmoid
d_sigma = lambda z: np.cosh(z/2)**(-2) / 4
```

* Output range: (0,1)
* Smooth, differentiable → good for backpropagation

---

## 2️⃣ Network Initialization

The network has:

* Input layer: 1 neuron
* Hidden layer 1: `n1` neurons
* Hidden layer 2: `n2` neurons
* Output layer: 2 neurons

Weights and biases are initialized randomly:

```python
def reset_network(n1=6, n2=7, random=np.random):
    global W1, W2, W3, b1, b2, b3
    W1 = random.randn(n1, 1) / 2
    W2 = random.randn(n2, n1) / 2
    W3 = random.randn(2, n2) / 2
    b1 = random.randn(n1, 1) / 2
    b2 = random.randn(n2, 1) / 2
    b3 = random.randn(2, 1) / 2
```

---

## 3️⃣ Forward Pass

```python
def network_function(a0):
    z1 = W1 @ a0 + b1
    a1 = sigma(z1)
    z2 = W2 @ a1 + b2
    a2 = sigma(z2)
    z3 = W3 @ a2 + b3
    a3 = sigma(z3)
    return a0, z1, a1, z2, a2, z3, a3
```

* `@` is matrix multiplication
* Returns all **weighted sums and activations** for backpropagation

---

## 4️⃣ Cost Function

We use **squared error**:

$$
C = \frac{1}{N} \sum (a3 - y)^2
$$

```python
def cost(x, y):
    return np.linalg.norm(network_function(x)[-1] - y)**2 / x.size
```

* `x.size` = number of training examples
* Measures network performance

---

## 5️⃣ Backpropagation (Jacobians)

### Output layer

#### Weights `W3`

```python
def J_W3(x, y):
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)
    J = 2 * (a3 - y)           # dC/da3
    J = J * d_sigma(z3)        # da3/dz3
    J = J @ a2.T / x.size      # dz3/dW3 (previous activations)
    return J
```

#### Biases `b3`

```python
def J_b3(x, y):
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)
    J = 2 * (a3 - y)
    J = J * d_sigma(z3)
    J = np.sum(J, axis=1, keepdims=True) / x.size
    return J
```

---

### Hidden Layer 2

#### Weights `W2`

```python
def J_W2(x, y):
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)    
    J = 2 * (a3 - y)
    J = J * d_sigma(z3)
    J = (J.T @ W3).T            # da3/da2 * W3
    J = J * d_sigma(z2)
    J = J @ a1.T / x.size
    return J
```

#### Biases `b2`

```python
def J_b2(x, y):
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)
    J = 2 * (a3 - y)
    J = J * d_sigma(z3)
    J = (J.T @ W3).T
    J = J * d_sigma(z2)
    J = np.sum(J, axis=1, keepdims=True) / x.size
    return J
```

---

### Hidden Layer 1

#### Weights `W1`

```python
def J_W1(x, y):
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)
    J = 2 * (a3 - y)
    J = J * d_sigma(z3)
    J = (J.T @ W3).T
    J = J * d_sigma(z2)
    J = (J.T @ W2).T
    J = J * d_sigma(z1)
    J = J @ a0.T / x.size
    return J
```

#### Biases `b1`

```python
def J_b1(x, y):
    a0, z1, a1, z2, a2, z3, a3 = network_function(x)
    J = 2 * (a3 - y)
    J = J * d_sigma(z3)
    J = (J.T @ W3).T
    J = J * d_sigma(z2)
    J = (J.T @ W2).T
    J = J * d_sigma(z1)
    J = np.sum(J, axis=1, keepdims=True) / x.size
    return J
```

---

## 6️⃣ Notes on Implementation

* **Chain Rule** is applied from output → input
* Bias derivatives **do not multiply by previous activations**
* Weight derivatives **multiply by previous layer activations**
* Averaged over all training examples using `/ x.size`
* This setup allows **manual backpropagation** for understanding gradient flow

---

## ✅ Summary

* Forward pass computes activations at each layer
* Cost measures difference between network output and desired output
* Jacobians compute gradients for **gradient descent**
* This is a fully connected 3-layer network example implemented **from scratch** in Python

---

If you like, Asahi, I can also make a **diagram of the network with the Jacobian flow arrows** to paste into your GitHub notes—it will look super clean and explanatory.

Do you want me to do that too?
