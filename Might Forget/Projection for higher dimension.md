Nice — let’s do it. 😌

We want the orthogonal projection of (v=\begin{bmatrix}12\0\0\end{bmatrix}) onto (U=\operatorname{span}{u_1,u_2}) where
(u_1=\begin{bmatrix}1\1\1\end{bmatrix},; u_2=\begin{bmatrix}0\1\2\end{bmatrix}.)

Form the Gram matrix and right-hand side:
[
G=A^T A=\begin{bmatrix}u_1\cdot u_1 & u_1\cdot u_2[4pt] u_2\cdot u_1 & u_2\cdot u_2\end{bmatrix}
=\begin{bmatrix}3 & 3[4pt] 3 & 5\end{bmatrix},\qquad
A^T v=\begin{bmatrix}u_1\cdot v[4pt] u_2\cdot v\end{bmatrix}=\begin{bmatrix}12[4pt]0\end{bmatrix}.
]

Solve (G\begin{bmatrix}c_1\c_2\end{bmatrix}=A^T v):
[
\begin{cases}
3c_1+3c_2=12 \Rightarrow c_1+c_2=4,[4pt]
3c_1+5c_2=0.
\end{cases}
]
From these: (2c_2=-12 \Rightarrow c_2=-6,; c_1=10.)

So the projection is
[
\operatorname{proj}_U(v)=c_1u_1+c_2u_2
=10\begin{bmatrix}1\1\1\end{bmatrix}-6\begin{bmatrix}0\1\2\end{bmatrix}
=\begin{bmatrix}10\4\-2\end{bmatrix}.
]

Check: the error (v-\operatorname{proj}_U(v)=\begin{bmatrix}2\-4\2\end{bmatrix}) is orthogonal to both (u_1) and (u_2) (dot products = 0), so the projection is correct.

Final answer:
[
\boxed{\operatorname{proj}_U!\begin{bmatrix}12\0\0\end{bmatrix}=\begin{bmatrix}10\4\-2\end{bmatrix}.}

----------------

Excellent catch, Asahi — you’re absolutely right 💡

That formula
[
\operatorname{proj}_{\langle w\rangle}(v) = \frac{v\cdot w}{w\cdot w}, w
]
is **the projection formula for a *1-dimensional* subspace**, meaning the subspace is spanned by **a single vector** (w).

---

### Here’s the difference clearly:

| Case                                                              | Subspace                            | Formula                                                                                  |
| ----------------------------------------------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------- |
| 1D (spanned by one vector (w))                                    | (U = \text{span}{w})                | (\displaystyle \operatorname{proj}_U(v) = \frac{v\cdot w}{w\cdot w},w)                   |
| Higher dimension (spanned by multiple vectors (u_1, u_2, …, u_k)) | (U = \text{span}{u_1, u_2, …, u_k}) | (\displaystyle \operatorname{proj}_U(v) = A(A^TA)^{-1}A^T v) where (A = [u_1;u_2;…;u_k]) |

---

In your last question, the subspace was spanned by **two vectors**
[
u_1 = \begin{bmatrix}1\0\0\end{bmatrix}, \quad u_2 = \begin{bmatrix}0\1\1\end{bmatrix},
]
so it’s a **2-dimensional** subspace (a plane).
That’s why we used the matrix-form formula.

If it had been just one vector — say only ([0,1,1]^T) — then the shorter
[
\frac{v\cdot w}{w\cdot w} w
]
formula would’ve worked perfectly.

Would you like me to show how both formulas give the same result when the subspace has only one vector?

]

Want me to show this using an orthonormal basis (Gram–Schmidt) too, or is this good? 🐾
