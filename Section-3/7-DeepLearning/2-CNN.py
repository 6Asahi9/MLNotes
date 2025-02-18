# Importing necessary libraries
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Preprocessing the Training set
# The ImageDataGenerator is used to preprocess and augment images
train_datagen = ImageDataGenerator(rescale = 1./255,   # Normalizing pixel values (0-255 to 0-1)
                                   shear_range = 0.2,   # Random shear transformation for data augmentation
                                   zoom_range = 0.2,    # Random zoom transformation for data augmentation
                                   horizontal_flip = True)  # Random horizontal flipping for data augmentation

# Loading images from the training directory, resized to (64, 64) and set to binary classification (cat/dog)
training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size = (64, 64),  # Resizing images to 64x64 pixels
                                                 batch_size = 32,         # Batch size of 32 images per iteration
                                                 class_mode = 'binary')   # Binary classification (cat or dog)

# Preprocessing the Test set (only rescaling)
test_datagen = ImageDataGenerator(rescale = 1./255)  # Normalizing pixel values (same as training)
# Loading images from the test directory
test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size = (64, 64),  # Resizing images to 64x64 pixels
                                            batch_size = 32,         # Batch size of 32 images per iteration
                                            class_mode = 'binary')   # Binary classification (cat or dog)

# Initialising the CNN (Convolutional Neural Network)
cnn = tf.keras.models.Sequential()  # Sequential model, layers are added one by one

# Adding the first convolutional layer with ReLU activation
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=[64, 64, 3]))  
# 32 filters (kernels), each of size 3x3, with ReLU activation function (non-linear)
# input_shape defines the shape of each input image (64x64 pixels with 3 color channels)

# Adding a max-pooling layer to reduce the spatial dimensions (downsampling)
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))  # 2x2 pooling with stride of 2 (halves the size)

# Adding another convolutional layer with ReLU activation
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'))

# Adding another max-pooling layer
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

# Flattening the feature map to convert it into a vector (to feed into the fully connected layers)
cnn.add(tf.keras.layers.Flatten())

# Adding a fully connected dense layer with 128 units and ReLU activation
cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))  # 128 neurons in the layer

# Output layer with a single neuron, using sigmoid activation for binary classification (0 or 1)
cnn.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

# Compiling the CNN with the Adam optimizer, binary cross-entropy loss, and accuracy as the evaluation metric
cnn.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Training the CNN on the Training set and evaluating on the Test set for 25 epochs
cnn.fit(x = training_set, validation_data = test_set, epochs = 25)

# Making a single prediction
# Loading an image to classify (resize it to 64x64 pixels)
test_image = image.load_img('dataset/single_prediction/cat_or_dog_1.jpg', target_size = (64, 64))

# Converting the image to an array
test_image = image.img_to_array(test_image)

# Expanding the dimensions of the image (to match the model's input)
test_image = np.expand_dims(test_image, axis = 0)

# Predicting the class of the image
result = cnn.predict(test_image)

# Checking the class label of the prediction (training_set.class_indices tells us which number is 'cat' or 'dog')
training_set.class_indices

# If the result is 1, it's a dog, otherwise it's a cat
if result[0][0] == 1:
  prediction = 'dog'  # The predicted class is 'dog'
else:
  prediction = 'cat'  # The predicted class is 'cat'

# Printing the prediction
print(prediction)
