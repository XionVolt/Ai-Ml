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
A **linear transformation** maps an input vector **`v`** to a transformed vector **`v'`** using a transformation matrix **`A`**:

```
v' = A * v
```

The matrix **`A`** is constructed by placing the transformed basis vectors **`i, j, ..., n`** as its **columns**.

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
v' = | (3 + 2)  |
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

find the transformed vector **`v'`**.

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
1. **Construct the Transformation Matrix `A`:** Place the transformed basis vectors as the columns of the matrix.
2. **Multiply `A` by the Input Vector `v`:** Use standard matrix multiplication rules.
3. **Simplify the Result:** Perform the arithmetic to get the transformed vector.

This method works for any number of dimensions or transformed basis vectors!

---

### Now if our input vector is in a linear combination **`v = i, j, ..., n`**

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
we want to find the transformed vector **`v'`**.

---

##### Step 1: Transformation Matrix
The transformation matrix **`A`** is constructed by placing the transformed **`i`** and **`j`** as its columns:

```
A = |  1  3 |
    | -2  0 |
```

---

##### Step 2: Original Vector
The original vector ```v = -1i + 2j``` is written as a column vector (*as we know that any vector coordinates are scalars that actually scale basis vectors*):

```
v = | -1 |
    |  2 |
```

---

##### Step 3: Compute the Transformed Vector
The transformed vector **`v'`** is obtained by multiplying the transformation matrix **`A`** with the original vector **`v`**:

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
v' = | (1 * -1 + 3 * 2)  |
     | (-2 * -1 + 0 * 2) |

   = | -1 + 6 |
     | 2 + 0  |

   = | 5  |
     | 2  |
```

---

##### Step 4: Linear Combination of Transformed Basis Vectors
The transformed vector **`v'`** can also be expressed as a linear combination of the transformed **`i`** and **`j`**:

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
*We can do this thing for other input vectors too because we know that vector coordinates are scalars that actually scale basis vectors , like they do above*

---

## Final Answer
The transformed vector **`v'`** is:

```
v' = | 5  |
     | 2  |
```

[See this clip to make your understanding more clear of this](https://youtu.be/kYB8IZa5AuE?feature=shared&t=337)


*When you see a matrix you can interpret it like a certain transformation of space*
[See this clip to understand this thing visually](https://youtu.be/kYB8IZa5AuE?si=0SnA5ybZogD4K6ds&t=614)


## Transformation Matrix Problem Explanation and Solution

### Problem Statement
The question asks us to determine the transformation matrix **`A`** that satisfies the following behaviors:

1. The vector 
```
| 2 |  
| 3 |   
```
is transformed into the vector 
```
| 8 |  
| 1 |  
```
2. The vector 
```
| -2 |  
|  1 |  
```
is transformed into the vector 
```
|  0 |  
|  3 |  
```

Our task is to find the 2x2 matrix **`A`** such that:
- **`A`** applied to 
```
| 2 |  
| 3 |  
```
gives 
```
| 8 |  
| 1 |  
```
- **`A`** applied to 
```
| -2 |  
|  1 |  
```
gives 
```
|  0 |  
|  3 |  
```

### Solution

Let the transformation matrix **`A`** be represented as:
```
| a  b |  
| c  d |  
```

This means the transformation is represented mathematically as:
1. 
```
| a  b |   *   | 2 |   =  | 8 |  
| c  d |       | 3 |      | 1 |  
```
   
2. 
```
| a  b |   *   | -2 |  =   |  0 |  
| c  d |       |  1 |      |  3 |  
```

#### Step 1: Write the equations for transformations

From the first transformation:
```
| a  b |   *  | 2 |   =  | 8 |  
| c  d |       | 3 |      | 1 |  
```

This gives us two equations:
- 2a + 3b = 8  (Equation 1)  
- 2c + 3d = 1  (Equation 2)  

From the second transformation:
```
| a  b |   *   | -2 |  =   |  0  |  
| c  d |       |  1 |      |  3  |  
```

This gives us two equations:
- -2a + b = 0  (Equation 3)  
- -2c + d = 3  (Equation 4)  

#### Step 2: Solve the system of equations

From Equation 3:  
- Solve for b:  
  b = 2a  

Substitute b = 2a into Equation 1:  
2a + 3(2a) = 8  
2a + 6a = 8  
8a = 8  
a = 1  

Using a = 1 in b = 2a:  
b = 2(1) = 2  

From Equation 4:  
- Solve for d:  
  d = 3 + 2c  

Substitute d = 3 + 2c into Equation 2:  
2c + 3(3 + 2c) = 1  
2c + 9 + 6c = 1  
8c = -8  
c = -1  

Using c = -1 in d = 3 + 2c:  
d = 3 + 2(-1) = 1  

#### Step 3: Write the transformation matrix

The transformation matrix **`A`** is:

```
| 1   2 |  
| -1  1 |  
```

#### Final Answer:
The transformation matrix that satisfies the given behaviors is:
```
| 1   2 |  
| -1  1 |  
```


### Formal Properties of Linear Transformations

Linear transformations are a special class of transformations in linear algebra that adhere to strict mathematical rules. These transformations ensure that grid lines remain parallel and evenly spaced and origin remains fixed when applied. The two key properties of a linear transformation are:

#### 1. Additivity Property

This property states that the transformation of the sum of two vectors is the same as the sum of the transformations of those vectors. Mathematically:
```
L( v + w ) = L( v ) + L( w )
```

##### Explanation:
- If you have two vectors `v` and `w` in a space, and you first add them to get `v + w`, the transformation `L` applied to this result is the same as transforming `v` and `w` individually and then adding their transformed results.
- This property ensures that linear transformations preserve the structure of vector addition.

### Example:
Let:
```
v =  | 1 |
     | 2 |

w =  | 3 |
     | 4 |
```
And the linear transformation `L` is represented by the matrix:
```
L = | 2 1 | 
    | 1 1 |
```
1. First, compute `v + w`:
```
v + w = | 1 + 3 | = | 4 | 
        | 2 + 4 |   | 6 |
```
2. Apply `L` to `v + w`:
```
L( v + w ) = | 2(4) + 1(6) | = | 14 | 
             | 1(4) + 1(6) |   | 10 |
```
3. Apply `L` to `v`:
```
L( v ) =   | 2(1) + 1(2) | = | 4 | 
           | 1(1) + 1(2) |   | 3 |
```
4. Apply `L` to `w`:
```
L( w ) = | 2(3) + 1(4) | = | 10 | 
         | 1(3) + 1(4) |   | 7  |
```
5. Add the transformed results:
```
L( v ) + L( w ) = | 4 + 10 | = | 14 | 
                  | 3 + 7  |   | 10 |
```
6. Compare the result to `v + w`:
```
L( v + w ) = L( v ) + L( w ) =  | 14 | 
                                | 10 |   
```
In this example, the linear transformation `L` preserves the structure of vector addition, as the transformed result of `v + w` is the same as the sum of the transformed results of `v` and `w`. We also call this property with the term **"additivity"**.

---

### 2. Scaling Property

This property states that scaling (multiplying) a vector by a scalar before applying a transformation is the same as scaling the transformed vector after applying the transformation. Mathematically:
```
L( s * v ) = s * L( v )
```
### Explanation:
- If a vector `v` is scaled by a scalar `s`, the transformation `L` applied to the scaled vector produces the same result as scaling the transformed vector `L(v)` by the scalar `s`.
- This property ensures that linear transformations preserve the structure of scalar multiplication.

### Example:
Let:
```
v =  | 1 |
     | 2 |
```
And the linear transformation `L` is represented by the matrix:
```
L = | 2 1 | 
    | 1 1 |
```
1. Scale `v` by 2:
```
s * v = | 2(1) | = | 2 | 
        | 2(2) |   | 4 |
```
2. Apply `L` to the scaled vector:
```
L( s * v ) = | 2(2) + 1(4) | = | 8 | 
             | 1(2) + 1(4) |   | 6 |
```
3. Now , Scale the transformed vector by 2:
```
s * L( v ) = | 2(1) + 1(2) | = | 3 | 
             | 1(1) + 1(2) |   | 3 |
```
4. Compare the result to `s * v`:
```
s * L( v ) = s * | 2(1) + 1(2) | = | 4 |  => 2 * | 4 | = | 8 |
                 | 1(1) + 1(2) |   | 3 |         | 3 |   | 6 |
```
In this example, the linear transformation `L` preserves the structure of scaling, as the transformed result of `s * v` is the same as the scaled result of `L(v)`. We also call this property with term **"Homogeneity"**.

There are few transformations that have special names : Of which two can be seen by going to these links : 
1. [Rotation](https://www.3blue1brown.com/lessons/linear-transformations#rotation)
2. [Shear](https://www.3blue1brown.com/lessons/linear-transformations#shear)