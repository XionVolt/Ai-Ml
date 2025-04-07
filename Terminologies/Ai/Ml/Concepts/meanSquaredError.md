[Mean squared error](https://www.youtube.com/live/40xGMygHMDU?si=3FoO-kLXNyFvX2US&t=4337)

Formula for mean squared error:
```math
MSE = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y_i})^2
```
Where:

- $n$ is the number of data points
- $y_i$ is the true value of the $i_{th}$  data point
- $\hat{y_i}$ is the predicted value of the $i_{th}$ data point

In other words, the **mean squared error** is the ***average of the squared difference between the true and predicted values*** for each data point.

Example:

```python
import numpy as np

# Consider some data set,where:
y_true = np.array([1, 2, 3, 4, 5])
y_pred = np.array([2, 3, 4, 5, 6])

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

mse = mean_squared_error(y_true, y_pred)
print("Mean squared error:", mse)

# Output:
# Mean squared error: 1.0
```