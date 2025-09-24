
ols_data = data[["Radio", "Sales"]]
ols_data.head(10)
ols_formula = "Sales ~ Radio"
# "Sales ~ Radio" → formula notation:
# Sales = dependent/outcome variable Y
# Radio = predictor/independent variable 𝑋
# ~ = “is modeled by”
# ols() = defines the problem, fit() = actually calculates the slope/intercept that minimize SSR
OLS = ols(formula = ols_formula, data = ols_data)
model = OLS.fit()
model.summary()

sns.regplot(x = "Radio", y = "Sales", data = ols_data)
esiduals = model.resid

fig = sns.histplot(residuals)
fig.set_xlabel("Residual Value")
fig.set_title("Histogram of Residuals")
plt.show()

sm.qqplot(residuals, line='s')
plt.title("Q-Q plot of Residuals")
plt.show()


fitted_values = model.predict(ols_data["Radio"])


fig = sns.scatterplot(x=fitted_values, y=residuals)
fig.axhline(0)
fig.set_xlabel("Fitted Values")
fig.set_ylabel("Residuals")
plt.show()

