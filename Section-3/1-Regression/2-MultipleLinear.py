import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv('50_Startups.csv')
print(df)

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

#encoding the categorical data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
#countries column is on the 3rd index
ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [3] )], remainder= 'passthrough')
X = np.array(ct.fit_transform(X))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#this class will stop dummy varaible trap itslef
#for manual elimination, watch the video
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#prediction
y_pred = regressor.predict(X_test)

np.set_printoptions(precision = 2)
print(np.concatenate( (y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1 )) , 1))

#Steps for Manual Backward Elimination

#1.Fit the Full Model: Start with all the independent variables/features.
#2. Check p-values: Determine the significance of each feature by checking its p-value.
# A common significance level ( 𝛼 α) is 0.05.
#3. Remove the Least Significant Feature: If the highest p-value is greater than 𝛼 α, remove the corresponding feature.
#4. Refit the Model: Fit the model again without the removed feature.
#5. Repeat: Continue until all remaining features have p-values below 𝛼 α.

#for manual backward Elimination
import statsmodels.api as sm
X = np.append(arr = np.ones((50, 1)).astype(int), values = X, axis = 1)
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_opt = X_opt.astype(np.float64)
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()
X_opt = X[:, [0, 1, 3, 4, 5]]
X_opt = X_opt.astype(np.float64)
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()
X_opt = X[:, [0, 3, 4, 5]]
X_opt = X_opt.astype(np.float64)
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()
X_opt = X[:, [0, 3, 5]]
X_opt = X_opt.astype(np.float64)
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()
X_opt = X[:, [0, 3]]
X_opt = X_opt.astype(np.float64)
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

