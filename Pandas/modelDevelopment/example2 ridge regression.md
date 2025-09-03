Exactly 👌 — checking correlations is the quickest way.

🔎 How to spot multicollinearity

1. Correlation matrix (.corr())



import pandas as pd

corr = df.corr()
print(corr)

Look for pairs of features with correlation close to +1 or -1.

Example: diameter vs circumference → correlation ≈ 0.99.
That’s a red flag 🚩.



---

2. Heatmap (visual check)



import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

This lets you instantly spot blocks of highly correlated features.


---

3. Variance Inflation Factor (VIF)
This is a more formal test:



from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

X = add_constant(df)  # add intercept
vif = pd.DataFrame()
vif["feature"] = X.columns
vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(vif)

VIF > 5 or 10 = strong multicollinearity.



---

👉 .corr() is enough for a quick check, but VIF is the professional way to confirm.

Do you want me to show you a small dataset with fake numbers where you’ll see .corr() flagging two features almost identical?

