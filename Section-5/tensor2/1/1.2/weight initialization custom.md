

### 🧱 **Basic Model with Initializers**

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Conv1D, MaxPooling1D

# Construct a model
model = Sequential([
    Conv1D(filters=16, 
           kernel_size=3, 
           input_shape=(128, 64), 
           kernel_initializer='random_uniform', 
           bias_initializer='zeros', 
           activation='relu'),
    
    MaxPooling1D(pool_size=4),
    
    Flatten(),
    
    Dense(64, 
          kernel_initializer='he_uniform', 
          bias_initializer='ones', 
          activation='relu'),
])
```

> 🧠 **Note:** Here, we use common initializer **strings** like `'random_uniform'`, `'he_uniform'`, and `'ones'`. These are useful for quick setup.

---

### 🧪 **Initializers with Parameters**

```python
import tensorflow as tf

# Add more layers using instantiated initializers with custom arguments
model.add(Dense(64, 
                kernel_initializer=tf.keras.initializers.RandomNormal(mean=0.0, stddev=0.05), 
                bias_initializer=tf.keras.initializers.Constant(value=0.4), 
                activation='relu'))

model.add(Dense(8, 
                kernel_initializer=tf.keras.initializers.Orthogonal(gain=1.0, seed=None), 
                bias_initializer=tf.keras.initializers.Constant(value=0.4), 
                activation='relu'))
```

> 🧠 **Note:** When using `tf.keras.initializers.SomeInitializer(...)`, we gain full control over how weights and biases are generated.

---

### 🔧 **Custom Weight Initializer**

```python
import tensorflow.keras.backend as K

# Define a custom initializer function
def my_init(shape, dtype=None):
    return K.random_normal(shape, dtype=dtype)

# Use it in a layer
model.add(Dense(64, kernel_initializer=my_init))
```

> 🧠 **Note:** Custom initializers must accept `shape` and `dtype`. You can define any logic inside — from Gaussian noise to your own distribution.

---

### 📊 **Visualizing Weights and Biases**

```python
import matplotlib.pyplot as plt

# Plot histograms of initialized weights and biases
fig, axes = plt.subplots(5, 2, figsize=(12,16))
fig.subplots_adjust(hspace=0.5, wspace=0.5)

# Ignore layers like pooling/flatten with no weights
weight_layers = [layer for layer in model.layers if len(layer.weights) > 0]

for i, layer in enumerate(weight_layers):
    for j in [0, 1]:
        axes[i, j].hist(layer.weights[j].numpy().flatten(), align='left')
        axes[i, j].set_title(layer.weights[j].name)
```

> 🧠 **Note:** Use this visualization to compare the effects of different initializers. Watch for variance, symmetry, and outliers.

---

### 🧾 Summary

```python
# Print model summary to confirm structure
model.summary()
```

---

Let me know if you'd like:

* 📚 Markdown version
* 📐 Annotated diagram explaining `kernel_initializer` vs `bias_initializer`
* 🎨 Miya-themed cover page that says "Neural Nets and Their Delicious Initializers: Approved by Miya 🐾"

Your notebook is already elite, but let’s make it *paw-sitively* perfect 😼.
