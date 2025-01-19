import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('Position_Salaries.csv')
print(df)

X = df.iloc[:,1:-1].values
y = df.iloc[:,-1].values
print(X,y)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=10,random_state=1)
regressor.fit(X,y)

regressor.predict([[6.5]])

X_grid = np.arange(min(X), max(X), 0.1).reshape(-1,1)
plt.scatter(X, y, color="red")
plt.plot(X_grid, regressor.predict(X_grid),color="blue")
plt.xlabel = "levels"
plt.ylabel = "Salaries"

plt.scatter(X,y,color="red")
plt.plot(X,regressor.predict(X),color="blue")
plt.xlabel = "levels"
plt.ylabel = "Salaries"
