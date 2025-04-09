[Mean Absolute Error](https://youtu.be/7oSh63dE_lE?si=o807Dq_tStSHHIYT&t=97)

Math formula:


```math
MAE = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y_i}|

```
[Why we take absolute difference between target and predicted value](https://youtu.be/7oSh63dE_lE?si=HKHS3rlERul-PcQa&t=137)

Example: 

```python
import numpy as np

def mean_absolute_error(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))
```