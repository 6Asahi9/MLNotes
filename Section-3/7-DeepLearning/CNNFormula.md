### 📌 CNN Workflow (Step-by-Step)

When you pass an image into a Convolutional Neural Network (CNN), it goes through these stages:

* 1️⃣ Input Layer – The image is fed into the model.
* 2️⃣ Convolutional Layers – Extracts important features (edges, textures, etc.).
* 3️⃣ ReLU Activation – Introduces non-linearity to help detect complex patterns.
* 4️⃣ Pooling Layer – Reduces the size of feature maps, making the model efficient.
* 5️⃣ Flattening – Converts the pooled feature maps into a 1D vector.
* 6️⃣ Fully Connected Layer – Connects all neurons to make a final decision.
* 7️⃣ Logits (Final Outputs) – The model outputs raw scores (these are not probabilities yet!).
* 8️⃣ Softmax Layer – Converts logits into probabilities.
* 9️⃣ Prediction – The class with the highest probability is chosen. 🎯

### softmax

![](/images/image_2025-02-18_212722890.png)

### cross Entropy loss

![](/images/image_2025-02-18_212951826.png)
