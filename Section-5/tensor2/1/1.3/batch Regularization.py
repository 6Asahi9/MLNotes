# Batch normalisation - defining the model
# We can implement batch normalisation into our model by adding it in the same way as any other layer.

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Conv2D, MaxPooling2D, BatchNormalization, Dropout
# Build the model
​
model = Sequential([
    Dense(64, input_shape=[train_data.shape[1],], activation="relu"),
    BatchNormalization(),  # <- Batch normalisation layer
    Dropout(0.5),
    BatchNormalization(),  # <- Batch normalisation layer
    Dropout(0.5),
    Dense(256, activation='relu'),
])
​
# NB: We have not added the output layer because we still have more layers to add!
# Print the model summary
​
model.summary()
# Recall that there are some parameters and hyperparameters associated with batch normalisation.

# The hyperparameter momentum is the weighting given to the previous running mean when re-computing it with an extra minibatch. By default, it is set to 0.99.

# The hyperparameter ϵ
#  is used for numeric stability when performing the normalisation over the minibatch. By default it is set to 0.001.

# The parameters β
#  and γ
#  are used to implement an affine transformation after normalisation. By default, β
#  is an all-zeros vector, and γ
#  is an all-ones vector.

# Customising parameters
# These can all be changed (along with various other properties) by adding optional arguments to tf.keras.layers.BatchNormalization().
# We can also specify the axis for batch normalisation. By default, it is set as -1.
# Add a customised batch normalisation layer
​
model.add(tf.keras.layers.BatchNormalization(
    momentum=0.95, 
    epsilon=0.005,
    axis = -1,
    beta_initializer=tf.keras.initializers.RandomNormal(mean=0.0, stddev=0.05), 
    gamma_initializer=tf.keras.initializers.Constant(value=0.9)
))
# Add the output layer
​
model.add(Dense(1))
Compile and fit the model
# Let's now compile and fit our model with batch normalisation, and track the progress on training and validation sets.

model.compile(optimizer='adam',
              loss='mse',
              metrics=['mae'])
Now we fit the model to the data.

# Train the model
history = model.fit(train_data, train_targets, epochs=100, validation_split=0.15, batch_size=64,verbose=False)
