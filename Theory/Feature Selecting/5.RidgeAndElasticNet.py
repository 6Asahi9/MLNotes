# Random seed for reproducibility
np.random.seed(42)

# Generate fake data
X = np.random.rand(100, 5)
true_weights = np.array([5, 0, 0, 2, 0])  # Only features 0 and 3 are actually useful
y = X @ true_weights + np.random.normal(0, 0.5, 100)  # Add noise

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ridge Regression ----------------------------------------------------------
ridge = Ridge(alpha=1.0)  # alpha is λ, the regularization strength
ridge.fit(X_train, y_train)

ridge_preds = ridge.predict(X_test)
ridge_mse = mean_squared_error(y_test, ridge_preds)

print("Ridge Coefficients:", ridge.coef_)
print("Ridge MSE:", ridge_mse)

# Elastic Net Regression ----------------------------------------------------
elastic = ElasticNet(alpha=1.0, l1_ratio=0.5)  # 50% Lasso, 50% Ridge
elastic.fit(X_train, y_train)

elastic_preds = elastic.predict(X_test)
elastic_mse = mean_squared_error(y_test, elastic_preds)

print("ElasticNet Coefficients:", elastic.coef_)
print("ElasticNet MSE:", elastic_mse)

# Visualize Coefficients
labels = [f"X{i}" for i in range(X.shape[1])]
x = np.arange(len(labels))

plt.bar(x - 0.2, ridge.coef_, width=0.4, label='Ridge')
plt.bar(x + 0.2, elastic.coef_, width=0.4, label='ElasticNet')
plt.xticks(x, labels)
plt.ylabel("Coefficient Value")
plt.legend()
plt.title("Comparison of Coefficients")
plt.show()
