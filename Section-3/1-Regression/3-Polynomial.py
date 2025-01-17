import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Position_Salaries.csv')
print(df)

X = df.iloc[:, 1:-1].values
y = df.iloc[:, -1].values

#false regressor
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

#traiing the polynomial model
from sklearn.preprocessing import PolynomialFeatures
#look at the formula if you don't get this
poly_reg = PolynomialFeatures(degree = 4) #here we gonna choose the n (degree)
X_poly = poly_reg.fit_transform(X)

#true regressor 
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly, y)

#false graph
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.xlabel('Position Level')
plt.ylabel('Salary')

#true graph
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)), color='blue')
plt.xlabel('Position Level')
plt.ylabel('Salary')

#but above curve looks a bit bonky so to make it smooth with this 
plt.scatter(X, y, color="blue")
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid),1))
plt.plot(X_grid, lin_reg2.predict(poly_reg.fit_transform(X_grid)), color='green')
plt.xlabel('Position Level')
plt.ylabel('Salary')

#or 
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1,1)

#now predicting new result with lin_reg
lin_reg.predict([[6.5]]) #this is giving the wrong answer
# array([330378.78787879])

lin_reg2.predict(poly_reg.fit_transform([[6.5]])) #this will give the right answer
# array([158862.45265155])
