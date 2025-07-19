import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import gc
import h5py

from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
import tensorflow_hub as hub

# 1. Check TensorFlow version
print(tf.__version__)  # Expected: 2.0.0+

# 2. Load CIFAR-10 dataset and preprocess
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# 3. Subset for faster experiments
x_train, y_train = x_train[:1000], y_train[:1000]
x_test, y_test = x_test[:100], y_test[:100]

# 4. Visualize first 10 images
fig, ax = plt.subplots(1, 10, figsize=(10, 1))
for i in range(10):
    ax[i].imshow(x_train[i])
    ax[i].axis("off")

# 5. Helper: Evaluate test accuracy of a model
def get_test_accuracy(model, x_test, y_test):
    test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
    print('accuracy: {acc:0.3f}'.format(acc=test_acc))

# 6. Helper: Create new CNN model
def get_new_model():
    model = Sequential([
        Conv2D(16, (3, 3), activation='relu', input_shape=(32, 32, 3), name='conv_1'),
        Conv2D(8, (3, 3), activation='relu', name='conv_2'),
        MaxPooling2D((4, 4), name='pool_1'),
        Flatten(name='flatten'),
        Dense(32, activation='relu', name='dense_1'),
        Dense(10, activation='softmax', name='dense_2')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

# 7. Instantiate and view model
model = get_new_model()
model.summary()

# 8. Check accuracy before training (should be ~10%)
get_test_accuracy(model, x_test, y_test)

# 9. Save model weights every epoch
checkpoint_path = 'model_checkpoints/cp.ckpt'
checkpoint = ModelCheckpoint(filepath=checkpoint_path,
                             save_weights_only=True,
                             save_best_only=False,
                             verbose=1)

model.fit(x_train, y_train, epochs=5,
          validation_data=(x_test, y_test),
          callbacks=[checkpoint])

# 10. Check files created by the checkpoint
os.listdir("model_checkpoints")

# 11. Evaluate trained model
get_test_accuracy(model, x_test, y_test)

# 12. Load weights into a new model
model = get_new_model()
model.load_weights('model_checkpoints/cp.ckpt')
get_test_accuracy(model, x_test, y_test)

# 13. Clean directory (if needed)
os.system('rm -r model_checkpoints')

# 14. Use better checkpoint naming (custom filename per epoch)
checkpoint_path = 'model_checkpoints/ckpt_epoch_{epoch:02d}_val_loss_{val_loss:.6f}.ckpt'
checkpoint = ModelCheckpoint(filepath=checkpoint_path,
                             monitor='val_loss',
                             save_best_only=True,
                             save_weights_only=True,
                             save_freq='epoch',
                             mode='min',
                             verbose=1)

model = get_new_model()
model.fit(x_train, y_train, epochs=5,
          validation_data=(x_train, y_train),
          callbacks=[checkpoint])

# 15. Save based on highest validation accuracy
x_train, y_train = x_train[:100], y_train[:100]
x_test, y_test = x_test[:100], y_test[:100]

model = get_new_model()
checkpoint_path = 'model_checkpoints/acc.ckpt'
checkpoint = ModelCheckpoint(filepath=checkpoint_path,
                             monitor='val_accuracy',
                             save_best_only=True,
                             save_weights_only=True,
                             verbose=1)

history = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=5,
                    callbacks=[checkpoint])

# 16. Plot training vs validation accuracy
df = pd.DataFrame(history.history)
df.plot(y=['accuracy', 'val_accuracy'])

# 17. Load best weights
model = get_new_model()
model.load_weights(checkpoint_path)

# 18. Save entire model (.h5)
os.makedirs('model_checkpoints_best', exist_ok=True)
checkpoint = ModelCheckpoint(filepath='model_checkpoints_best/full_model.h5',
                             monitor='val_accuracy',
                             save_best_only=True,
                             save_weights_only=False,
                             verbose=1)

model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10, callbacks=[checkpoint])

# 19. Load full model from .h5
model = load_model('model_checkpoints_best/full_model.h5')
model.evaluate(x_test, y_test)

# 20. Save manually in .h5 format
model.save('full_model.h5')

# 21. Inspect the .h5 file
with h5py.File('full_model.h5', 'r') as f:
    print(list(f.keys()))  # ['model_weights', 'optimizer_weights']

# 22. Delete and reload
del model
gc.collect()
model = load_model('full_model.h5')

# 23. Load Keras built-in ResNet50 model
model = ResNet50(weights='imagenet')

# 24. Load sample images for ResNet50
lemon_img = load_img('data/lemon.jpg', target_size=(224, 224))
viaduct_img = load_img('data/viaduct.jpg', target_size=(224, 224))
water_tower_img = load_img('data/water_tower.jpg', target_size=(224, 224))

# 25. Helper: Predict top 5 classes
def get_top_5_predictions(img):
    x = img_to_array(img)[np.newaxis, ...]
    x = preprocess_input(x)
    preds = decode_predictions(model.predict(x), top=5)
    top_preds = pd.DataFrame(columns=['prediction', 'probability'],
                             index=np.arange(5)+1)
    for i in range(5):
        top_preds.loc[i+1] = [preds[0][i][1], preds[0][i][2]]
    return top_preds

# 26. TensorFlow Hub: MobileNet v1
module_url = "https://tfhub.dev/google/imagenet/mobilenet_v1_050_160/classification/4"
model = Sequential([hub.KerasLayer(module_url)])
model.build(input_shape=[None, 160, 160, 3])

# 27. Preprocess for MobileNet
lemon_img = load_img("data/lemon.jpg", target_size=(160, 160))
viaduct_img = load_img("data/viaduct.jpg", target_size=(160, 160))
water_tower_img = load_img("data/water_tower.jpg", target_size=(160, 160))

with open('data/imagenet_categories.txt') as f:
    categories = f.read().splitlines()

# 28. Helper: MobileNet predictions
def get_top_5_predictions(img):
    x = img_to_array(img)[np.newaxis, ...] / 255.0
    preds = model.predict(x)
    top_preds = pd.DataFrame(columns=['prediction'], index=np.arange(5)+1)
    sorted_index = np.argsort(-preds[0])
    for i in range(5):
        top_preds.loc[i+1, 'prediction'] = categories[sorted_index[i]]
    return top_preds
