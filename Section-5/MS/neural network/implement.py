### IMPLEMENTING A SIMPLE NEURAL NETWORK ON AZURE ###

# Step 1: Install the Azure Machine Learning SDK
# This provides tools to create and manage Azure ML workspaces, datasets, compute targets, etc.
pip install azureml-core

# Step 2: Import core class to work with Azure ML resources
from azureml.core import Workspace

# Step 3: Create a new Azure ML workspace
# Alternatively, use Workspace.get() to attach to an existing workspace
ws = Workspace.create(
    name='myworkspace',
    subscription_id='your-subscription-id',
    resource_group='myresourcegroup',
    location='eastus'
)

# Step 4: Save workspace configuration locally to .azureml/config.json
# This allows other scripts or notebooks to auto-load the workspace
ws.write_config(path='.azureml')


# -------------------- PYTORCH MODEL SETUP -------------------- #

import torch
import torch.nn as nn
import torch.optim as optim

# Step 5: Define the architecture of a simple feedforward neural network
# This one has one hidden layer and ReLU activation for MNIST classification
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(784, 128)   # First fully connected layer (input -> hidden)
        self.fc2 = nn.Linear(128, 10)    # Second fully connected layer (hidden -> output)
        self.relu = nn.ReLU()            # Non-linear activation function

    def forward(self, x):
        x = self.relu(self.fc1(x))       # Apply activation after hidden layer
        x = self.fc2(x)                  # Output layer (logits for 10 classes)
        return x

# Step 6: Instantiate the model
model = SimpleNN()

# Step 7: Define the loss function and optimizer
# CrossEntropyLoss is suitable for multi-class classification
# SGD is a basic optimizer with a fixed learning rate
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)


# -------------------- DATASET AND TRAINING -------------------- #

from torchvision import datasets, transforms

# Step 8: Load the MNIST dataset using torchvision
# Applies ToTensor() transform to convert images into normalized tensors
train_loader = torch.utils.data.DataLoader(
    datasets.MNIST(root='data', train=True, download=True,
                   transform=transforms.ToTensor()),
    batch_size=32, shuffle=True
)

# Step 9: Train the neural network over 5 epochs
# For each batch: perform forward pass, calculate loss, backpropagate, update weights
num_epochs = 5
for epoch in range(num_epochs):
    running_loss = 0.0
    for inputs, labels in train_loader:
        optimizer.zero_grad()                     # Clear previous gradients

        outputs = model(inputs.view(-1, 784))     # Flatten 28x28 images to 784
        loss = criterion(outputs, labels)         # Compute classification loss

        loss.backward()                           # Backpropagate gradients
        optimizer.step()                          # Update model parameters

        running_loss += loss.item()               # Accumulate loss per batch

    print(f"Epoch {epoch+1}, Loss: {running_loss/len(train_loader)}")


# -------------------- SAVE AND REGISTER MODEL IN AZURE -------------------- #

from azureml.core import Model

# Step 10: Save the model's trained weights to a file
torch.save(model.state_dict(), 'simple_nn.pth')

# Step 11: Register the saved model inside the Azure ML workspace
# This allows deployment, versioning, and tracking
model = Model.register(
    workspace=ws,
    model_path='simple_nn.pth',
    model_name='simple_nn'
)

# Note: To deploy this model as a REST API, you'd need to:
# - Write a scoring script (score.py) to handle input/output
# - Define an inference environment using Environment.from_conda_specification or Docker
# - Use InferenceConfig and Model.deploy() methods
# These steps are not shown here.
