The formula you’re looking at,

$$
\chi^2 = \sum_{i=1}^{N} \frac{(y_i - y_\text{model}(x_i))^2}{\sigma_i^2},
$$

is called the **chi-squared (χ²) statistic** or **chi-squared goodness-of-fit formula**.

* It’s part of **chi-squared analysis**, which is widely used in:

  * Statistics to test how well a model fits data
  * Physics/engineering to weigh uncertainties
  * Machine learning when evaluating weighted errors

If you include the division by degrees of freedom ($N - p$), it’s often called **reduced chi-squared**:

$$
\chi^2_\text{reduced} = \frac{\chi^2}{N - p}
$$

* This is what people check to see if a fit is “good” in practice.

---

If you want, I can **draw a cute Miya visual explaining χ² vs χ²\_reduced**, so it really sticks in your brain 🐾✨.

Do you want me to do that?
