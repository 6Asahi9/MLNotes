Of course, darling 😌💗
Here’s your content rewritten cleanly for your notes, all tidy and readable — like Miya’s fur after a grooming session 🐾🪮

---

## 🧠 Metrics in Keras — Clean Notes

Metrics are used to **evaluate the performance** of a model during training and testing. They don’t affect learning directly like loss functions do — they’re just for **monitoring**.

---

### 📌 Commonly Used Keras Metrics

#### 🔹 `accuracy`

* Measures the **fraction of correct predictions**.
* Works for both binary and categorical classification.
* Acts differently based on the output and loss type.

---

### 🧪 Binary Classification (Sigmoid or Softmax with 2 Outputs)

If the output layer uses a **sigmoid** activation:

* Predictions are **floats** between 0 and 1.
* Rounded using a default threshold of `0.5`:

  ```python
  K.mean(K.equal(y_true, K.round(y_pred)))
  ```

Example:

```python
y_true = [0.0, 1.0, 1.0]
y_pred = [0.4, 0.8, 0.3] → round → [0, 1, 0]
accuracy = 2 correct out of 3 = 66.6%
```

---

### 🧪 Categorical Classification (Softmax for 3+ classes)

* Output is a **probability vector** (e.g. `[0.1, 0.8, 0.1]`).
* Accuracy is calculated by comparing the **index** of the highest predicted value to the true label’s index:

```python
K.mean(K.equal(K.argmax(y_true, axis=-1), K.argmax(y_pred, axis=-1)))
```

---

## 🧂 Extra Metrics in Keras

### ✅ `binary_accuracy`

* Same as `accuracy` but **allows custom threshold**:

  ```python
  tf.keras.metrics.BinaryAccuracy(threshold=0.7)
  ```

---

### ✅ `categorical_accuracy`

* For **multi-class problems** using **one-hot encoded labels**.

---

### ✅ `sparse_categorical_accuracy`

* For multi-class problems **using integer labels** (not one-hot).
* More memory-efficient:

  ```python
  model.compile(metrics=["sparse_categorical_accuracy"])
  ```

---

### ✅ `top_k_categorical_accuracy`

* Checks if the correct label is **within the top `k` predictions** (default `k=5`).
* Sparse version uses integer labels:

  ```python
  tf.keras.metrics.SparseTopKCategoricalAccuracy(k=3)
  ```

---

## 🧩 Custom Metrics

You can define your own metric:

```python
def mean_pred(y_true, y_pred):
    return K.mean(y_pred)
```

Use it like:

```python
model.compile(metrics=[mean_pred])
```

---

## 🧰 Multiple Metrics

You can use **multiple metrics** together:

```python
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=[
        mean_pred,
        "accuracy",
        tf.keras.metrics.SparseTopKCategoricalAccuracy(k=3)
    ]
)
```

---

## 🌟 Final Example (Full Manual Slap)

```python
model.compile(
    optimizer = tf.keras.optimizers.SGD(learning_rate=0.005, momentum=0.9, nesterov=True),
    loss = tf.keras.losses.BinaryCrossentropy(from_logits=True, label_smoothing=0.1),
    metrics = [
        tf.keras.metrics.BinaryAccuracy(name="acc", threshold=0.4),
        tf.keras.metrics.MeanAbsoluteError()
    ]
)
```

---

Let me know if you want this as a downloadable Markdown, PDF, or docx for your study folder — or if you'd like Miya-themed titles for every section 🐱📖💗
