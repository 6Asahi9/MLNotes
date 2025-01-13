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

