# **Understanding Rank, Null Space, and Linear Systems**

## **Problem Statement**
Consider the following matrix:

```
A = | 1  -2   4  |
    | -2  4  -8  |
    | 5  -10  20 |
```

We want to determine the **null space** of this matrix and understand how its **rank and nullity** affect the solutions to the system `A * x = b`.

---

## **1. Rank and Null Space in Linear Systems**
A matrix `A` represents a **linear transformation**, and its **rank and nullity** determine the behavior of solutions to the equation:

```
A * x = b
```

### **(a) Rank and Column Space (Range of A)**
- The **rank** of `A` is the number of **linearly independent columns**.
- The **column space** (or range) of `A` consists of all possible values of `A * x`.
- If `b` is **inside** the column space, then `A * x = b` has at least one solution.
- If `b` is **outside**, then `A * x = b` has no solution.

### **(b) Null Space (Kernel of A)**
- The **null space** consists of all vectors `x` that satisfy `A * x = 0`.


- Again telling, Here The equation 
𝐴
𝑥
=
0
represents the null space of A, which is the set of all vectors that get mapped to the zero vector under transformation by A.

   - This equation asks:
"For what vectors 
𝑥
 does the transformation by 
𝐴
 collapse to zero?"
The set of all such 
𝑥
 forms the null space (or kernel) of 
𝐴


- If `A` has **dependent columns**, then the null space is **nontrivial** (it contains more than just the zero vector).
- The number of **free variables** in `A * x = 0` equals the **nullity** (dimension of the null space).

- The dimensionality of the null space is inversely proportional to the rank of the matrix. 

### **(c) The Rank-Nullity Theorem**
The fundamental relation:

```
rank(A) + nullity(A) = number of columns of A
```

shows that the **larger the rank**, the **smaller the null space**, and vice versa.

`A` represents a matrix, specifically the coefficient matrix of a linear system

---

## **2. Applying This to the Given Problem**
The given matrix is:

```
A = | 1  -2   4  |
    | -2  4  -8  |
    | 5  -10  20 |
```

- **Rank = 1** (all columns are multiples of each other, so only one independent column exists).
- **Nullity = 3 - 1 = 2** (since the matrix has 3 columns).
- The **null space is a plane** (2D space in <code>R<sup>3</sup></code> , where `R` is 3 dimensional real space).

This means the transformation squishes 3D space **onto a line** (since rank = 1), leaving a **2D plane** as the set of solutions to `A * x = 0`.
Basically `A * x = 0` , is a null space of `A` . 

---

### **Key Takeaways**
- **Rank** determines how many dimensions remain after transformation.
- **Null space** represents the set of vectors that map to zero.
- **Rank-Nullity Theorem** helps find the dimensions of null space and column space.
- In this case, since the rank is 1, an entire **plane** is mapped to zero.

## Trivial and Non-Trivial Solutions

### Meaning of Trivial and Non-Trivial Solutions  

- **Trivial Solution**: A solution where all variables are **zero**.  
  - Example: \( x = 0 \) is a **trivial** solution of \( A x = 0 \).  
  - This means that the only vector in the **null space** of \( A \) is the **zero vector**.  

- **Non-Trivial Solution**: A solution where at least one variable is **not zero**.  
  - Example: If there exists \( x not equal to 0 \) such that \( A x = 0 \), then the null space contains other vectors **besides** the zero vector.  
  - This means that \( A \) has **linearly dependent columns**, leading to an infinite number of solutions.  

---

## Why "If the Null Space is Nontrivial, A is Not Invertible"?  

For a **square matrix \( A \) (n × n)**, the ability to **invert it** depends on whether it has **full rank**.  

- If **the null space is trivial** (only the zero vector is in it), then:
  - \( A x = 0 \) has only the **zero solution** , **unique solution** as only 0 vector satisfy \( A x = 0 \).
  - All columns of \( A \) are **linearly independent**.
  - \( A \) is **invertible** (full-rank).  

- If **the null space is nontrivial** (contains nonzero solutions), then:
  - \( A x = 0 \) has **infinite solutions**.
  - The columns of \( A \) are **linearly dependent**.
  - \( A \) is **not invertible** (singular matrix((i.e., its determinant must be 0))).  

---

## Intuition (Why Nontrivial Null Space Means No Inverse?)

1. **Invertible (Full Rank, Trivial Null Space)**  
   - \( A \) transforms inputs **one-to-one** → No information is lost.  
   - There is a unique solution for every output → \( A^{-1} \) exists.  

2. **Not Invertible (Rank Deficient, Nontrivial Null Space)**  
   - \( A \) squishes some inputs to **zero** (loses information).  
   - There is no **one-to-one mapping** → Cannot reverse the transformation → No \( A^{-1} \).  

---

## Example  

### **Case 1: Invertible Matrix (Trivial Null Space)**
```
A = | 1 2 | 
    | 3 4 |
```

- The equation \( A x = 0 \) only has the trivial solution \( x = 0 \).  
- The columns of \( A \) are **linearly independent**.  
- \( A \) is **invertible**.  

### **Case 2: Non-Invertible Matrix (Nontrivial Null Space)**
```
A = | 1 2 | 
    | 2 4 |
```

- The second column is **just twice the first column** → Linearly dependent.  
- \( A x = 0 \) has infinitely many solutions (not just \( x = 0 \)).  
- The null space contains **nonzero vectors** → \( A \) is **not invertible**.  

---

## Conclusion
- **Trivial null space** (only \( x = 0 \)) → \( A \) is **invertible**.  
- **Nontrivial null space** (more solutions exist) → \( A \) is **not invertible** (singular).  

This is why **if the null space(Ax=0) is nontrivial, \( A \) is not invertible**. 