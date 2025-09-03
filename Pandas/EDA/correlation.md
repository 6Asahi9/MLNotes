Ahhh, Asahi, back to stats! 🐾

`pearsonr` is a **function in Python (from `scipy.stats`)** that calculates the **Pearson correlation coefficient** between two variables, **and also gives a p-value** to tell you how statistically significant that correlation is.

---

### **1️⃣ What it does**

* Measures **linear correlation** between two variables.
* Returns **two values**: `(r, p)`

  * `r` → correlation coefficient (between -1 and 1)
  * `p` → p-value (how confident we are that this correlation isn’t by chance)

---

### **2️⃣ Example**

```python
from scipy.stats import pearsonr

x = [1, 2, 3, 4, 5]   # hours studied
y = [50, 60, 65, 80, 90]  # marks scored

r, p = pearsonr(x, y)
print("r =", r)
print("p-value =", p)
```

Output might be something like:

```
r = 0.9819805061   # very strong positive correlation
p-value = 0.0005   # very significant
```

* `r = 0.98` → strong positive correlation (as x increases, y increases)
* `p = 0.0005` → correlation is statistically significant

---

### **3️⃣ Key points**

* `r = 1` → perfect positive correlation
* `r = -1` → perfect negative correlation
* `r = 0` → no linear correlation
* Small p-value (<0.05) → correlation is unlikely to be by chance

---

💡 **Think of it like:**
Miya’s **purr level vs number of treats**. `pearsonr` tells you both **how strongly the purrs follow the treats** and **whether it’s significant or just random fluff behavior**. 😹

---

If you want, I can also **show a tiny visual example** with Miya treats and purrs so you can *see Pearson correlation in action* — it makes it much easier to grasp.

Do you want me to do that?
