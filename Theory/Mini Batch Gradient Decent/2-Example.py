import numpy as np

# Simulated dataset (weight -> height)
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # 100 random weights
y = 2.5 + 1.3 * X + np.random.randn(100, 1) * 2  # True height + some noise

# Hyperparameters
alpha = 0.01  # Learning rate
batch_size = 16  # Mini-batch size
epochs = 1000  # Number of passes over the dataset

# Initialize parameters
b, m = 0.0, 0.0  # Intercept and slope

# Mini-Batch Gradient Descent
for epoch in range(epochs):
    indices = np.random.permutation(len(X))  # Shuffle indices
    X_shuffled, y_shuffled = X[indices], y[indices]  # Shuffle data

    for i in range(0, len(X), batch_size):
        X_batch = X_shuffled[i:i + batch_size]
        y_batch = y_shuffled[i:i + batch_size]

        # Predictions
        y_pred = b + m * X_batch

        # Compute gradients for the batch
        db = -2 * np.mean(y_batch - y_pred)
        dm = -2 * np.mean(X_batch * (y_batch - y_pred))

        # Update parameters
        b -= alpha * db
        m -= alpha * dm

    # Optional: Print progress every 100 epochs
    if epoch % 100 == 0:
        print(f"Epoch {epoch}: b = {b:.4f}, m = {m:.4f}")

print(f"Final Model: y = {b:.4f} + {m:.4f} * x")
