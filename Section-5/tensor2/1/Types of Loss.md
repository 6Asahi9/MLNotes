| Task Type                      | Loss Function                     | Use When                                         |
| ------------------------------ | --------------------------------- | ------------------------------------------------ |
| **Binary classification**      | `BinaryCrossentropy()`            | 2 classes (e.g., cat vs no cat)                  |
| **Multiclass classification**  | `CategoricalCrossentropy()`       | More than 2 classes + **one-hot** encoded labels |
|                                | `SparseCategoricalCrossentropy()` | More than 2 classes + **integer labels**         |
| **Regression**                 | `MeanSquaredError()`              | Predicting continuous values (e.g., house price) |
|                                | `MeanAbsoluteError()`             | Less sensitive to outliers than MSE              |
| **Autoencoders / GANs / etc.** | Custom loss                       | When you’re doing something fancy                |
