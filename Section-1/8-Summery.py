#1. Loading the Dataset
#We use pandas to load the dataset into a DataFrame for analysis:

import pandas as pd
df = pd.read_csv('dataset.csv', delimiter=';')

#delimiter=';': Specifies the column separator used in the dataset (e.g., semicolon).
#Use it only if the dataset's columns are separated by ;. Otherwise, it may result in errors or misinterpretation of data.

#----------------------------------------------------------------------------------------------#

#2. Separating Features and Target
#Split the dataset into features (X) and target (y):

X = df.iloc[:, :-1].values  # All rows, all columns except the last (features)
y = df.iloc[:, -1].values   # All rows, only the last column (target)

#X: Contains input features (independent variables).
#y: Contains the target column (dependent variable).

#----------------------------------------------------------------------------------------------#

#3. Handling Categorical Data
#Categorical columns are converted into numeric form using either:
#Label Encoding: Converts categories into integers (e.g., Yes/No to 1/0).

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

#Best for binary data or ordinal categories.

#One-Hot Encoding: Converts categories into dummy variables (e.g., country names into separate columns).

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), [column_index])],
    remainder='passthrough')
X = ct.fit_transform(X)

#Best for non-ordinal categorical data.

#----------------------------------------------------------------------------------------------#

#4. Splitting the Dataset
#Split the dataset into training and test/validation sets:

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Training set: Used to train the model.
#Test/Validation set: Used to evaluate the model’s performance.
#random_state: Ensures reproducibility of the split.

#----------------------------------------------------------------------------------------------#

#5. Feature Scaling
#Feature scaling standardizes the range of features to ensure all variables contribute equally to the model:

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train = sc.fit_transform(X_train)  # Fit and scale training data
X_test = sc.transform(X_test)        # Scale test data using training parameters

#fit_transform:
    #Fits: Calculates the mean and standard deviation from the training data.
    #Transforms: Applies the scaling formula:

#transform:
    #Uses the mean and std dev calculated from X_train to scale the test data.
    #Avoids recalculating to prevent data leakage.

#----------------------------------------------------------------------------------------------#

#Why Avoid fit_transform on Test Data?
#If you use fit_transform on test data, it recalculates the mean and standard deviation based on the test data, leading to data leakage and inconsistent scaling. This results in:
#Biased evaluation of the model.
#Unrealistic performance metrics.

#----------------------------------------------------------------------------------------------#

#Example with Miya's Toys 🌈:

Training sizes: [10, 20, 30]
Mean: 20
Std Dev: 8.16
Scaled: [-1.22, 0.00, 1.22]
Test sizes: [25, 35]
Scaled using training mean/std: [0.61, 1.84]
