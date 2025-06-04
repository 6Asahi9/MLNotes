# Step-by-step process:
# Fit the model with all features.
# Identify the feature with the highest p-value.
# Remove the feature with the highest p-value.
# Refit the model and repeat until all remaining features are statistically significant.
# Define a significance level
significance_level = 0.05

# Perform backward elimination
while True:
    # Fit the model
    model = sm.OLS(y, X).fit()
    # Get the highest p-value in the model
    max_p_value = model.pvalues.max()
    
    # Check if the highest p-value is greater than the significance level
    if max_p_value > significance_level:
        # Identify the feature with the highest p-value
        feature_to_remove = model.pvalues.idxmax()
        print(f"Removing feature: {feature_to_remove} with p-value: {max_p_value}")
        
        # Drop the feature
        X = X.drop(columns=[feature_to_remove])
    else:
        break

# Display the final model summary
print(model.summary())
