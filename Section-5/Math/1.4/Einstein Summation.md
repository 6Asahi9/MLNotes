Einstein summation convention is a **shorthand notation** used in mathematics and physics (especially tensor calculus and relativity) to make expressions involving sums more compact.

---

### 📝 **Basic Idea**

* If an index **appears twice** in a single term (once as a subscript and once as a superscript), it means **you automatically sum over it**.
* This removes the need to explicitly write the summation symbol (Σ).

---

### 🔹 **Example Without Einstein Notation**

$$
c_i = \sum_{j=1}^{n} A_{ij} b_j
$$

(This is normal matrix-vector multiplication.)

---

### 🔹 **With Einstein Summation**

$$
c_i = A_{ij} b_j
$$

Because $j$ is repeated, it’s understood we sum over $j$.

---

### ⚡ **Multiple Summations**

If more indices are repeated, summation happens for **each** repeated index:

$$
y = A_{ij} B_{jk} C_{ki} 
$$

This implies:

$$
y = \sum_{i}\sum_{j}\sum_{k} A_{ij} B_{jk} C_{ki}
$$

---

### 🔑 **Rules**

1. **Summation happens only when an index is repeated exactly twice.**
2. **If an index appears once, it’s free** (no summation over it).
3. **No index should appear more than twice** in a single term.

---

Would you like me to show you how this looks in **code** (e.g., using NumPy’s `einsum`), which actually uses this notation?
