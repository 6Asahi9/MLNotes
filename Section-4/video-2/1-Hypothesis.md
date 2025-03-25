![](https://www.youtube.com/watch?v=4b4MUYve_U8&list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU&index=2&t=7s)

### During Prediction:
The model no longer needs 
y because it already has optimized values for 
𝜃.

We just apply the learned formula:

h 
θ
​(x) = θ0 + θ1 x1 + θ2 x2... θn xn 

We input new values of 
X and get predictions.

Since 
y was used in training to find 
θ, it doesn’t appear in the formula anymore—it’s already "baked into" the model.

NOTE: x0 and x1... xn are all DIFFERENT FEATURES  (not just different values of the same feature).
