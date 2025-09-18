That one’s a nice little trick 👀

`null_df['device'].value_counts(normalize=True)`

* **`null_df['device']`** → grabs the `"device"` column from your dataframe.
* **`.value_counts()`** → counts how many times each unique device appears.
* **`normalize=True`** → instead of raw counts, it gives you **proportions (percentages)**.

---

💻 Example:

```python
import pandas as pd

data = {
    "device": ["iOS", "Android", "iOS", "iOS", "Android", "Web"]
}
null_df = pd.DataFrame(data)

print(null_df['device'].value_counts(normalize=True))
```

Output:

```
iOS       0.50
Android   0.33
Web       0.17
Name: device, dtype: float64
```

* iOS makes up **50%** of devices
* Android makes up **33%**
* Web makes up **17%**

---

👉 In short: it shows the **distribution** of categories in percentages instead of raw numbers.

Would you like me to also show you how to plot that distribution as a chart (pie or bar) so it’s easier to “see” than just reading numbers?


-----------------------------------
That’s another useful one 😼

`df.median(numeric_only=True)`

* **`median`** → finds the middle value of a column (50th percentile).
* **`numeric_only=True`** → tells Pandas to **ignore non-numeric columns** (like strings, dates, categories) and only calculate the median for numeric ones.

---

💻 Example:

```python
import pandas as pd

data = {
    "age": [20, 25, 30, 35, 40],
    "score": [90, 85, 70, 95, 88],
    "name": ["A", "B", "C", "D", "E"]
}

df = pd.DataFrame(data)

print(df.median(numeric_only=True))
```

Output:

```
age      30.0
score    88.0
dtype: float64
```

* Median age = **30**
* Median score = **88**
* `"name"` column is ignored, since it’s not numeric.

---

👉 If you **don’t** put `numeric_only=True` and your dataframe has strings, Pandas might give a warning or fail, because it can’t compute the median of text.

Do you want me to also contrast **mean vs median** (with an example where they give very different results)?
