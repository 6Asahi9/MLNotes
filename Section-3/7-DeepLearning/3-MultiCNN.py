# Importing necessary libraries
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define the number of classes (change according to your dataset)
num_classes = 5  # Example: If you have 5 object categories

# Preprocessing the Training set
train_datagen = ImageDataGenerator(rescale=1./255,    
                                   shear_range=0.2,    
                                   zoom_range=0.2,    
                                   horizontal_flip=True)

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size=(64, 64),
                                                 batch_size=32,
                                                 class_mode='categorical')  # Change to categorical

# Preprocessing the Test set
test_datagen = ImageDataGenerator(rescale=1./255)

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='categorical')  # Change to categorical

# Initialising the CNN
cnn = tf.keras.models.Sequential()

# First convolutional layer
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=[64, 64, 3]))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

# Second convolutional layer
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

# Flattening
cnn.add(tf.keras.layers.Flatten())

# Fully connected layer
cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))

# Output layer (change units to match the number of classes)
cnn.add(tf.keras.layers.Dense(units=num_classes, activation='softmax'))  # Softmax for multi-class classification

# Compiling the CNN
cnn.compile(optimizer='adam',
            loss='categorical_crossentropy',  # Change to categorical_crossentropy
            metrics=['accuracy'])

# Training the CNN
cnn.fit(x=training_set,
        validation_data=test_set,
        epochs=25)

# Making a prediction on a new image
test_image = image.load_img('dataset/single_prediction/test_image.jpg', target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)

# Predicting the class
result = cnn.predict(test_image)

# Getting class labels
class_labels = list(training_set.class_indices.keys())

# Finding the highest probability class
predicted_class = class_labels[np.argmax(result)]
print(predicted_class)
