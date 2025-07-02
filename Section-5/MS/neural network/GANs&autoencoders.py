import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
from tensorflow.keras.datasets import mnist

### 🧠 GAN SECTION ###

# Generator: Takes random noise and tries to create something that looks like a real image
def build_generator():
    model = models.Sequential([
        layers.Dense(128, activation='relu', input_shape=(100,)),     # Expand the 100D noise
        layers.Dense(784, activation='sigmoid')                       # Output: 28x28 = 784 pixels (flattened image)
    ])
    return model

# Discriminator: Tries to decide if an input image is real (from dataset) or fake (from generator)
def build_discriminator():
    model = models.Sequential([
        layers.Dense(128, activation='relu', input_shape=(784,)),     # Input: flattened image
        layers.Dense(1, activation='sigmoid')                         # Output: 1 neuron for binary classification (real/fake)
    ])
    return model

# Load the MNIST dataset (handwritten digits)
(X_train, _), (_, _) = mnist.load_data()

# Normalize images to [-1, 1] and flatten them to shape (784,) to feed into the models
X_train = (X_train.astype(np.float32) - 127.5) / 127.5
X_train = X_train.reshape(-1, 784)

print(f"X_train shape: {X_train.shape}")  # Debugging sanity check

# Build and compile models
generator = build_generator()
discriminator = build_discriminator()
discriminator.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Stack generator + discriminator to form the full GAN model
gan = models.Sequential([generator, discriminator])
discriminator.trainable = False  # Lock discriminator weights during GAN training
gan.compile(optimizer='adam', loss='binary_crossentropy')

# Training config
epochs = 1000
batch_size = 32
half_batch = batch_size // 2

# Main training loop
for epoch in range(epochs):
    # Step 1: Train discriminator on real images
    idx = np.random.randint(0, X_train.shape[0], half_batch)
    real_imgs = X_train[idx]
    real_labels = np.ones((half_batch, 1))  # Label: 1 = real

    # Step 2: Train discriminator on fake images
    noise = np.random.normal(0, 1, (half_batch, 100))
    fake_imgs = generator.predict(noise)
    fake_labels = np.zeros((half_batch, 1))  # Label: 0 = fake

    # Update discriminator weights using both real and fake batches
    d_loss_real = discriminator.train_on_batch(real_imgs, real_labels)
    d_loss_fake = discriminator.train_on_batch(fake_imgs, fake_labels)

    # Step 3: Train generator (via GAN): try to make the discriminator think generated images are real
    noise = np.random.normal(0, 1, (batch_size, 100))
    gan_labels = np.ones((batch_size, 1))  # Try to trick the discriminator: label as real (1)
    g_loss = gan.train_on_batch(noise, gan_labels)

    # Occasionally log progress
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Discriminator Loss: {d_loss_real[0]}, Generator Loss: {g_loss}")

### 🪞 AUTOENCODER SECTION ###

# Encoder: Compress 784-dimensional input into a smaller latent representation
def build_encoder():
    input_img = layers.Input(shape=(784,))
    encoded = layers.Dense(128, activation='relu')(input_img)
    encoded = layers.Dense(64, activation='relu')(encoded)
    return models.Model(input_img, encoded)

# Decoder: Reconstruct the image from the latent 64-dimensional vector
def build_decoder():
    encoded_input = layers.Input(shape=(64,))
    decoded = layers.Dense(128, activation='relu')(encoded_input)
    decoded = layers.Dense(784, activation='sigmoid')(decoded)
    return models.Model(encoded_input, decoded)

# Build the full autoencoder model by chaining encoder and decoder
encoder = build_encoder()
decoder = build_decoder()

input_img = layers.Input(shape=(784,))
encoded_img = encoder(input_img)
decoded_img = decoder(encoded_img)

autoencoder = models.Model(input_img, decoded_img)

# Compile and train the autoencoder to reconstruct input images
autoencoder.compile(optimizer='adam', loss='mse')

# 💥 WARNING: X_test is not defined — make sure to load it if you want validation
autoencoder.fit(X_train, X_train, epochs=50, batch_size=256)
