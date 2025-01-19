#Ridge Regression

from sklearn.linear_model import Ridge

# Model
ridge = Ridge(alpha=1.0)  # alpha is the regularization strength (lambda)

# Fit and predict
ridge.fit(X_train, y_train)
ridge_predictions = ridge.predict(X_test)


#Lasso Regression

from sklearn.linear_model import Lasso

# Model
lasso = Lasso(alpha=0.1)  # Smaller alpha = less regularization

# Fit and predict
lasso.fit(X_train, y_train)
lasso_predictions = lasso.predict(X_test)


#Elastic Net Regression

from sklearn.linear_model import ElasticNet

# Model
elastic_net = ElasticNet(alpha=0.1, l1_ratio=0.5)  
# l1_ratio: Mix of Lasso (L1) and Ridge (L2). 0.5 = equal mix.

# Fit and predict
elastic_net.fit(X_train, y_train)
elastic_net_predictions = elastic_net.predict(X_test)
