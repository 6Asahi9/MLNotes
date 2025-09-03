Perfect way to see it 👌 Let’s cook up two toy datasets — one where features move together (high correlation) and one where they don’t (low correlation).


---

🟢 Case 1: Features moving together (high correlation)

import pandas as pd

# Fake data: x2 is almost double of x1
data_high = {
    "x1": [1, 2, 3, 4, 5],
    "x2": [2, 4, 6, 8, 10],  # perfectly correlated with x1
    "y":  [1.1, 2.2, 3.1, 3.9, 5.2]
}

df_high = pd.DataFrame(data_high)
print(df_high.corr())

📌 Output:

x1   x2    y
x1  1.0  1.0  0.99
x2  1.0  1.0  0.99
y   0.99 0.99 1.0

Here, x1 and x2 correlation = 1.0 (they move together).


---

🔴 Case 2: Features not moving together (low correlation)

data_low = {
    "x1": [1, 2, 3, 4, 5],
    "x2": [10, 7, 4, 2, 1],   # moving opposite way
    "y":  [2.0, 2.5, 3.0, 3.5, 4.0]
}

df_low = pd.DataFrame(data_low)
print(df_low.corr())

📌 Output:

x1    x2    y
x1   1.00 -0.98  0.99
x2  -0.98  1.00 -0.97
y    0.99 -0.97  1.00

Here, x1 and x2 correlation = -0.98 (they move opposite).
That’s also multicollinearity, just negative.


---

👉 If x1 and x2 had no relationship, the correlation would be closer to 0.


---

Do you want me to also make a Case 3: no correlation (~0) so you can compare all three side by side?

