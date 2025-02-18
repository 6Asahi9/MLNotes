# Importing necessary libraries
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Preprocessing the Training set
# ImageDataGenerator applies real-time data augmentation and rescaling to the training set
train_datagen = ImageDataGenerator(rescale = 1./255,        # Rescaling pixel values to [0, 1]
                                   shear_range = 0.2,       # Randomly shears the image
                                   zoom_range = 0.2,        # Randomly zooms in on the image
                                   horizontal_flip = True)  # Randomly flips the image horizontally
# Loading images from the training set directory, resized to 64x64, with binary labels
training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size = (64, 64),  # Resizing images to 64x64
                                                 batch_size = 32,          # Batch size of 32 images
                                                 class_mode = 'binary')    # Binary classification (cat or dog)

# Preprocessing the Test set
# Just rescaling the pixel values for the test set (no augmentation)
test_datagen = ImageDataGenerator(rescale = 1./255)  # Rescaling test set images
# Loading images from the test set directory, resized to 64x64, with binary labels
test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size = (64, 64),  # Resizing images to 64x64
                                            batch_size = 32,          # Batch size of 32 images
                                            class_mode = 'binary')    # Binary classification (cat or dog)

# Initialising the CNN
# Starting the sequential model for the Convolutional Neural Network
cnn = tf.keras.models.Sequential()

# Adding the first convolutional layer
cnn.add(tf.keras.layers.Conv2D(filters=32,                 # 32 filters to detect features
                               kernel_size=3,             # 3x3 kernel to look at image regions
                               activation='relu',         # ReLU activation function for non-linearity
                               input_shape=[64, 64, 3]))  # Input image shape: 64x64 with 3 color channels (RGB)

# Adding the first max-pooling layer to downsample the image and reduce dimensionality
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))  # 2x2 pooling window, moves 2 steps at a time

# Adding the second convolutional layer
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'))  # Another 3x3 convolution

# Adding the second max-pooling layer
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))  # Another 2x2 pooling window

# Flattening the pooled feature maps into a 1D vector
cnn.add(tf.keras.layers.Flatten())  # Flatten the 2D pooled features into a 1D vector for the Dense layer

# Adding a fully connected (dense) layer with 128 units and ReLU activation
cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))  # Dense layer with 128 neurons

# Adding the final output layer with 1 neuron and a sigmoid activation function
cnn.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))  # Sigmoid activation for binary output (cat or dog)

# Training the CNN
# Compiling the CNN model with an optimizer, loss function, and metric for evaluation
cnn.compile(optimizer = 'adam',           # Adam optimizer for efficient training
            loss = 'binary_crossentropy',  # Binary cross-entropy for binary classification
            metrics = ['accuracy'])       # Measuring accuracy during training

# Training the CNN on the training set and evaluating it on the test set for 25 epochs
cnn.fit(x = training_set,                # Training data
        validation_data = test_set,       # Test data for validation
        epochs = 25)                      # Number of times to train the model

# Making a single prediction on a new image
import numpy as np
from tensorflow.keras.preprocessing import image

# Loading and preparing the test image
test_image = image.load_img('dataset/single_prediction/cat_or_dog_1.jpg', target_size = (64, 64))  # Load image and resize
test_image = image.img_to_array(test_image)  # Convert image to array
test_image = np.expand_dims(test_image, axis = 0)  # Expand dimensions to match the input shape for prediction

# Predicting the class of the image using the trained CNN model
result = cnn.predict(test_image)

# Retrieving the class indices to map predictions to labels
training_set.class_indices

# If the prediction is 1 (dog), return "dog", otherwise "cat"
if result[0][0] == 1:
  prediction = 'dog'
else:
  prediction = 'cat'

# Printing the prediction
print(prediction)
