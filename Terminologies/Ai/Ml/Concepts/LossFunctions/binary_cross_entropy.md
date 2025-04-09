- [Binary Cross Entropy](https://youtu.be/zTXBB3oGFbU?si=qwDsBe74_FGi6ETw)

It is used in those classification tasks, where we want to classify data in two classes, like "yes" or "no", "cat" or "not cat".

## 🔹 What is Binary Cross Entropy?
**Binary Cross Entropy** is a **loss function** used for binary classification tasks — where the output is either 0 or 1 (like "yes" or "no", "cat" or "not cat").\
Btw it can also be used for multiples classes, but it especially for 2 classes classification problems, for multiple classes we use **Categorical Cross Entropy**


It tells us how wrong the model's prediction is, compared to the true label(means gives the error).

Mathematical Formula:
```math
BCE = \frac{-1}{N} \sum_{i=1}^N (y_i \log(\hat{y}_i) + (1-y_i) \log(1-\hat{y}_i))
``` 
🧠 Explanation of the terms:
- $N$ = total number of samples
- $y_i$ = true label for sample $i$(either 0 or 1)
- $\hat{y}_i$ = predicted probability for sample $i$ (between 0 and 1)
- log = natural logarithm(means the base of the logarithm is e)
- You're averaging over all samples with the $\frac{1}{N}$ factor
- The negative sign makes the loss positive (since logs are negative when < 1)

[But you can ignore the left side (sparated by +) and only focus on the right side (separated by +) when your actual label is 0\
or
you can work on the left side (separated by +) when your actual label is 1, reason:](https://youtu.be/zTXBB3oGFbU?si=UOk7Mi40OIpkizIy&t=247)

This also implies:
- If $y_i = 1$ then it only cares about $log(\hat{y}_i)$
- If $y_i = 0$ then it only cares about $log(1-\hat{y}_i)$

And that's also because:
- For class 1, you want $y_i$  to be close to 1
- For class 0, you want $y_i$ to be close to 0
- So the BCE loss rewards predictions close to the true label and penalizes wrong guesses.

----

Where:
- $N$ is the number of data points
- $y_i$ is the true label for data point $i$
- $\hat{y}_i$ is the predicted probability for data point $i$
- For $\log$ we taking base $e$ (euler's number $e \approx 2.718$) genrally


[Example](https://youtu.be/zTXBB3oGFbU?si=hzfPrArcUCk-sUH8&t=217)