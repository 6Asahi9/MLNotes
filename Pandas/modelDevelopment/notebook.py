# ==============================
# Required Libraries
# ==============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
%matplotlib inline

# ==============================
# Downloading the Dataset
# ==============================
from pyodide.http import pyfetch

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod2.csv"

# Download dataset
await download(path, "laptops.csv")
file_name = "laptops.csv"

# Load dataset into a pandas dataframe
df = pd.read_csv(file_name, header=0)

# ==============================
# Task 1: Single Linear Regression
# ==============================
lm = LinearRegression()
X = df[['CPU_frequency']]
Y = df['Price']

lm.fit(X, Y)
Yhat = lm.predict(X)

# Distribution plot: Actual vs Predicted
ax1 = sns.distplot(df['Price'], hist=False, color="r", label="Actual Value")
sns.distplot(Yhat, hist=False, color="b", label="Fitted Values", ax=ax1)

plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price')
plt.ylabel('Proportion of laptops')
plt.legend()
plt.show()

# Evaluate MSE and R^2
mse_slr = mean_squared_error(df['Price'], Yhat)
r2_slr = lm.score(X, Y)
print('Single Linear Regression R²:', r2_slr)
print('Single Linear Regression MSE:', mse_slr)

# ==============================
# Task 2: Multiple Linear Regression
# ==============================
# Features strongly related to Price
features = ['CPU_frequency','RAM_GB','Storage_GB_SSD','CPU_core','OS','GPU','Category']
Z = df[features]

lm1 = LinearRegression()
lm1.fit(Z, Y)
Y_hat = lm1.predict(Z)

# Distribution plot: Actual vs Predicted
ax2 = sns.distplot(df['Price'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values", ax=ax2)

plt.title('Actual vs Fitted Values for Price (Multiple Linear Regression)')
plt.xlabel('Price')
plt.ylabel('Proportion of laptops')
plt.show()

# Evaluate MSE and R^2
mse_mlr = mean_squared_error(df['Price'], Y_hat)
r2_mlr = lm1.score(Z, Y)
print('Multiple Linear Regression R²:', r2_mlr)
print('Multiple Linear Regression MSE:', mse_mlr)

# ==============================
# Task 3: Polynomial Regression
# ==============================
X_array = X.to_numpy().flatten()

# 1st-degree polynomial (linear)
f1 = np.polyfit(X_array, Y, 1)
p1 = np.poly1d(f1)

# 3rd-degree polynomial
f3 = np.polyfit(X_array, Y, 3)
p3 = np.poly1d(f3)

# 5th-degree polynomial
f5 = np.polyfit(X_array, Y, 5)
p5 = np.poly1d(f5)

# PlotPolly is assumed to be defined elsewhere
# Plot for 3rd-degree polynomial
PlotPolly(p3, X, Y, 'CPU_frequency')

# Plot for 5th-degree polynomial
PlotPolly(p5, X, Y, 'CPU_frequency')

# Evaluate R² and MSE
print('1st-degree polynomial R²:', r2_score(Y, p1(X_array)))
print('1st-degree polynomial MSE:', mean_squared_error(Y, p1(X_array)))

print('3rd-degree polynomial R²:', r2_score(Y, p3(X_array)))
print('3rd-degree polynomial MSE:', mean_squared_error(Y, p3(X_array)))

print('5th-degree polynomial R²:', r2_score(Y, p5(X_array)))
print('5th-degree polynomial MSE:', mean_squared_error(Y, p5(X_array)))

# ==============================
# Task 4: Polynomial Pipeline with Multiple Features
# ==============================
pipeline_steps = [
    ('scale', StandardScaler()), 
    ('polynomial', PolynomialFeatures(include_bias=False)), 
    ('model', LinearRegression())
]

pipe = Pipeline(pipeline_steps)
Z = Z.astype(float)  # Ensure numeric
pipe.fit(Z, Y)
ypipe = pipe.predict(Z)

# Evaluate MSE and R²
print('Pipeline Multi-variable Polynomial Regression MSE:', mean_squared_error(Y, ypipe))
print('Pipeline Multi-variable Polynomial Regression R²:', r2_score(Y, ypipe))
