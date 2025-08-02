``` python
import psutil

# Monitor resource usage
cpu_usage = psutil.cpu_percent()
memory_usage = psutil.virtual_memory().percent

# for better results, measure CPU usage while inference is active,
# and measure memory usage against a baseline before the model is loaded
print(f"CPU Usage: {cpu_usage}%")
print(f"Memory Usage: {memory_usage}%")
```
### stress testing 
```python
import numpy as np
import time

# Ensure correct shape before repeating
print("Original x_test shape:", x_test.shape)  # Expected: (10000, 28, 28)

# Properly duplicate test data along batch axis
large_input = np.repeat(x_test, 10, axis=0)  # Expands batch size only

# Verify new shape
print("Large input shape after fix:", large_input.shape)  # Should be (100000, 28, 28)

# Measure performance under stress
start_time = time.time()
model.predict(large_input)  # Now matches model input (batch_size, 28, 28)
end_time = time.time()

print(f"Response Time under Stress (Reduced Size): {end_time - start_time:.4f} seconds")
```
### bench marks and cross validation
``` python
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

# Example data generation for demonstration (replace with actual data)
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
agent_model = RandomForestClassifier()  # Replace with your actual model

# Perform 5-fold cross-validation
cv_scores = cross_val_score(agent_model, X, y, cv=5)

# Print the cross-validation scores for each fold
print(f'Cross-Validation Scores: {cv_scores}')

# Print the mean and standard deviation of the scores
print(f'Mean CV Score: {cv_scores.mean():.4f}')
print(f'Standard Deviation of CV Scores: {cv_scores.std():.4f}')
```
