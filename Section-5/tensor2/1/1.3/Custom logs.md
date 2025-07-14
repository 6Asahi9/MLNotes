Absolutely, my darling! 💖 Here's a cleaned-up, beautifully structured version of the entire lesson on **callbacks using the logs dictionary**, rewritten in my style — crystal clear, nicely commented, and beginner-friendly, just how Miya would expect 🐾✨

---

## 🧠 **Using the `logs` Dictionary in Custom Callbacks (TensorFlow/Keras)**

In Keras, callbacks allow us to inject custom behavior during training, evaluation, and prediction. The `logs` dictionary is passed to many callback methods and contains useful info like **loss**, **metrics**, etc.

---

### 📦 Step 1: Load & Prepare the Dataset

```python
import tensorflow as tf
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

# Load the diabetes dataset
diabetes = load_diabetes()
data = diabetes['data']
targets = diabetes['target']

# Split into training and test sets
train_data, test_data, train_targets, test_targets = train_test_split(data, targets, test_size=0.1)
```

---

### 🏗️ Step 2: Build the Model

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization

model = Sequential([
    Dense(128, activation='relu', input_shape=(train_data.shape[1],)),
    Dense(64, activation='relu'),
    BatchNormalization(),
    Dense(64, activation='relu'),
    Dense(64, activation='relu'),
    Dense(1)
])
```

---

### ⚙️ Step 3: Compile the Model

```python
model.compile(
    loss='mse',
    optimizer='adam',
    metrics=['mae']
)
```

---

### 🧩 Step 4: Create a Custom Callback with `logs`

```python
class LossAndMetricCallback(tf.keras.callbacks.Callback):
    
    def on_train_batch_end(self, batch, logs=None):
        if batch % 2 == 0:
            print(f"\nAfter training batch {batch}, loss = {logs['loss']:.2f}")
    
    def on_test_batch_end(self, batch, logs=None):
        print(f"\nAfter testing batch {batch}, loss = {logs['loss']:.2f}")
    
    def on_epoch_end(self, epoch, logs=None):
        print(f"Epoch {epoch + 1}: loss = {logs['loss']:.2f}, MAE = {logs['mae']:.2f}")
    
    def on_predict_batch_end(self, batch, logs=None):
        print(f"Finished prediction on batch {batch}")
```

---

### 🚀 Step 5: Train the Model with the Custom Callback

```python
history = model.fit(
    train_data, train_targets,
    epochs=20,
    batch_size=100,
    callbacks=[LossAndMetricCallback()],
    verbose=False
)
```

---

### 🧪 Step 6: Use the Callback in Evaluation and Prediction

```python
# Evaluation
model.evaluate(
    test_data, test_targets,
    batch_size=10,
    callbacks=[LossAndMetricCallback()],
    verbose=False
)

# Prediction
model.predict(
    test_data,
    batch_size=10,
    callbacks=[LossAndMetricCallback()],
    verbose=False
)
```

---

## 🎯 Application: Custom Learning Rate Scheduler Callback

---

### 🧭 Step 1: Define the Learning Rate Schedule

```python
lr_schedule = [
    (4, 0.03),
    (7, 0.02),
    (11, 0.005),
    (15, 0.007)
]

def get_new_epoch_lr(epoch, current_lr):
    for scheduled_epoch, new_lr in lr_schedule:
        if epoch == scheduled_epoch:
            return new_lr
    return current_lr
```

---

### 🛠️ Step 2: Define the Scheduler Callback

```python
class LRScheduler(tf.keras.callbacks.Callback):
    def __init__(self, schedule_fn):
        super().__init__()
        self.schedule_fn = schedule_fn

    def on_epoch_begin(self, epoch, logs=None):
        if not hasattr(self.model.optimizer, 'lr'):
            raise ValueError("Optimizer has no learning rate to adjust.")

        current_lr = float(tf.keras.backend.get_value(self.model.optimizer.lr))
        updated_lr = self.schedule_fn(epoch, current_lr)

        tf.keras.backend.set_value(self.model.optimizer.lr, updated_lr)
        print(f"Epoch {epoch + 1}: Learning rate set to {updated_lr:.4f}")
```

---

### 🔁 Step 3: Train Model with Learning Rate Scheduler

```python
# Rebuild model
new_model = Sequential([
    Dense(128, activation='relu', input_shape=(train_data.shape[1],)),
    Dense(64, activation='relu'),
    BatchNormalization(),
    Dense(64, activation='relu'),
    Dense(64, activation='relu'),
    Dense(1)
])

new_model.compile(
    loss='mse',
    optimizer='adam',
    metrics=['mae', 'mse']
)

# Fit with learning rate scheduler callback
new_history = new_model.fit(
    train_data, train_targets,
    epochs=20,
    batch_size=100,
    callbacks=[LRScheduler(get_new_epoch_lr)],
    verbose=False
)
```

---

## 📚 Further Resources

* [Keras: Custom Callbacks](https://www.tensorflow.org/guide/keras/custom_callback)
* [Keras Callback API](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/Callback)

---

Would you like me to turn this cleaned-up version into:

* A downloadable notebook (`.ipynb`)?
* A printable PDF study sheet?
* Or something Miya-themed? 🐾✨
