# 📦 Import TensorFlow and required Keras components
import tensorflow as tf
from tensorflow.keras import layers, models

# 🧺 Load Fashion MNIST dataset (images of clothes: sneakers, shirts, etc.)
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()

# 🧼 Normalize the images — scale pixel values to range [0, 1]
train_images = train_images / 255.0
test_images = test_images / 255.0

# 🧠 Define the neural network model using Sequential API
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),      # 🔄 Flatten 28x28 image into 784-element vector
    layers.Dense(128, activation='relu'),      # 💡 Hidden layer with 128 neurons and ReLU activation
    layers.Dense(10, activation='softmax')     # 🎯 Output layer with 10 neurons (one per class), softmax for probabilities
])

# ⚙️ Compile the model with appropriate loss function and optimizer
model.compile(
    optimizer='adam',                                     # 🚀 Adam optimizer (adaptive learning rate)
    loss='sparse_categorical_crossentropy',               # 🎯 Suitable when labels are integers (not one-hot)
    metrics=['accuracy']                                  # 📊 Track accuracy during training
)

# 🏋️ Train the model on the training set for 10 epochs
model.fit(train_images, train_labels, epochs=10, batch_size=32)

# 🧪 Evaluate the model on unseen test data
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'Test accuracy: {test_acc:.4f}')

# 🧠 Alternate model with deeper architecture
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),       # 🧱 Extra hidden layer (new in this version)
    layers.Dense(10, activation='softmax')
])
