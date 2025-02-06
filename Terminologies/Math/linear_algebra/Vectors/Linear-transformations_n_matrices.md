# Read this to deep dive into topics of Linear transformations and matrices by `3blue1brown`: 
https://www.3blue1brown.com/lessons/linear-transformations

**And you can also watch videos of 3blue1brown** on the corresponding topic of the link that is related to `3blue1brown`.

## Summary and Main things to remember, things we do not understand

### Let's understand this term: `Transformation`
Transformation is essentially a fancy word for function; it's something that takes in inputs and spits out some output for each one (the thing we do in day-to-day life in programming). Specifically, in the context of linear algebra, we think about transformations that take in some vector and spit out another vector.

### Linear transformation (What transformations are linear?)
***A transformation is linear if it has two properties***:
- All lines must remain lines (especially talking about grid lines) without getting curved, and the origin must remain fixed in place.
- Grid lines remain parallel and evenly spaced.

### Solving Linear Transformation Problems

This guide explains how to solve **linear transformation problems** step-by-step using matrix multiplication. The solution is generalizable to any number of dimensions or transformed basis vectors.

---

## Key Concept: Linear Transformation via Matrix Multiplication
A **linear transformation** maps an input vector **v** to a transformed vector **v'** using a transformation matrix **A**:

```
v' = A * v
```

The matrix **A** is constructed by placing the transformed basis vectors **i, j, ..., n** as its **columns**.

---

## Example Problem 1
### Problem Statement:
Given the transformation:

```

i = | -1 |
    |  1 |

j = | -2 |
    | -1 |

```

and an input vector:

```
v =  | -3 |
     | -1 |
```

find how the input vector is transformed.

### Step 1: Construct the Transformation Matrix

```
A = | -1  -2 |
    |  1  -1 |
```

### Step 2: Apply the Transformation

```
v' = A * v = | -1  -2 | * | -3 |
             |  1  -1 |   | -1 |
```

### Step 3: Perform the Matrix Multiplication

```
v' = | (3 + 2) |
     | (-3 + 1) |

     = |  5  |
       | -2  |
```

### Final Answer:

```
v' = |  5  |
     | -2  |
```

---

## Example Problem 2 (3D Transformation)
### Problem Statement:
Given transformed:
```
i =    |  2  |
       |  1  |
       |  0  |

j =    |  1  |
       | -1  |
       |  3  |

k =    |  0  |
       |  2  |
       | -1  |

```

and an input vector:
```
v = |  3  |
    | -2  |    
    |  1  |
```

find the transformed vector **v'**.

### Step 1: Construct the Transformation Matrix *by placing i, j, k transformed basis vectors as its columns*

```
A = | 2  1  0 |
    | 1 -1  2 |
    | 0  3 -1 |
```

### Step 2: Apply the Transformation

```
v' = A * v = | 2  1  0 | * | 3  |
             | 1 -1  2 |   | -2 |
             | 0  3 -1 |   | 1  |
```

### Step 3: Perform the Matrix Multiplication

```
v' = | (6 - 2 + 0) |
     | (3 + 2 + 2) |
     | (0 - 6 - 1) |

     = |  4  |
       |  7  |
       | -7  |
```

### Final Answer:

```
v' = |  4  |
     |  7  |
     | -7  |
```

---

## Generalized Steps for Any Linear Transformation
1. **Construct the Transformation Matrix A:** Place the transformed basis vectors as the columns of the matrix.
2. **Multiply A by the Input Vector v:** Use standard matrix multiplication rules.
3. **Simplify the Result:** Perform the arithmetic to get the transformed vector.

This method works for any number of dimensions or transformed basis vectors!

---

### Now if our input vector is in a linear combination **v = i, j, ..., n**

#### Example: Transformation of a Vector

Given an untransformed vector ```v = -1i + 2j```, and the transformed basis vectors:
```
Transformed i=          |  1  |
                        | -2  | 
```          


```
Transformed j=          |  3  |
                        |  0  | 
```
we want to find the transformed vector **v'**.

---

##### Step 1: Transformation Matrix
The transformation matrix **A** is constructed by placing the transformed **i** and **j** as its columns:

```
A = |  1  3 |
    | -2  0 |
```

---

##### Step 2: Original Vector
The original vector ```v = -1i + 2j``` is written as a column vector:

```
v = | -1 |
    |  2 |
```

---

##### Step 3: Compute the Transformed Vector
The transformed vector **v'** is obtained by multiplying the transformation matrix **A** with the original vector **v**:

```
v' = A * v
```

Substitute the values:

```
v' = |  1  3 | * | -1 |
     | -2  0 |   |  2 |
```

Perform the matrix multiplication:

```
v' = | (1 * -1 + 3 * 2) |
     | (-2 * -1 + 0 * 2) |

     = | -1 + 6 |
       | 2 + 0  |

     = | 5  |
       | 2  |
```

---

##### Step 4: Linear Combination of Transformed Basis Vectors
The transformed vector **v'** can also be expressed as a linear combination of the transformed **i** and **j**:

```
v' = -1 * (transformed i) + 2 * (transformed j)
```

Substitute the transformed basis vectors:

```
v' = -1 * |  1  |  + 2 * | 3  |
          |  -2 |        | 0  |
     
     = | -1  | + | 6 |
       | 2   |   | 0 |
       
     = | 5  |
       | 2  |
```

---

## Final Answer
The transformed vector **v'** is:

```
v' = | 5  |
     | 2  |
```

*See this clip to make your understanding more clear of this thing*

https://youtu.be/kYB8IZa5AuE?si=dVlmqc0LtVp-4LJm&t=337, by `3blue1brown`