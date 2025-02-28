import numpy as np

# Sample data (Weight -> Height prediction)
X = np.array([50, 60, 70, 80, 90])  # Input (Weight)
Y = np.array([150, 160, 170, 180, 190])  # True Height

# Hyperparameters
alpha = 0.01  # Learning rate
batch_size = 2  # Mini-batch size
epochs = 1000  # Number of iterations

# Initialize parameters
b, m = 0, 0  # Intercept and slope

# Training loop
for epoch in range(epochs):
    # Shuffle data before each epoch
    indices = np.random.permutation(len(X))
    X_shuffled, Y_shuffled = X[indices], Y[indices]
    
    for i in range(0, len(X), batch_size):
        # Create mini-batch
        X_batch = X_shuffled[i:i+batch_size]
        Y_batch = Y_shuffled[i:i+batch_size]
        
        # Compute gradients for mini-batch
        dj_db = -2 * np.mean(Y_batch - (b + m * X_batch))
        dj_dm = -2 * np.mean(X_batch * (Y_batch - (b + m * X_batch)))
        
        # Update parameters
        b -= alpha * dj_db
        m -= alpha * dj_dm

print(f"Final intercept (b): {b}, Final slope (m): {m}")
