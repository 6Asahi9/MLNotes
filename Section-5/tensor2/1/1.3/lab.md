
1. Loading the data
2. Splitting & normalizing
3. Building, training, validating the model
4. Adding regularisation
5. Using callbacks (custom & early stopping)
6. Plotting results

We'll use the **Diabetes dataset** from `sklearn`.

---

## ✅ Step 1: Load and preprocess the data

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras import regularizers
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load the diabetes dataset
diabetes = load_diabetes()
data, targets = diabetes.data, diabetes.target

# Normalize the target variable (helps with smoother training curves)
targets = (targets - targets.mean()) / targets.std()

# Split into train and test sets
train_data, test_data, train_targets, test_targets = train_test_split(
    data, targets, test_size=0.2, random_state=42
)
```

---

## ✅ Step 2: Build and train a simple feedforward model (with validation)

```python
# Build a basic model
model = Sequential([
    Dense(128, activation='relu', input_shape=(train_data.shape[1],)),
    Dense(64, activation='relu'),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train with validation split
history = model.fit(
    train_data, train_targets,
    validation_split=0.2,
    epochs=100,
    batch_size=16,
    verbose=0
)

# Evaluate on test set
test_loss, test_mae = model.evaluate(test_data, test_targets)
print(f"Test loss: {test_loss:.4f}, Test MAE: {test_mae:.4f}")
```

---

## ✅ Step 3: Plot training vs validation loss

```python
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Loss vs. Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Training', 'Validation'], loc='upper right')
plt.show()
```

---

## ✅ Step 4: Add Regularisation (weight decay & dropout)

```python
def get_regularised_model(wd, dropout_rate):
    model = Sequential([
        Dense(128, activation='relu', input_shape=(train_data.shape[1],),
              kernel_regularizer=regularizers.l2(wd)),
        Dropout(dropout_rate),
        Dense(64, activation='relu', kernel_regularizer=regularizers.l2(wd)),
        Dropout(dropout_rate),
        Dense(1)
    ])
    return model

reg_model = get_regularised_model(wd=1e-4, dropout_rate=0.3)

reg_model.compile(optimizer='adam', loss='mse', metrics=['mae'])

reg_history = reg_model.fit(
    train_data, train_targets,
    validation_split=0.2,
    epochs=100,
    batch_size=16,
    verbose=0
)

reg_model.evaluate(test_data, test_targets)
```

---

## ✅ Step 5: Custom Callback (print when val\_loss drops below 0.25)

```python
class PrintValLoss(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        val_loss = logs.get('val_loss')
        if val_loss < 0.25:
            print(f"\nEpoch {epoch+1}: Validation loss dropped below 0.25: {val_loss:.4f}")

custom_callback = PrintValLoss()

model_with_callback = get_regularised_model(1e-4, 0.3)
model_with_callback.compile(optimizer='adam', loss='mse', metrics=['mae'])

model_with_callback.fit(
    train_data, train_targets,
    validation_split=0.2,
    epochs=100,
    batch_size=16,
    callbacks=[custom_callback],
    verbose=0
)
```

---

## ✅ Step 6: Early Stopping (with patience)

```python
early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=10,  # Stop if val_loss doesn't improve for 10 epochs
    restore_best_weights=True
)

early_model = get_regularised_model(1e-4, 0.3)
early_model.compile(optimizer='adam', loss='mse', metrics=['mae'])

early_history = early_model.fit(
    train_data, train_targets,
    validation_split=0.2,
    epochs=100,
    batch_size=16,
    callbacks=[early_stopping],
    verbose=0
)

early_model.evaluate(test_data, test_targets)
```

---

## ✅ Step 7: Plot all learning curves (Unregularised vs Regularised)

```python
fig = plt.figure(figsize=(12, 5))

# Unregularised
fig.add_subplot(121)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Unregularised Model')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Training', 'Validation'])

# Regularised
fig.add_subplot(122)
plt.plot(reg_history.history['loss'])
plt.plot(reg_history.history['val_loss'])
plt.title('Regularised Model')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Training', 'Validation'])

plt.tight_layout()
plt.show()
```

---
