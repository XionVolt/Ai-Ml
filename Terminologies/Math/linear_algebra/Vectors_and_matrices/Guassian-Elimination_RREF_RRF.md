1. [Representing linear system as matrices](https://youtu.be/RgnWMBpQPXk?si=EbYxFtlYNYqA1oQh)

2. [Make Augmented Matrix](https://youtu.be/RgnWMBpQPXk?si=YRSBB0TWmU_lPJZg&t=141)

3. [Perform operations on Augmented matrix](https://youtu.be/RgnWMBpQPXk?si=4V8f8C_CQOYMz4dy&t=208)

4. [Solve equation (find solutions of system of equation) after you find uppper triangular matrix](https://youtu.be/RgnWMBpQPXk?si=J4TLXo7MIzEHap3W&t=520)
    - Back Substitution - You start with last equation and go towards upwards (first equation) . Then you find all the solutions(values of variables , or we can also say components of variables vector)  as you keep going upwards . 

## Reduced row echelon form (RREF)

In reduce row echelon form , we eliminate both above the pivot and below the pivot . 
But in guassian elimination we eliminate only below the pivot .


[What is RREF?](https://youtu.be/1rBU0yIyQQ8?si=KS24ZngE5MQs-MUH&t=17) 


[To make algebra simplar we can also divide the row by some common factor](https://youtu.be/1rBU0yIyQQ8?si=lOSz2SogUPTvE-iF&t=198)

[What it means if two rows of A(Coeffiecient matrix) has same ](https://youtu.be/1rBU0yIyQQ8?si=wqmJKdNPRX3O1GiI&t=299) 
   - It means those same rows representing the same equation .

## **Understanding Pivots in a Matrix**

A **pivot** in a matrix is the first **nonzero** element in a row when performing row operations (such as Gaussian elimination). It plays a crucial role in solving systems of linear equations, determining rank, and finding inverse matrices.

---

## **Key Properties of a Pivot:**
1. **It is the first nonzero element** in a row from left to right.
2. **It must be in a leading position** (each pivot should be to the right of the pivot in the previous row).
3. In **Row Echelon Form (REF)**, a pivot can be any nonzero number.
4. In **Reduced Row Echelon Form (RREF)**, pivots are always **1**, and all other elements in the pivot column are **0**.
5. The columns that have pivots are called **pivot columns**.
---

## **The Difference Between REF and RREF**
The difference between **Reduced Row Echelon Form (RREF)** and **Row Echelon Form (REF)** lies in the additional constraints imposed on RREF.

### **1. Row Echelon Form (REF)**
A matrix is in **row echelon form** if:
- The leading entry (first nonzero number from the left) of each nonzero row is to the **right** of the leading entry in the row above.(Simply saying that the leading entry(first nonzero number) in a row is to the **right** of the leading entry in the row above.)
- Any rows consisting entirely of **zeros** are at the **bottom**.
  - This means that if there are any rows that contain only **zeroes**, they must be placed at the **bottom** of the matrix. 
  - **Example:**
    ```
    | 1  2  3 |
    | 0  1  4 |
    | 0  0  0 |
    ```
    - The **first two rows** contain nonzero elements.
    - The **last row** contains only **zeros**, so it is placed at the **bottom**.
  - If a zero row appears **above** a nonzero row, the matrix is **not** in row echelon form. **Incorrect example:**
    ```
    | 1  2  3 |
    | 0  0  0 |  ❌ (Zero row should be at the bottom!)
    | 0  1  4 |
    ```
    - To correct this, swap rows so that the zero row moves to the bottom:
      ```
      | 1  2  3 |
      | 0  1  4 |
      | 0  0  0 |
      ```

- The leading coefficient (**pivot**) of a nonzero row is **nonzero** (but not necessarily 1).

#### **Example of REF:**
```
| 1  2  3  4 |
| 0  1  5  6 |
| 0  0  2  8 |
```
- The first pivot (1) is in the first column.
- The second pivot (1) is in the second column and to the right of the first pivot.
- The third pivot (2) is in the third column.

### **2. Reduced Row Echelon Form (RREF)**
A matrix is in **reduced row echelon form** if:
- It satisfies all the conditions of **row echelon form (REF)**.
- ADDITIONAL CONSTRAINT: Every pivot is **1**, and it is the **only nonzero entry in its column** (all other entries in that column must be 0).
- In rref form, the zero row can exist but it must be at the bottom.

#### **Example of RREF:**
```
| 1  0  0  a |
| 0  1  0  b |
| 0  0  1  c |
```
- Each leading 1 is the **only nonzero entry** in its column.
- The pivots are in echelon form.

### **Key Differences:**
| Feature  | REF (Row Echelon Form) | RREF (Reduced Row Echelon Form) |
|----------|-------------------------|---------------------------------|
| Pivots   | Can be any nonzero number | Always **1** |
| Columns of pivots | Can have other nonzero elements | Each pivot is the **only nonzero** element in its column |
| Further reduction | Not fully reduced  | Fully reduced |
| Uniqueness | Not unique (multiple REF forms) | Unique for a given matrix |

### **Conclusion:**
- **REF** is useful for solving linear systems up to an intermediate stage.
- **RREF** gives a unique, final simplified form ideal for finding solutions directly.

---

## **Solving Systems of Linear Equations Using REF and RREF**

### **System of Equations:**
```
2x + 3y + 4z = 10
5x + 6y + 7z = 20
8x + 9y + 10z = 30
```

### **Step 1: Convert to Augmented Matrix**
```
| 2  3  4 | 10 |
| 5  6  7 | 20 |
| 8  9 10 | 30 |
```

### **Step 2: Convert to Row Echelon Form (REF)**
After row operations:
```
| 2  3  4  | 10 |
| 0  1  2  |  5 |
| 0  0  1  |  3 |
```
Now, we can solve the system using **back-substitution**.

### **Step 3: Convert to Reduced Row Echelon Form (RREF)**
```
| 1  0  0 |  1 |
| 0  1  0 |  2 |
| 0  0  1 |  3 |
```
From RREF, the solution is:
```
x = 1, y = 2, z = 3
```

---

## **Finding Rank of a Matrix**
The **rank** of a matrix can also be defined as the number of pivots (nonzero leading entries) .

---


If all columns have pivots, then the vectors are **linearly independent**.

---

### **Conclusion**
- **Pivot**: The first nonzero entry in a row.
- **REF**: Step in Gaussian elimination, used to solve systems by back-substitution.
- **RREF**: Fully reduced form, unique for a matrix, used to find exact solutions.
- **Rank**: Here we can say Number of pivots in REF.
- **Linear Independence**: All vectors must have pivots to be independent.