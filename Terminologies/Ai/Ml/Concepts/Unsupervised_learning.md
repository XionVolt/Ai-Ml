# Unsupervised learning
***Unsupervided learning*** refers to the type of ml where the model learns from **unlabeled data** 

In unsupervised learning, the goal is to **discover patterns**, **structures**, **relationships** , or just something intresting in the provided data without any predefined labels or output.(Means we not provided with any output label , so data is *unlabeled*(**data with unknown answers**) unlike supervised learning where data we provided is with known answers(labeled)) The key characteristics of unsupervised learning are:
- **Goal**: Discover patterns, structures, or relationships, within the data. Here goal is to understand the data's underlying structure without prior knowledge of the output.
- **Output**: The output can be in the form of clusters, feature representations, or other forms of data organization that reveal underlying patterns.
- **Examples**: Clustering, dimensionality reduction, anomaly detection, and association rule mining.
- We call this unsupervised learning because we are not trying to supervise the algorithm , to give some quote right answer(output label) for every input .
- Instead we ask the algorithm the figure out all by itself that what's intresting , or what patterns or structures in the given data . 

# Clustering in Unsupervised Learning

## 📌 What is Clustering?
Clustering is a type of **unsupervised learning** where the goal is to group similar data points(into what we called **clusters**) together. It helps in discovering patterns, structures, and relationships in data.
## 🎯 Goal of Clustering
The primary objective of clustering is to identify **natural groups** in a dataset. It is used when we do not have labeled data but want to explore the inherent structure of the data.
[Examples and use of clustering by `Andrew Ng`](https://youtu.be/gG_wI_uGfIE?si=Kpk-XiI9-twsz0aj&t=137) 
Basically in the first example `Mr. Andrew Ng` gives us example of goggle news ,in which clustering algorithm works and that groups related news together(into groups (**clusters**)) , and we can say that this is a type of clustering technique they are using for this . 
Summarize - Clustering algorithms take data without labels and tries to automatically group similar data points into clusters . 

- [Another Example](https://youtu.be/81ymPYEtFOw?si=dvkulZJzIe2QNVOZ&t=605)

------- Dimensionality Reduction --------
- [See this to understand dimensionality reduction](https://youtu.be/81ymPYEtFOw?si=r2h5vAQbmpYBdP1T&t=757)
     - [Visualization](https://youtu.be/81ymPYEtFOw?si=8sDuaqCjJP633Drs&t=887)
     - [Anomaly Detection](https://youtu.be/81ymPYEtFOw?si=P9e1ZiFGZ6vk0aRm&t=1030)
     - [Association Rule based learning](https://youtu.be/81ymPYEtFOw?si=nRos0o41Ln5IdaWn&t=1097)

----
# Association Rule Mining
## What is Association Rule Mining?

- It is a technique to find patterns, associations, or relationships between items in large datasets.

- No labels (no "right" or "wrong" output for corrsponding features) — it just discovers patterns hidden in the data.

- Very common in market basket analysis (analyzing customer purchases).

### 📚 Example:
Imagine you run a supermarket. After analyzing all customer bills, you find:

- **"If a customer buys bread and butter, they also buy milk 70% of the time."**

This can be written as a rule:

`{Bread, Butter} ➔ {Milk}`

Here:

`{Bread, Butter}` is the **antecedent** (the "if" part).

`{Milk}` is the consequent (the "then" part).

You didn't tell the machine what to look for — you just gave it data, and it found this pattern on its own.
That's why it's unsupervised!

### ⚡ Some Key Terms:
- **Support**: How often the items appear together.

- **Confidence**: How often the rule has been true (given the "if" part, how often the "then" part happens).

- **Lift**: How much more likely the "then" part is, compared to random chance.

- **Interest Measure**: A measure of how much the rule is interesting to the user.

- **Antecedent**: (One that precedes another), basially item(s) found in the data before leading to another item.

- **Consequent**: (One that follows another), basially item(s) found in the data after leading to another item.

***You can think *Antecedent* as "if" and *Consequent* as "then":***

> IF you have antecedent, THEN you will likely have consequent.


