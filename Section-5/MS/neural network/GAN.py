# ✅ Installation (run this in terminal, not in script)
# pip install tensorflow matplotlib

import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import matplotlib.pyplot as plt

### 🧠 Load and Preprocess MNIST Data ###
(X_train, _), (X_test, _) = tf.keras.datasets.mnist.load_data()

# Normalize pixel values to [0, 1]
X_train = X_train.astype('float32') / 255.
X_test = X_test.astype('float32') / 255.

# Flatten images: 28x28 → 784
X_train = X_train.reshape((len(X_train), np.prod(X_train.shape[1:])))
X_test = X_test.reshape((len(X_test), np.prod(X_test.shape[1:])))

### 🔄 AUTOENCODER ###

# Encoder: compress input to 64-dimensional latent space
encoder = models.Sequential([
    layers.Input(shape=(784,)),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu')  # Bottleneck layer
])

# Decoder: reconstruct original image from latent vector
decoder = models.Sequential([
    layers.Input(shape=(64,)),
    layers.Dense(128, activation='relu'),
    layers.Dense(784, activation='sigmoid')  # Output: flattened 28x28 image
])

# Combine encoder and decoder into full autoencoder
autoencoder = models.Sequential([encoder, decoder])
autoencoder.compile(optimizer='adam', loss='mse')

# Train autoencoder
autoencoder.fit(
    X_train, X_train,
    epochs=20,
    batch_size=256,
    validation_data=(X_test, X_test)
)

# Evaluate reconstruction performance
reconstructed_images = autoencoder.predict(X_test)
mse = np.mean(np.square(X_test - reconstructed_images))
print(f'Autoencoder Reconstruction MSE: {mse:.6f}')


### 🧙 GENERATIVE ADVERSARIAL NETWORK (GAN) ###

# Generator: takes random noise → generates fake image
def build_generator():
    model = models.Sequential([
        layers.Dense(128, activation='relu', input_shape=(100,)),
        layers.Dense(784, activation='sigmoid')  # Output: 784 pixels = flattened 28x28 image
    ])
    return model

# Discriminator: takes image → predicts real (1) or fake (0)
def build_discriminator():
    model = models.Sequential([
        layers.Dense(128, activation='relu', input_shape=(784,)),
        layers.Dense(1, activation='sigmoid')  # Output: probability
    ])
    return model

# Instantiate models
generator = build_generator()
discriminator = build_discriminator()

# Compile discriminator (binary classification)
discriminator.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Build GAN by stacking generator and discriminator
gan = models.Sequential([generator, discriminator])
discriminator.trainable = False  # Freeze discriminator during generator training
gan.compile(optimizer='adam', loss='binary_crossentropy')


### 🧪 Training the GAN ###

epochs = 10000
batch_size = 64
half_batch = batch_size // 2

for epoch in range(epochs):
    # --- Train Discriminator ---
    
    # Select real images randomly
    idx = np.random.randint(0, X_train.shape[0], half_batch)
    real_images = X_train[idx]
    real_labels = np.ones((half_batch, 1))  # Label: real = 1

    # Generate fake images from noise
    noise = np.random.normal(0, 1, (half_batch, 100))
    fake_images = generator.predict(noise)
    fake_labels = np.zeros((half_batch, 1))  # Label: fake = 0

    # Train discriminator on real and fake
    d_loss_real = discriminator.train_on_batch(real_images, real_labels)
    d_loss_fake = discriminator.train_on_batch(fake_images, fake_labels)

    # --- Train Generator via GAN ---
    noise = np.random.normal(0, 1, (batch_size, 100))
    gan_labels = np.ones((batch_size, 1))  # Fool discriminator → label as real
    g_loss = gan.train_on_batch(noise, gan_labels)

    # --- Every 1000 epochs: print progress + show samples ---
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Discriminator Loss: {d_loss_real[0]:.4f}, Generator Loss: {g_loss:.4f}")
        
        # Generate 10 sample images
        generated_images = generator.predict(np.random.normal(0, 1, (10, 100)))

        # Display images in 2x5 grid
        plt.figure(figsize=(10, 4))
        for i in range(10):
            plt.subplot(2, 5, i+1)
            plt.imshow(generated_images[i].reshape(28, 28), cmap='gray')
            plt.axis('off')
        plt.tight_layout()
        plt.show()
