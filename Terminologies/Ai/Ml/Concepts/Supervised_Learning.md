# Supervised learning : 
Supervised learning refers to type of ml in which algorithms learns X to Y  or we can also say Input to Output mappings.The key characteristics of supervised learning is that you give your learning algorithms , **examples** to learn from , that includes the right answers , whereby right answers means here correct label Y for a given input X and by seeing correct pairs of input X and desired output label Y that learning algorithm eventually learns to take just the input alone without the output label and gives us reasonable accurate prediction or guess of the output for the new given input., 
Example : [Regression Problem](https://youtu.be/sca5rQ9x1cA?si=x5hcOOdTOfFomfpT&t=64)
Example: [Classification Problem](https://youtu.be/hh6gE0LxfO8?si=SNeN3leskHea-ul9)  , these both videos by `Andrew Ng` also tells you why `regression`(a type of supervised learning task) is different from a `classification`(its also another type of supervised learning task) .

**These two are major types of supervised learning , used in different scenarios**


## Regression vs. Classification 

So we know Supervised learning is a type of machine learning where the model learns from labeled data (data with known answers(we can say outputs/output labels y) of corresponding input/inputs). There are two main types of supervised learning tasks: **regression** and **classification**. Let’s break down the difference between them.

---

### Regression
- **Goal**: Predict a **continuous numerical value**.
- **Output**: A number (e.g., price, temperature, age).
- **Example**: Predicting the price of a house based on its size, location, and number of bedrooms.(this *size*, *location*, *number of bedrooms* are inputs or features)
  - Input: Features like square footage, number of rooms, etc.
  - Output: A continuous value, such as $350,000(house price).

## Real-Life Example:
Imagine you want to predict the temperature tomorrow based on weather data like humidity, wind speed, and cloud cover. The output will be a number (e.g., 25.6°C). This is a regression problem because the result is a continuous value.(This is regression because our algorithm has to predict output number(y label) from a infinitely many possible outputs)

---

### Classification
- **Goal**: Predict a **category or class label**.
- **Output**: A discrete label (e.g., yes/no, spam/not spam, dog/cat).
- **Example**: Predicting whether an email is spam or not spam.
  - Input: Features like the email’s text, sender, and subject line.
  - Output: A label, such as "spam" or "not spam."

#### Real-Life Example:
Imagine you want to classify whether a fruit is an apple or an orange based on its color, size, and weight. The output will be a category (e.g., "apple" or "orange"). This is a classification problem because the result is a discrete label.(This is classification problem because our algorithm has to predict output label(y label) from a finite number of possible outputs available )

---

### Key Differences
| **Aspect**            | **Regression**                          | **Classification**                      |
|------------------------|-----------------------------------------|-----------------------------------------|
| **Output Type**        | Continuous numerical value (e.g., 10.5) | Discrete label (e.g., "yes" or "no")    |
| **Goal**               | Predict "how much" or "how many"        | Predict "which category" or "class"     |
| **Examples**           | House price prediction, temperature     | Spam detection, image recognition       |
| **Algorithms**         | Linear Regression, Decision Tree Reg and etc...   | Logistic Regression, Decision Tree Classifier and etc... |

---


#### Basically we can say in regression we certainly not know the amount of possible outputs available (it can even be infinite(more often infinite)) ,  but on the other hand in classification we know the number of possible outputs available(it can be many but finite).

### Summary
- Use **regression** when you want to predict a number (e.g., price, temperature).
- Use **classification** when you want to predict a category (e.g., spam/not spam, apple/orange).