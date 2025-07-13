# 📦 Import necessary libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 🧠 Print TensorFlow version
print(tf.__version__)  # Should be 2.0.0

# 🧵 Load the Fashion MNIST dataset
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# 🧼 Normalize the data
train_images = train_images / 255.0
test_images = test_images / 255.0

# 🐈 Labels for prediction output
labels = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
    'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
]

# 🖼️ Preview a sample image
plt.imshow(train_images[0], cmap='gray')
plt.title(f"Label: {labels[train_labels[0]]}")
plt.show()

# 🏗️ Build the CNN model using Sequential API
model = Sequential([
    Conv2D(32, kernel_size=(3, 3), padding ='SAME', activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(32, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# 🧪 Compile the model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 📐 Reshape the input data to include the channel dimension
train_images = train_images.reshape(-1, 28, 28, 1)
test_images = test_images.reshape(-1, 28, 28, 1)

# 🔁 Train the model
history = model.fit(
    train_images,
    to_categorical(train_labels),
    epochs=1,
    validation_data=(test_images, to_categorical(test_labels))
)

# 📈 Convert training history to a DataFrame
history_df = pd.DataFrame(history.history)

# 📊 Plot loss
plt.plot(history_df['loss'], label='Train Loss')
plt.plot(history_df['val_loss'], label='Val Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()

# 📊 Plot accuracy
plt.plot(history_df['accuracy'], label='Train Acc')
plt.plot(history_df['val_accuracy'], label='Val Acc')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# 🧪 Evaluate the model on test set
test_loss, test_acc = model.evaluate(test_images, to_categorical(test_labels))
print(f"Test accuracy: {test_acc:.4f}")

# 🔮 Make a prediction on a random test image
random_index = np.random.choice(test_images.shape[0])
test_image = test_images[random_index]

# Show the image
plt.imshow(test_image.squeeze(), cmap='gray')
plt.title(f"Actual Label: {labels[test_labels[random_index]]}")
plt.show()

# Expand dimensions for prediction
input_image = np.expand_dims(test_image, axis=0)
predictions = model.predict(input_image)
predicted_class = np.argmax(predictions)

print(f"Predicted Label: {labels[predicted_class]}")
