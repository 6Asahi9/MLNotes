# 1. Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# 2. Load and prepare the data
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 

# Filter rows with missing values
filtered_melbourne_data = melbourne_data.dropna(axis=0)

# Choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                      'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

# 3. Split data into training and validation sets
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

# 4. Define the function to calculate MAE for Decision Tree
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return mae

# 5. Compare MAE with different values for max_leaf_nodes (Decision Tree)
candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]

# Use a dictionary comprehension to get the MAE for each candidate size
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}

# Find the best tree size (min MAE)
best_tree_size = min(scores, key=scores.get)

# 6. Fit the final Decision Tree model with the best tree size
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=1)
final_model.fit(X, y)  # Train the model with the entire dataset

# 7. Add Random Forest Model
# Define the Random Forest model
rf_model = RandomForestRegressor(random_state=1)

# Fit the model with training data
rf_model.fit(train_X, train_y)

# Predict on validation data
rf_val_prediction = rf_model.predict(val_X)

# Calculate the MAE for Random Forest
rf_val_mae = mean_absolute_error(val_y, rf_val_prediction)

# Print the MAE for Random Forest
print("Validation MAE for Random Forest Model: {}".format(rf_val_mae))

