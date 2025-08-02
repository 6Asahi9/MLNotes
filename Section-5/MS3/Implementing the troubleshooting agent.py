# Install necessary packages
!pip install pandas scikit-learn logging

import pandas as pd
import numpy as np

# Set random seed so results are the same each time you run (important for reproducibility)
np.random.seed(42)

# -------------------- Generate Synthetic Data -------------------- #
n_samples = 1000
data = {
    'timestamp': pd.date_range(start='2024-01-01', periods=n_samples, freq='h'),  # hourly timestamps
    'cpu_usage': np.random.normal(50, 10, n_samples),        # avg 50% CPU usage
    'memory_usage': np.random.normal(60, 15, n_samples),     # avg 60% memory usage
    'network_latency': np.random.normal(100, 20, n_samples), # avg 100ms network latency
    'disk_io': np.random.normal(75, 10, n_samples),          # avg 75 MB/s disk I/O
    'error_rate': np.random.choice([0, 1], n_samples, p=[0.95, 0.05])  # 5% errors randomly
}

# Create DataFrame
df = pd.DataFrame(data)

# Quick look at data structure and first few rows
print(df.head())
print(df.info())

# -------------------- Anomaly Detection -------------------- #
from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    """
    Uses Isolation Forest to detect anomalies.
    contamination=0.05 → assumes 5% of data is anomalous.
    Returns: 1 for normal, -1 for anomaly.
    """
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(data)
    anomalies = model.predict(data)
    return anomalies

# Detect anomalies in numeric columns only
numeric_data = df.select_dtypes(include=[float, int])
df['anomaly'] = detect_anomalies(numeric_data)

print(df['anomaly'].value_counts())  # Check how many anomalies found

# -------------------- Identify Anomalous Columns -------------------- #
from scipy.stats import zscore

# Calculate z-scores for each numeric value
z_scores = numeric_data.apply(zscore)

def find_anomalous_columns(row, threshold=3):
    """
    For each anomalous row, find which columns have extreme z-scores (>3).
    Returns a list of column names.
    """
    return [col for col in numeric_data.columns if abs(z_scores.loc[row.name, col]) > threshold]

# Apply only to anomalous rows
df['anomalous_columns'] = df.apply(
    lambda row: find_anomalous_columns(row) if row['anomaly'] == -1 else [], axis=1
)

# Show anomalies and which columns triggered them
print(df[df['anomaly'] == -1][['timestamp', 'anomaly', 'anomalous_columns']])

# -------------------- Root Cause Analysis -------------------- #
from sklearn.tree import DecisionTreeClassifier

def root_cause_analysis(X_train, y_train, X_test):
    """
    Trains a decision tree to predict anomaly causes.
    NOTE: Here 'cause' is simplified (we just predict anomaly label again).
    """
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return predictions

# Prepare training data
X_train = df.drop('anomaly', axis=1)
y_train = df['anomaly']
predicted_causes = root_cause_analysis(X_train, y_train, X_train)

# -------------------- Solution Recommendation -------------------- #
def recommend_solution(root_cause):
    """
    Maps detected causes to recommended solutions.
    This is a mockup dictionary (you'd expand this in a real system).
    """
    solutions = {
        "network_error": "Restart the network service.",
        "database_issue": "Check the database connection and restart the service.",
        "high_cpu_usage": "Optimize running processes or allocate more resources."
    }
    return solutions.get(root_cause, "No recommendation available.")

solution = recommend_solution("network_error")
print(f"Recommended solution: {solution}")

# -------------------- Simulate a Network Error -------------------- #
# Manually inject an anomaly (spike in network latency)
df.loc[0, 'network_latency'] = 1000

# Run detection + root cause + solution steps
anomalies = detect_anomalies(df)
predicted_causes = root_cause_analysis(X_train, y_train, df)
solution = recommend_solution(predicted_causes[0])

print(f"Detected issue: {predicted_causes[0]}")
print(f"Recommended solution: {solution}")
