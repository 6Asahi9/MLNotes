import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np

### 🌸 FEEDFORWARD NEURAL NETWORK (FNN) on IRIS ###

# Load the classic Iris dataset
iris = load_iris()
X = iris.data                                # Shape: (150, 4) — features
y = iris.target.reshape(-1, 1)               # Shape: (150, 1) — class labels

# One-hot encode the target labels (3 classes → [1, 0, 0] etc.)
encoder = OneHotEncoder(sparse=False)
y = encoder.fit_transform(y)

# Split the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Build a simple feedforward neural network for classification
model_fnn = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),  # Input: 4 features
    layers.Dense(32, activation='relu'),
    layers.Dense(3, activation='softmax')  # Output: 3 classes
])

# Compile and train the model
model_fnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model_fnn.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))


### 🧠 CONVOLUTIONAL NEURAL NETWORK (CNN) on CIFAR-10 ###

# Load CIFAR-10 dataset: 60,000 color images (32x32x3), 10 classes
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.cifar10.load_data()

# Normalize images to [0, 1] range
train_images, test_images = train_images / 255.0, test_images / 255.0

# Build a simple CNN
model_cnn = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),  # First conv layer
    layers.MaxPooling2D((2, 2)),                                           # Downsample
    layers.Conv2D(64, (3, 3), activation='relu'),                          # More filters
    layers.MaxPooling2D((2, 2)),                                           # Downsample again
    layers.Flatten(),                                                     # Flatten for dense layers
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')                                # Output: 10 classes
])

# Compile and train the model
model_cnn.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model_cnn.fit(train_images, train_labels, epochs=10, batch_size=64, validation_data=(test_images, test_labels))


### 🌊 RECURRENT NEURAL NETWORK (RNN) on SINE WAVE ###

# Create synthetic sine wave data
t = np.linspace(0, 100, 10000)
X = np.sin(t).reshape(-1, 1)  # Shape: (10000, 1)

# Create sequences from the sine wave for time series prediction
def create_sequences(data, seq_length):
    X_seq, y_seq = [], []
    for i in range(len(data) - seq_length):
        X_seq.append(data[i:i+seq_length])
        y_seq.append(data[i+seq_length])
    return np.array(X_seq), np.array(y_seq)

seq_length = 100
X_seq, y_seq = create_sequences(X, seq_length)  # Predict the next value from the last 100

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_seq, y_seq, test_size=0.2, random_state=42
)

# Build a simple RNN model for regression
model_rnn = models.Sequential([
    layers.SimpleRNN(128, input_shape=(seq_length, 1)),  # Input shape: (100, 1)
    layers.Dense(1)  # Predict the next sine wave value
])

# Compile and train the model
model_rnn.compile(optimizer='adam', loss='mse')
model_rnn.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))
