import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('1-DataProcessing.csv')
# method of using features = ['a','b'] then X = dataset[features] also works
X = dataset.iloc[:, :-1].values # include everything expect the last element
# or can use df.drop(columns=['target']) or df.drop(['C'], axis=1)
y = dataset.iloc[:, -1].values # -1 means the last element

#------------------------------------------------------------------------

# filtered = dataset.dropna(axis = 0) also works but not a good behavior
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values= np.nan, strategy= 'mean')
# SimpleImputer automatically assumes that missing values are
# represented by np.nan so The missing_values parameter is optional
imputer.fit(X[:, 1:3])# cover all the values but leaves column 0 and
# stops before 3 so only column 1 and 2 are included
X[:, 1:3] = imputer.transform(X[:, 1:3])
# can use this too X[:, 1:3] = imputer.fit_transform(X[:, 1:3])
# If you want to update the original data (X) directly
# If you want to keep the original data (X) intact and store the imputed result
# separately, use this transformed_X = imputer.transform(X[:, 1:3])

#------------------------------------------------------------------------

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
# Create a ColumnTransformer
ct = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), [0])], # Apply OneHotEncoder to column 0 (the 'Country' column)
    remainder='passthrough'  # Keep all other columns unchanged
)

# Fit and transform the data (apply transformations)
X = np.array(ct.fit_transform(X))

#------------------------------------------------------------------------

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
# converting yes/no values into 1 and 0

from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y, test_size = 0.2, random_state = 1)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
train_X[:, 3:] = sc.fit_transform(train_X[:, 3:])
val_X[:, 3:] = sc.transform(val_X[:, 3:]) #don't use fit_transform here

print(train_X)
[[0.0 0.0 1.0 -0.19159184384578545 -1.0781259408412425]
[0.0 1.0 0.0 -0.014117293757057777 -0.07013167641635372]
[1.0 0.0 0.0 0.566708506533324 0.633562432710455]
[0.0 0.0 1.0 -0.30453019390224867 -0.30786617274297867]
[0.0 0.0 1.0 -1.9018011447007988 -1.420463615551582]
[1.0 0.0 0.0 1.1475343068237058 1.232653363453549]
[0.0 1.0 0.0 1.4379472069688968 1.5749910381638885]
[1.0 0.0 0.0 -0.7401495441200351 -0.5646194287757332]]

print(val_X)
[[0.0 1.0 0.0 -1.4661817944830124 -0.9069571034860727]
[1.0 0.0 0.0 -0.44973664397484414 0.2056403393225306]]
