### 📋 Weight and Bias Indexing
In a neural network, weights and biases are key parameters that influence the network’s predictions. Here's how they’re indexed:

### 🔹 Weights (W)
Weights connect neurons between layers.

Each weight is specific to a connection between two neurons.

Indexed as:

W 
ij
​
Where:

i = Neuron index in the current layer (output neuron)

j = Neuron index in the previous layer (input neuron)

Example: W₃₂ = The weight connecting Neuron 3 in the current layer to Neuron 2 in the previous layer.

### 🔹 Biases (b)
Bias is a separate value added to each neuron before activation.

Each neuron has one unique bias.

Indexed as:

bi

Where:

i = The neuron index in the current layer.

Example: b₄ = The bias for Neuron 4 in the current layer.

Vi = 
∑
j 
​
 (W 
ij
​
 ×X 
j
​
 )+bi
​
Where:

X_j = Input value from neuron j.

W_{ij} = Weight for the connection.

b_i = Bias for neuron i.

![](/images/{2C7F2C1A-A6EE-432E-9B6A-22F2E6B7E417}.png)
