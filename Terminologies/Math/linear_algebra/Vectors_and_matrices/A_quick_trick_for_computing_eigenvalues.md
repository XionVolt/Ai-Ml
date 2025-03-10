[See this video to know about A quick trick for computing eigenvalues](https://youtu.be/e50Bj7jn9IQ?si=g2II9oQb-508kdsw) 

[To discover this trick a 3 facts are](https://youtu.be/e50Bj7jn9IQ?si=n9-snFGlgS17Rglt&t=117)

1. [A track of matrix](https://youtu.be/e50Bj7jn9IQ?si=WEQc7A2ij77EVMJO&t=125)

```
| a  b | 
| c  d |
```
`Here trace of a matrix is a + d` is equal to sum of eigenvalues of a matrix (**λ<sub>1</sub>** + **λ<sub>2</sub>**) , 
   - Sum of trace of matrix is equal to sum of eigenvalues 
 - And mean(a,d) =  mean(**λ<sub>1</sub>**,**λ<sub>2</sub>**) = m (m stands for mean)


2. ad-bc (Determinant of a matrix) = **λ<sub>1</sub>** **λ<sub>2</sub>** (Product of eigenValues) = p (p stands for product)
3. [See this clip](https://youtu.be/e50Bj7jn9IQ?si=Adt095AraH8xHrBM&t=196)

## **Where this equation comes from ?**

Let's see

```math
 d^2 = m^2 - p
```

which is used to compute eigenvalues efficiently.

---

### **Step 1: Characteristic Equation of a 2×2 Matrix**

Consider a general **2×2 matrix**:

```
| a   b |
| c   d |
```

The characteristic equation is found by solving:

```math
 det(A - \lambda I) = 0
```

***Already know about this equation***

Subtracting `λI` from `A`, we get:

```
| a - λ   b    |
| c      d - λ |
```

Taking determinant:

```math
 (a - \lambda)(d - \lambda) - bc = 0
```

Expanding:

```math
  \lambda^2 - (a + d)\lambda + (ad - bc) = 0
```

This is the **quadratic equation** for eigenvalues.

---

### **Step 2: Defining `m` and `p`**

We define:

- **`m`** (Mean of diagonal elements): So  here `𝑚` represents the average or center value of the eigenvalues.

```math
 m = \frac{a + d}{2}
```

- **`p`** (Determinant of the matrix):

```math
 p = ad - bc
```

Rewriting the quadratic equation in terms of `m` and `p`:

```math
 \lambda^2 - 2m\lambda + p = 0
```

***2m because beacuse m is half of trace and we want exactly trace which is a+d (double of m)***

---

### **Step 3: Solving for Eigenvalues**

The roots of the quadratic equation:

```math
 \lambda = \frac{2m \pm \sqrt{(2m)^2 - 4p}}{2}
```

Simplifying:

```math
 \lambda = \frac{2m}{2} \pm \frac{\sqrt{4m^2 - 4p}}{2}
```
***In root we take 4 as a common***
```math
\lambda = \frac{2m}{2} = \frac{\sqrt{4(m^2 - p)}}{2}
```

Solving RHS:

```math
\frac{\sqrt{4(m^2 - p)}}{2} = \frac{\sqrt{4} \cdot \sqrt{m^2 - p}}{2} =  \frac{\cancel{2}\sqrt{m^2 - p}}{\cancel{2}}
```




```math
 \lambda = m \pm \sqrt{m^2 - p}
```

---

### **Step 4: Defining `d`**

We define:

```math
 d^2 = m^2 - p
```
***d(deviation) -> here deviation of eigenvalues from m , but Note:***

```math
 d^2 = m^2 - p
 ```    
 ***is just a convenient notation, not the actual discriminant. d helps simplify the eigenvalues `λ=m±d`***

now it gives:

```math
 d = \sqrt{m^2 - p}
```

So the eigenvalues can be written as:

```math
 \lambda_1, \lambda_2 = m \pm d
```

---

### **Final Conclusion**

- The equation `d^2 = m^2 - p` is derived from the quadratic formula.
- `d` represents the deviation of eigenvalues from `m`.
- This method provides an intuitive way to **compute eigenvalues** without solving the full quadratic equation.

This approach simplifies eigenvalue calculations and provides an easy way to visualize them on a **number line**.

# **Understanding Deviation of Eigenvalues from \( m \)**

## **1. Again What is \( m \)?**
\( m \) is the average of the diagonal elements (trace divided by dimension).  
For a **\( 2 X 2 \)** matrix:

```math
m = \frac{a + d}{2}
```

where:

```math
A =
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
```

## **2. Eigenvalues Formula (Shortcut)**
For a \( 2 X 2 \) matrix, eigenvalues  λ  are given by:

```math
\lambda_1, \lambda_2 = m \pm \sqrt{m^2 - p}
```

where:
- \( m \) = average of diagonal elements.
- \( p \) = determinant of the matrix \( p = ad - bc \).
```math 
\sqrt{m^2 - p}
``` 
- This represents the **deviation from \( m \)**.

## **3. What is Deviation?**
### **Simple Meaning**
Deviation tells us how much the eigenvalues move away from the central value \( m \).  
It is given by:

```math
d = \sqrt{m^2 - p}
```

### **Key Idea**
- If **\( d = 0 \)**, then both eigenvalues are exactly \( m \).
- If **\( d > 0 \)**, eigenvalues are **spread apart** (real and distinct).
- If **\( d < 0 \)**, eigenvalues are **complex conjugates**.

## **4. Example Calculation**
Consider the matrix:

```math
A =
\begin{bmatrix}
8 & 4 \\
2 & 6
\end{bmatrix}
```

- **Step 1:** Compute \( m \)

```math
m = \frac{8 + 6}{2} = 7
```

- **Step 2:** Compute determinant \( p \)

```math
p = (8)(6) - (4)(2) = 48 - 8 = 40
```

- **Step 3:** Compute deviation

```math
d = \sqrt{m^2 - p} = \sqrt{7^2 - 40} = \sqrt{49 - 40} = \sqrt{9} = 3
```

- **Step 4:** Find eigenvalues

```math
\lambda_1, \lambda_2 = 7 \pm 3
```

```math
\lambda_1 = 10, \quad \lambda_2 = 4
```

### **Interpretation**
- \( m = 7 \) is the **center**.
- The eigenvalues **deviate** 
```math
\pm 3
```
- λ<sub>1</sub> =m+d (the larger eigenvalue)
- λ<sub>2</sub> =m-d (the smaller eigenvalue)
- So, eigenvalues **move from 7 to 10 and 4**.

## **5. Visual Representation**
```
Eigenvalues:  4       7       10
              |-------|-------|
         -3  (Deviation)  +3
```
[Another Example from 3blue1brown](https://youtu.be/e50Bj7jn9IQ?si=t3dS4xx0EHjtEafh&t=296)

## **6. Why is Deviation Important?**
- Helps understand the **spread of eigenvalues**.
- If deviation is **zero**, eigenvalues are the same.
- If deviation is **negative**, eigenvalues are **complex**.

So this concept of center (m) and deviation (d) is mostly useful when we have only two eigenvalues

[Real application of this computation trick](https://youtu.be/e50Bj7jn9IQ?si=4mavFkpGYej8siyB&t=426)