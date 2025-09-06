Ah, perfect, darling 🌙💙 now it’s time to fill in the missing derivatives and see how the Lagrange system works in code. Let’s go **step by step**.

---

### **Step 1: Fill in the missing derivatives**

The constraint is:

$$
g(x, y) = x^2 + 3(y+1)^2 - 1
$$

* Derivative with respect to $x$:

$$
\frac{\partial g}{\partial x} = 2x
$$

* Derivative with respect to $y$:

$$
\frac{\partial g}{\partial y} = 6(y+1)
$$

So in code:

```python
def dgdx(x, y):
    return 2*x

def dgdy(x, y):
    return 6*(y + 1)
```

✅ Done!

---

### **Step 2: The vector equation**

The DL function is already correct:

```python
def DL(xyλ):
    [x, y, λ] = xyλ
    return np.array([
        dfdx(x, y) - λ * dgdx(x, y),
        dfdy(x, y) - λ * dgdy(x, y),
        - g(x, y)
    ])
```

* The first two entries are the Lagrange multiplier equations
* The last entry is the constraint $g(x, y) = 0$

---

### **Step 3: Solving**

You already have the starting point: `(-1, -1, 0)`.

* Use `optimize.root(DL, [x0, y0, λ0]).x` to find one solution
* To find **other stationary points**, just **change the initial guess** (starting point) because root-finding methods can converge to different solutions depending on the start.

There are **4 solutions in total**, as mentioned.

---

### **Step 4: Answer the quiz**

* Once you run the code with a different starting point, check `y` in the output.
* Round it to **two decimal places**.

---

If you want, darling, I can **write a full Python snippet that finds all four solutions** so you can just run it and get all the `y` values for the quiz 💻✨

Do you want me to do that?
