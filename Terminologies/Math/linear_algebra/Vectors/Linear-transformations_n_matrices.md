# Read this , to deep dive in topics of Linear transformations and matrices by `3blue1brown`: 
https://www.3blue1brown.com/lessons/linear-transformations

**And you can also watch videos of 3blue1brown** of the cooresponding topic of the link that is related to `3blue1brown`

## Summary and Main things to remember , things we not understand

### Let's understand this term : `Transformation`
Transformation is essentially a fancy word for function; it's something that takes in inputs, and spits out some output for each one (the thing we do in day to day life in programming). Specifically, in the context of linear algebra, we think about transformations that take in some vector and spit out another vector.

### Linear transformation (What transformations are linear ?)
***Transformation is linear if it has two properties*** :
- All lines must remain lines(especially talking about grid lines) without getting curved , and the origin must remain fixed in place . 
- Grid lines remains parallel and evenly spaced

### Solving Linear Transformation Problems

This guide explains how to solve **linear transformation problems** step-by-step using matrix multiplication. The solution is generalizable to any number of dimensions or transformed basis vectors.

---

## Key Concept: Linear Transformation via Matrix Multiplication
A **linear transformation** maps an input vector $\mathbf{v}$ to a transformed vector $\mathbf{v'}$ using a transformation matrix $A$:

$$
\mathbf{v'} = A \cdot \mathbf{v}
$$

The matrix $A$ is constructed by placing the transformed basis vectors $\hat{i}, \hat{j}, \dots ,\hat{n} $ as its **columns**.

---

## Example Problem 1
### Problem Statement:
Given the transformation:

$$
\hat{i} \to \begin{bmatrix} -1 \\ 1 \end{bmatrix}, \quad \hat{j} \to \begin{bmatrix} -2 \\ -1 \end{bmatrix}
$$

and an input vector:

$$
\mathbf{v} = \begin{bmatrix} -3 \\ -1 \end{bmatrix},
$$

find how the input vector is transformed.

### Step 1: Construct the Transformation Matrix

$$
A = \begin{bmatrix} -1 & -2 \\ 1 & -1 \end{bmatrix}
$$

### Step 2: Apply the Transformation

$$
\mathbf{v'} = A \cdot \mathbf{v} = \begin{bmatrix} -1 & -2 \\ 1 & -1 \end{bmatrix} \cdot \begin{bmatrix} -3 \\ -1 \end{bmatrix}
$$

### Step 3: Perform the Matrix Multiplication

$$
\mathbf{v'} = \begin{bmatrix} (-1)(-3) + (-2)(-1) \\ (1)(-3) + (-1)(-1) \end{bmatrix} = \begin{bmatrix} 3 + 2 \\ -3 + 1 \end{bmatrix} = \begin{bmatrix} 5 \\ -2 \end{bmatrix}
$$

### Final Answer:

$$
\mathbf{v'} = \begin{bmatrix} 5 \\ -2 \end{bmatrix}
$$

---

## Example Problem 2 (3D Transformation)
### Problem Statement:
Given:
- $\hat{i} \to \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}$,
- $\hat{j} \to \begin{bmatrix} 1 \\ -1 \\ 3 \end{bmatrix}$,
- $\hat{k} \to \begin{bmatrix} 0 \\ 2 \\ -1 \end{bmatrix}$,

and an input vector:

$$
\mathbf{v} = \begin{bmatrix} 3 \\ -2 \\ 1 \end{bmatrix},
$$

find the transformed vector $\mathbf{v'}$.

### Step 1: Construct the Transformation Matrix

$$
A = \begin{bmatrix} 2 & 1 & 0 \\ 1 & -1 & 2 \\ 0 & 3 & -1 \end{bmatrix}
$$

### Step 2: Apply the Transformation

$$
\mathbf{v'} = A \cdot \mathbf{v} = \begin{bmatrix} 2 & 1 & 0 \\ 1 & -1 & 2 \\ 0 & 3 & -1 \end{bmatrix} \cdot \begin{bmatrix} 3 \\ -2 \\ 1 \end{bmatrix}
$$

### Step 3: Perform the Matrix Multiplication

$$
\mathbf{v'} = \begin{bmatrix} (2)(3) + (1)(-2) + (0)(1) \\
(1)(3) + (-1)(-2) + (2)(1) \\
(0)(3) + (3)(-2) + (-1)(1) \end{bmatrix} = \begin{bmatrix} 6 - 2 + 0 \\
3 + 2 + 2 \\
0 - 6 - 1 \end{bmatrix} = \begin{bmatrix} 4 \\
7 \\
-7 \end{bmatrix}
$$

### Final Answer:

$$
\mathbf{v'} = \begin{bmatrix} 4 \\ 7 \\ -7 \end{bmatrix}
$$

---

## Generalized Steps for Any Linear Transformation
1. **Construct the Transformation Matrix $A$:** Place the transformed basis vectors as the columns of the matrix.
2. **Multiply $A$ by the Input Vector $\mathbf{v}$:** Use standard matrix multiplication rules.
3. **Simplify the Result:** Perform the arithmetic to get the transformed vector.

This method works for any number of dimensions or transformed basis vectors!

---

### Now if our input vector is in a linear combination $$ v = \hat{i},\hat{j} ,\dots,\hat{n}   $$

#### Example: Transformation of a Vector

Given an untransformed vector $$ \mathbf{v} = -1\hat{i} + 2\hat{j} $$, and the transformed basis vectors:
- Transformed $$ \hat{i} = \begin{bmatrix} 1 \\ -2 \end{bmatrix} $$
- Transformed $$ \hat{j} = \begin{bmatrix} 3 \\ 0 \end{bmatrix} $$,

we want to find the transformed vector $$ \mathbf{v}' $$.

---

##### Step 1: Transformation Matrix
The transformation matrix $$ A $$ is constructed by placing the transformed $$ \hat{i} $$ and $$ \hat{j} $$ as its columns:

$$
A = \begin{bmatrix} 1 & 3 \\ -2 & 0 \end{bmatrix}
$$

---

##### Step 2: Original Vector
The original vector $$ \mathbf{v} = -1\hat{i} + 2\hat{j} $$ is written as a column vector:

$$
\mathbf{v} = \begin{bmatrix} -1 \\ 2 \end{bmatrix}
$$

---

##### Step 3: Compute the Transformed Vector
The transformed vector $$ \mathbf{v}' $$ is obtained by multiplying the transformation matrix $$ A $$ with the original vector $$ \mathbf{v} $$:

$$
\mathbf{v}' = A \mathbf{v}
$$

Substitute the values:

$$
\mathbf{v}' = \begin{bmatrix} 1 & 3 \\ -2 & 0 \end{bmatrix} \begin{bmatrix} -1 \\ 2 \end{bmatrix}
$$

Perform the matrix multiplication:

$$
\mathbf{v}' = \begin{bmatrix} (1)(-1) + (3)(2) \\ (-2)(-1) + (0)(2) \end{bmatrix}
$$

$$
\mathbf{v}' = \begin{bmatrix} -1 + 6 \\ 2 + 0 \end{bmatrix}
$$

$$
\mathbf{v}' = \begin{bmatrix} 5 \\ 2 \end{bmatrix}
$$

---

##### Step 4: Linear Combination of Transformed Basis Vectors
The transformed vector $$ \mathbf{v}' $$ can also be expressed as a linear combination of the transformed $$ \hat{i} $$ and $$ \hat{j} $$:

$$
\mathbf{v}' = -1 \cdot \text{(transformed } \hat{i}) + 2 \cdot \text{(transformed } \hat{j})
$$

Substitute the transformed basis vectors:

$$
\mathbf{v}' = -1 \cdot \begin{bmatrix} 1 \\ -2 \end{bmatrix} + 2 \cdot \begin{bmatrix} 3 \\ 0 \end{bmatrix}
$$

$$
\mathbf{v}' = \begin{bmatrix} -1 \\ 2 \end{bmatrix} + \begin{bmatrix} 6 \\ 0 \end{bmatrix}
$$

$$
\mathbf{v}' = \begin{bmatrix} 5 \\ 2 \end{bmatrix}
$$

---

## Final Answer
The transformed vector $$ \mathbf{v}' $$ is:

$$
\mathbf{v}' = \begin{bmatrix} 5 \\ 2 \end{bmatrix}
$$

*See this clip to make your understanding more clear of this thing*

https://youtu.be/kYB8IZa5AuE?si=dVlmqc0LtVp-4LJm&t=337 , by  `3blue1brown`
