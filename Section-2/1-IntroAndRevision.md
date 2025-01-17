![](../images)
![](../images/image_2025-01-17_215326569.png)

![](../images/image_2025-01-17_215616366.png)

### random forect

![](../images/image_2025-01-17_215729594.png)

### adding the mean 
from sklearn.metrics import mean_absolute_error

# Function for comparing different models
def score_model(model, X_t=X_train, X_v=X_valid, y_t=y_train, y_v=y_valid):
    model.fit(X_t, y_t)
    preds = model.predict(X_v)
    return mean_absolute_error(y_v, preds)

for i in range(0, len(models)):
    mae = score_model(models[i])
    print("Model %d MAE: %d" % (i+1, mae))

### results 
Model 1 MAE: 24015
Model 2 MAE: 23740
Model 3 MAE: 23528
Model 4 MAE: 23996
Model 5 MAE: 23706

* Fit the model to the training data
model_3.fit(X, y)

* Generate test predictions
preds_test = model_3.predict(X_test)
