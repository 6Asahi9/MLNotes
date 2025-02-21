### What is Kernel PCA?
Kernel Principal Component Analysis (Kernel PCA) is an extension of the traditional PCA that allows it to perform non-linear dimensionality reduction. While regular PCA assumes that the data is linearly separable in its original feature space, Kernel PCA can handle non-linearly separable data by mapping the data into a higher-dimensional space where linear separation is possible.

### Why Use Kernel PCA?
* Non-linearity: When data isn't linearly separable or the relationship between features is not linear, Kernel PCA can still perform well by mapping the data to a higher-dimensional feature space using a kernel trick.
* Flexibility: It uses a variety of kernels (like RBF, Polynomial, or Sigmoid) to transform the data, making it flexible for different kinds of datasets.

### Key Concepts of Kernel PCA:
1. Kernel Trick: Instead of explicitly computing the transformation into higher dimensions (which is computationally expensive), Kernel PCA applies a kernel function to the data. This kernel computes the inner product in the higher-dimensional space without having to compute the transformation explicitly.

2. Popular Kernels:

* RBF (Radial Basis Function): A common kernel for many machine learning tasks. It computes similarity based on the Euclidean distance between points.
* Polynomial Kernel: Computes similarity using polynomial functions, allowing for a broader range of decision boundaries.
* Sigmoid Kernel: A kernel that uses a sigmoid function (based on neural networks).

![](/images/image_2025-02-21_222237386.png)

*add n_components here too just like regular PCA

### Key Points:
* KernelPCA(kernel="rbf", gamma=15): Here, the kernel is set to RBF (Radial Basis Function) with the gamma parameter controlling the spread. You could replace "rbf" with "poly" or "sigmoid" to try other kernel functions.
* fit_transform(X): This applies the Kernel PCA transformation to the input data X, projecting it into a higher-dimensional space where the data can potentially become linearly separable.

![](/images/image_2025-02-21_222344055.png)
