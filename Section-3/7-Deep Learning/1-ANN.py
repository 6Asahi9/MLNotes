import numpy as np
import pandas as pd
import tensorflow as tf

dataset = pd.read_csv('/content/Churn_Modelling.csv')
X = dataset.iloc[:, 3:-1].values
y = dataset.iloc[:,-1].values

print(f"{X} \n {y}")
#[[619 'France' 'Female' ... 1 1 101348.88]...
#[792 'France' 'Female' ... 1 0 38190.78]] 
#[1 0 1 ... 1 1 0]

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:,2] = le.fit_transform(X[:,2])
print(X)
#[[619 'France' 0 ... 1 1 101348.88]

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [1])], remainder="passthrough")
X = np.array(ct.fit_transform(X))
print(X)
#[[1.0 0.0 0.0 ... 1 1 101348.88]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=1)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#-------------------------------------------------------------------------------------------------------

#initializing the ANN
ann = tf.keras.models.Sequential()
#keras → Keras is a high-level API inside TensorFlow that makes building neural networks easier
#Sequential → This is a specific type of model where layers are stacked one after another, meaning the output of one layer goes directly into the next.

# Adding the input layer and the first hidden layer  
# Dense layer with 6 neurons, using ReLU activation function  
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))  

# Adding the second hidden layer  
# Another Dense layer with 6 neurons, also using ReLU activation  
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))  

# Adding the output layer  
# Since this is a binary classification problem, we use 1 neuron with a sigmoid activation  
ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))  

# Compiling the ANN  
# Optimizer: Adam (adaptive learning rate optimization)  
# Loss function: Binary Crossentropy (used for binary classification)  
# Metric: Accuracy (to evaluate performance)  
ann.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  

# Training the ANN on the training set  
# batch_size: 32 (processes 32 samples at a time)  
# epochs: 100 (number of times the model will see the entire dataset)  
ann.fit(X_train, y_train, batch_size=32, epochs=100)  
#Epoch 1/100
#250/250 ━━━━━━━━━━━━━━━━━━━━ 4s 5ms/step - accuracy: 0.5008 - loss: 0.7194

# Making predictions on the test set  
y_pred = ann.predict(X_test)  

# Converting probabilities to binary values (True if > 0.5, otherwise False)  
y_pred = (y_pred > 0.5)  

# Printing predicted vs actual values side by side  
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1))))

#predicting
#Geography: France ,credit score: 600, Gender: Male, Age:40, Tenure: 3 years,
#Balace: 60,000, No. of Products: 2, have Credit card? : Yes,
#active member: Yes, estimated salary: 50,000, predict will he leave the bank?
print(ann.predict(sc.transform([[1,0,0,600,1,40,3,60000,2,1,1,50000]])) >0.5)
#False

#Making confusion matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)
