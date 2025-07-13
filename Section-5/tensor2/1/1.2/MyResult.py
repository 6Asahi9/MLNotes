def scale_mnist_data(train_images, test_images):
    train_images = train_images.astype("float32") / 255.0
    test_images = test_images.astype("float32") / 255.0
    return train_images, test_images

scaled_train_images, scaled_test_images = scale_mnist_data(train_images, test_images)
scaled_train_images = scaled_train_images[..., np.newaxis]
scaled_test_images = scaled_test_images[..., np.newaxis]


def get_model(input_shape):
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(8, kernel_size=(3, 3), padding='same', activation='relu', input_shape=input_shape),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    return model

model = get_model(scaled_train_images[0].shape)

def compile_model(model):
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

compile_model(model)

def train_model(model, scaled_train_images, train_labels):
    history = model.fit(scaled_train_images, train_labels, epochs=5)
    return history

history = train_model(model, scaled_train_images, train_labels)


def evaluate_model(model, scaled_test_images, test_labels):
    test_loss, test_accuracy = model.evaluate(scaled_test_images, test_labels)
    return test_loss, test_accuracy

test_loss, test_accuracy = evaluate_model(model, scaled_test_images, test_labels)
print(f"Test loss: {test_loss}")
print(f"Test accuracy: {test_accuracy}")
