import subprocess

# Install required packages (machine learning library and TensorFlow)
subprocess.check_call(["pip", "install", "scikit-learn", "tensorflow"])

# Install the TensorFlow Model Optimization Toolkit for pruning/quantization
!pip install tensorflow-model-optimization

# Note: Azure ML kernel uses Python 3.8; 
# installing tf-keras separately is needed for optimization toolkit to work properly
!conda install tf-keras

# Import TensorFlow and optimization toolkit
import tensorflow_model_optimization as tfmot
import tensorflow as tf
from tensorflow.keras.datasets import mnist

# Load the MNIST dataset (handwritten digits)
# Normalize pixel values to the range [0, 1]
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build a simple neural network for digit classification
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),        # Flatten 28x28 images into 1D
    tf.keras.layers.Dense(128, activation='relu'),        # Fully connected layer
    tf.keras.layers.Dropout(0.2),                         # Dropout for regularization
    tf.keras.layers.Dense(10, activation='softmax')       # Output layer (10 classes)
])

# Compile the model (define optimizer, loss function, and metric)
model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

# Train the base model
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# ----------------- APPLY MODEL PRUNING -----------------

# Define pruning parameters:
# Start with 0% sparsity and gradually increase to 50% by step 1000
pruning_params = {
    'pruning_schedule': tfmot.sparsity.keras.PolynomialDecay(
        initial_sparsity=0.0, 
        final_sparsity=0.5, 
        begin_step=0, 
        end_step=1000
    )
}

# Apply pruning to reduce model size (remove less important weights)
pruned_model = tfmot.sparsity.keras.prune_low_magnitude(model, **pruning_params)

# Re-compile the pruned model
pruned_model.compile(optimizer='adam', 
                     loss='sparse_categorical_crossentropy', 
                     metrics=['accuracy'])

# Train the pruned model (pruning is applied during training)
callbacks = [tfmot.sparsity.keras.UpdatePruningStep()]
pruned_model.fit(x_train, y_train, epochs=2, validation_data=(x_test, y_test), callbacks=callbacks)

# Remove pruning-specific layers and metadata for final deployment
pruned_model = tfmot.sparsity.keras.strip_pruning(pruned_model)

# ----------------- CONVERT TO TFLITE WITH QUANTIZATION -----------------

# Convert the pruned Keras model to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(pruned_model)

# Enable optimization (quantization) to reduce model size and improve efficiency
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# Perform the conversion
quantized_model = converter.convert()
