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
]

Want me to show this using an orthonormal basis (Gram–Schmidt) too, or is this good? 🐾
