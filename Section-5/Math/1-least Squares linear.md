Yes, exactly, Asahi 🌸

**Mean Squared Error (MSE)** is just **least squares divided by the number of points**. So:

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - y_\text{model,i})^2
$$

---

### Let’s do your linear least squares **by hand**, like math 📝

We have data:

| x | y |
| - | - |
| 1 | 2 |
| 2 | 3 |
| 3 | 5 |

Model:

$$
y = m x + c
$$

Goal: minimize

$$
S = \sum (y_i - (m x_i + c))^2
$$

---

### Step 1: Write the sum of squared errors

$$
S = (2 - (m\cdot1 + c))^2 + (3 - (m\cdot2 + c))^2 + (5 - (m\cdot3 + c))^2
$$

---

### Step 2: Take derivatives wrt $m$ and $c$ and set them to 0

**Derivative wrt $c$:**

$$
\frac{\partial S}{\partial c} = 2(2 - (m + c))(-1) + 2(3 - (2m + c))(-1) + 2(5 - (3m + c))(-1) = 0
$$

Divide by 2 and multiply by -1:

$$
(2 - m - c) + (3 - 2m - c) + (5 - 3m - c) = 0
$$

Combine terms:

$$
(2 + 3 + 5) - (m + 2m + 3m) - (c + c + c) = 0
$$

$$
10 - 6m - 3c = 0 \quad \Rightarrow \quad 6m + 3c = 10 \quad (1)
$$

---

**Derivative wrt $m$:**

$$
\frac{\partial S}{\partial m} = 2(2 - (m + c))(-1\cdot x_1) + 2(3 - (2m + c))(-1 \cdot x_2) + 2(5 - (3m + c))(-1 \cdot x_3) = 0
$$

Divide by 2 and multiply by -1:

$$
1\cdot(2 - m - c) + 2\cdot(3 - 2m - c) + 3\cdot(5 - 3m - c) = 0
$$

Compute each term:

$$
(2 - m - c) + 2(3 - 2m - c) + 3(5 - 3m - c) = 0
$$

$$
(2 - m - c) + (6 - 4m - 2c) + (15 - 9m - 3c) = 0
$$

Combine:

$$
2 + 6 + 15 - (m + 4m + 9m) - (c + 2c + 3c) = 0
$$

$$
23 - 14m - 6c = 0 \quad \Rightarrow \quad 14m + 6c = 23 \quad (2)
$$

---

### Step 3: Solve the system of equations

Equations:

1. $6m + 3c = 10$
2. $14m + 6c = 23$

Divide second equation by 2:

$$
7m + 3c = 11.5
$$

Subtract first equation:

$$
(7m + 3c) - (6m + 3c) = 11.5 - 10 \quad \Rightarrow \quad m = 1.5
$$

Plug $m = 1.5$ into first equation:

$$
6(1.5) + 3c = 10 \quad \Rightarrow \quad 9 + 3c = 10 \quad \Rightarrow \quad c = \frac{1}{3} \approx 0.333
$$

---

✅ Final best-fit line:

$$
\boxed{y \approx 1.5x + 0.333}
$$

* This **minimizes the sum of squared errors**, i.e., linear least squares.

---

If you want, I can **draw the points, the line, and the little squared errors on a tiny graph**, so you see why the “squared” part makes sense visually 🌸

Do you want me to do that?
