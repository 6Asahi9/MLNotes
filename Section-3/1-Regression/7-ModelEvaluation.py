import numpy as np

def r2_score(y, y_pred):
    # Calculate the mean of actual values
    y_mean = np.mean(y)
    
    # Calculate RSS (Residual Sum of Squares)
    rss = np.sum((y - y_pred) ** 2)
    
    # Calculate TSS (Total Sum of Squares)
    tss = np.sum((y - y_mean) ** 2)
    
    # Calculate R² score
    r2 = 1 - (rss / tss)
    
    return r2

# Given data
y = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])

# Calculate R² score
r2_score(y, y_pred)

#this will give a score of 0.9486081370449679
