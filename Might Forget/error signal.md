Nice — let’s do the concrete worked example you asked for.
I’ll use a tiny network with **2 inputs → hidden layer (3 neurons) → output layer (3 neurons)**, linear activations (so we can keep arithmetic simple and focus on where the error signals come from).

I’ll show: forward pass → per-output errors (MSE) → how the MSE produces gradients for each **output neuron** → how those gradients get distributed back so each **hidden neuron** gets its own error signal.

---

# Setup (numbers)

* Input: $x = [1.0,\; 2.0]$
* **Hidden layer (3 neurons)**

  * Weights $W^{(1)}$ (3×2):

    $$
    \begin{bmatrix}
    0.1 & 0.2\\[4pt]
    0.3 & -0.1\\[4pt]
    -0.2 & 0.4
    \end{bmatrix}
    $$
  * Biases $b^{(1)} = [0.0,\;0.1,\;-0.1]$
  * Activation: **identity** (linear) — so hidden outputs $h = W^{(1)} x + b^{(1)}$
* **Output layer (3 neurons)**

  * Weights $W^{(2)}$ (3×3):

    $$
    \begin{bmatrix}
    0.2 & -0.1 & 0.05\\[4pt]
    -0.3 & 0.4 & 0.1\\[4pt]
    0.1 & 0.2 & -0.2
    \end{bmatrix}
    $$
  * Biases $b^{(2)} = [0.05,\;-0.05,\;0.0]$
  * Output (linear): $y = W^{(2)} h + b^{(2)}$
* Targets: $t = [0.5,\; -0.1,\; 0.3]$
* Loss: **MSE** averaged over output neurons:

  $$
  E = \frac{1}{3}\sum_{i=1}^3 (y_i - t_i)^2
  $$

---

# 1) Forward pass — hidden layer outputs

Compute $h = W^{(1)}x + b^{(1)}$.

Neuron $h_1$:
$h_1 = 0.1\cdot1 + 0.2\cdot2 + 0.0 = 0.1 + 0.4 = 0.5$

Neuron $h_2$:
$h_2 = 0.3\cdot1 + (-0.1)\cdot2 + 0.1 = 0.3 -0.2 + 0.1 = 0.2$

Neuron $h_3$:
$h_3 = -0.2\cdot1 + 0.4\cdot2 - 0.1 = -0.2 +0.8 -0.1 = 0.5$

So hidden vector:

$$
h = [0.5,\;0.2,\;0.5]
$$

---

# 2) Forward pass — outputs

Compute $y = W^{(2)} h + b^{(2)}$.

$y_1 = 0.2\cdot0.5 + (-0.1)\cdot0.2 + 0.05\cdot0.5 + 0.05$
$= 0.10 -0.02 +0.025 +0.05 = 0.155$

$y_2 = -0.3\cdot0.5 + 0.4\cdot0.2 + 0.1\cdot0.5 -0.05$
$= -0.15 +0.08 +0.05 -0.05 = -0.07$

$y_3 = 0.1\cdot0.5 + 0.2\cdot0.2 + (-0.2)\cdot0.5 + 0.0$
$= 0.05 +0.04 -0.10 = -0.01$

So outputs:

$$
y = [0.155,\; -0.07,\; -0.01]
$$

---

# 3) Per-output errors (and total MSE)

Compute per-output squared errors $(y_i - t_i)^2$:

* $y_1 - t_1 = 0.155 - 0.5 = -0.345$ → squared = $0.119025$
* $y_2 - t_2 = -0.07 - (-0.1) = 0.03$ → squared = $0.000900$
* $y_3 - t_3 = -0.01 - 0.3 = -0.31$ → squared = $0.096100$

MSE (average):

$$
E = \frac{0.119025 + 0.000900 + 0.096100}{3} = 0.0720083333\ldots
$$

So yes: **each output neuron has its own squared error** — but training uses the combined MSE as the loss function.

---

# 4) Gradients at the outputs (how MSE turns into an error signal)

We differentiate loss w\.r.t. each output $y_i$. For

$$
E = \frac{1}{3}\sum (y_i-t_i)^2,
$$

the derivative is

$$
\frac{\partial E}{\partial y_i} = \frac{2}{3}(y_i - t_i).
$$

Compute the 3 values $\frac{\partial E}{\partial y_i}$:

* for output 1: $\frac{2}{3}\cdot(-0.345) = -0.230000$
* for output 2: $\frac{2}{3}\cdot(0.03) = 0.020000$
* for output 3: $\frac{2}{3}\cdot(-0.31) = -0.2066666667$

These are the **output-layer error signals** (often called $\delta$ for the output neurons when activation derivative = 1). They tell each output neuron how much changing its output would reduce the MSE.

---

# 5) How hidden neurons get *their* error signal

Hidden neurons do **not** see the raw MSE directly. Instead, each hidden neuron receives a *backpropagated* error which is the weighted sum of the output deltas (weights connecting that hidden neuron to each output), multiplied by the derivative of the hidden activation. With linear activation that derivative = 1, so:

$$
\delta^{(hidden)}_j = \sum_{i=1}^{3} W^{(2)}_{i,j}\; \delta^{(out)}_i
$$

Compute for each hidden neuron (column $j$ of $W^{(2)}$):

* Hidden neuron 1:

  $$
  \delta_{h1} = 0.2\cdot(-0.23) + (-0.3)\cdot(0.02) + 0.1\cdot(-0.2066667)
  $$

  $= -0.046 -0.006 -0.02066667 = -0.07266667$

* Hidden neuron 2:

  $$
  \delta_{h2} = (-0.1)\cdot(-0.23) + 0.4\cdot(0.02) + 0.2\cdot(-0.2066667)
  $$

  $= 0.023 +0.008 -0.04133333 = -0.01033333$

* Hidden neuron 3:

  $$
  \delta_{h3} = 0.05\cdot(-0.23) + 0.1\cdot(0.02) + (-0.2)\cdot(-0.2066667)
  $$

  $= -0.0115 +0.002 +0.04133333 = 0.03183333$

So hidden deltas:

$$
\delta^{(hidden)} = [-0.07266667,\; -0.01033333,\; 0.03183333]
$$

---

# 6) Interpretation — who “fixes itself” and how

* **Each output neuron** computes its own contribution to the loss and therefore has a direct error signal $\frac{\partial E}{\partial y_i}$. That is how that output neuron knows how to change its outgoing weights/bias to reduce the MSE.
* **Hidden neurons** don’t compute $(y-t)^2$ themselves (they’re not outputs). Instead, their error comes from the **weighted sum** of the output error signals — i.e. each hidden neuron gets a different $\delta$ proportional to how much that hidden neuron influenced each output’s error.
* The **MSE is not “ignored”** — it’s the global scalar loss from which those per-output derivatives are computed. The network minimizes that MSE, but the gradient is distributed back into per-neuron signals via the chain rule.

---

# TL;DR (short summary)

* MSE is computed as an average over output neurons (you see per-output squared errors and the combined MSE).
* Each **output neuron** gets a direct gradient $\partial E/\partial y_i$ (derived from MSE).
* Each **hidden neuron** gets an individual error signal formed by the **weighted sum** of the output gradients (times activation derivative). So **every neuron does receive its own error signal**, but those hidden-neuron signals are computed from the global loss via backpropagation, not by computing $(y-t)^2$ for the hidden neuron itself.

---

If you want, I can continue this worked example one step further and show **actual weight updates** (i.e. $\Delta W^{(2)}$, $\Delta b^{(2)}$, $\Delta W^{(1)}$, $\Delta b^{(1)}$) for a given learning rate — minute-by-minute arithmetic included. Want that? 😼✨
