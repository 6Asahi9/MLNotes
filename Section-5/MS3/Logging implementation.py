import pandas as pd

# Load the dataset
df = pd.read_csv('your-dataset.csv')

# Explore the dataset
print(df.info())
print(df.head())
def validate_data(data):
    try:
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        if data.isnull().values.any():
            raise ValueError("Missing values detected in the dataset.")
        print("Data validation successful.")
    except ValueError as e:
        print(f"Data validation error: {e}")

# Validate the dataset
validate_data(df)
from sklearn.tree import DecisionTreeClassifier

# Implement a decision tree model with error handling
def train_model(X_train, y_train):
    try:
        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)
        print("Model trained successfully.")
    except ValueError as e:
        print(f"Model training error: {e}")

# Example training call (assuming X_train and y_train are preprocessed correctly)
train_model(X_train, y_train)
import logging

# Set up logging to a file
logging.basicConfig(filename='ml_errors.log', level=logging.ERROR)

def validate_data_with_logging(data):
    try:
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        if data.isnull().values.any():
            raise ValueError("Missing values detected in the dataset.")
        print("Data validation successful.")
    except ValueError as e:
        logging.error(f"Data validation error: {e}")

# Validate the dataset and log errors
validate_data_with_logging(df)# Introduce missing values to test error handling
df_with_missing = df.copy()
df_with_missing.iloc[0, 0] = None

# Validate the modified dataset
validate_data_with_logging(df_with_missing)
