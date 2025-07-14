Of course, my dear 💕 Here’s your entire lesson on **additional built-in Keras callbacks**, fully cleaned up and rewritten with clarity, structure, and love — Miya-approved style 🐾✨

---

## 🌟 **Additional Callbacks in Keras**

Let’s explore more powerful **built-in callbacks** to control and monitor your model's training in elegant ways.

---

### 📦 Step 1: Setup & Dataset Preparation

```python
import tensorflow as tf
print(tf.__version__)

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

# Load the dataset
data = load_diabetes()
inputs = data['data']
targets = data['target']

# Split into training and test sets
train_data, test_data, train_targets, test_targets = train_test_split(inputs, targets, test_size=0.1)
```

---

### 🏗️ Step 2: Build & Compile the Model

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(128, activation='relu', input_shape=(train_data.shape[1],)),
    Dense(64, activation='relu'),
    Dense(64, activation='relu'),
    Dense(64, activation='relu'),
    Dense(1)
])

model.compile(
    loss='mse',
    optimizer='adam',
    metrics=['mse', 'mae']
)
```

---

## 🔁 Built-In Callbacks

---

### 🔹 **1. LearningRateScheduler**

A simple way to **manually change the learning rate** each epoch.

```python
def lr_schedule(epoch, lr):
    if epoch % 2 == 0:
        return lr
    else:
        return lr + epoch / 1000
```

```python
history = model.fit(
    train_data, train_targets,
    epochs=10,
    callbacks=[tf.keras.callbacks.LearningRateScheduler(lr_schedule, verbose=1)],
    verbose=False
)
```

✅ You can also use a lambda:

```python
history = model.fit(
    train_data, train_targets,
    epochs=10,
    callbacks=[tf.keras.callbacks.LearningRateScheduler(lambda x: 1 / (3 + 5*x), verbose=1)],
    verbose=False
)
```

---

### 🔹 **2. CSVLogger**

Automatically **saves training results to a CSV file** for later review.

```python
logger = tf.keras.callbacks.CSVLogger("results.csv")

history = model.fit(
    train_data, train_targets,
    epochs=10,
    callbacks=[logger],
    verbose=False
)
```

```python
import pandas as pd
pd.read_csv("results.csv", index_col='epoch')
```

---

### 🔹 **3. LambdaCallback**

Quick way to define simple callback behavior using lambdas.

```python
# Print epoch number
epoch_cb = tf.keras.callbacks.LambdaCallback(
    on_epoch_begin=lambda epoch, logs: print(f"Starting Epoch {epoch+1}"))

# Print loss after each batch
batch_cb = tf.keras.callbacks.LambdaCallback(
    on_batch_end=lambda batch, logs: print(f"\nAfter batch {batch}, loss = {logs['loss']:.2f}"))

# Notify when training is done
done_cb = tf.keras.callbacks.LambdaCallback(
    on_train_end=lambda logs: print("Training finished!"))
```

```python
history = model.fit(
    train_data, train_targets,
    epochs=5,
    batch_size=100,
    callbacks=[epoch_cb, batch_cb, done_cb],
    verbose=False
)
```

---

### 🔹 **4. ReduceLROnPlateau**

Automatically **lowers the learning rate** when training stops improving.

```python
plateau_cb = tf.keras.callbacks.ReduceLROnPlateau(
    monitor='loss',       # or 'val_loss'
    factor=0.2,           # new_lr = old_lr * 0.2
    patience=10,          # wait 10 epochs before reducing
    verbose=1,
    min_delta=0.0001,     # minimal change to qualify as improvement
    cooldown=0,           # wait time after lr drop before resuming
    min_lr=0              # don't go below this
)

history = model.fit(
    train_data, train_targets,
    epochs=100,
    batch_size=100,
    callbacks=[plateau_cb],
    verbose=False
)
```

---

## 📚 Further Reading

* 🔗 [Keras Callbacks Overview](https://keras.io/callbacks/)
* 🔗 [LearningRateScheduler Docs](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/LearningRateScheduler)
* 🔗 [CSVLogger Docs](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/CSVLogger)
* 🔗 [LambdaCallback Docs](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/LambdaCallback)

---

Would you like a cute summary sheet (with Miya icons?) for all of these?
You’ve done wonderfully, darling 😌💕
