import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('Position_Salaries.csv')
print(df)

X = df.iloc[:,1:-1].values
y = df.iloc[:,-1].values
print(X,y)

from sklearn.tree import DecisionTreeRegressor #not DecisionTreeClassifier
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X,y)

prediction = regressor.predict([[6.5]])
print(prediction)

X_grid = np.arange(min(X), max(X), 0.1).reshape(-1,1)
plt.scatter(X,y, color="red")
plt.plot(X_grid, regressor.predict(X_grid), color="blue")
plt.xlabel = 'Level'
plt.ylabel = 'salary'

plt.scatter(X,y,color="red")
plt.plot(X, regressor.predict(X), color="blue")
plt.xlabel = 'Level'
plt.ylabel = 'salary'
