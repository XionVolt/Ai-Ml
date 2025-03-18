[Documentation by 3blue1brown](https://www.3blue1brown.com/lessons/cross-products)

[See video for visualization by 3blue1brown](https://youtu.be/eu6i7WJeinw?si=T_etEcREf6wtHgSN)

[How to take dot product(geometrically)](https://youtu.be/eu6i7WJeinw?si=q-K6RNPXXwFZvzzl&t=40)

```python
import numpy
a = numpy.array([1, 2, 3])
b = numpy.array([4, 5, 6])
numpy.cross(a, b)
```
Pythonic way to compute cross product


In cross Product(also called the perpendicular or wedge product) order of Vectors(how they multiplying) change signs .
Example: 

$$
\overrightarrow{a} \times \overrightarrow{b} = - \overrightarrow{b} \times \overrightarrow{a}
$$
***If `a` is on left side then cross product is postive else negative , `a` and `b` can be any vecotor*** 
[Btw clockwise and counter-clockwise, also the way to know if cross product is postive or negative](https://www.3blue1brown.com/lessons/cross-products#two-dimensions)


[Remember ordering like when cross product is postive and when negative](https://youtu.be/eu6i7WJeinw?si=sPK3c7f-JxthAP-E&t=99)

Note : [***a***X***b***(Cross Product) can also be find using determinant , by placing ***a*** and ***b*** in 2x2 matrix columns](https://youtu.be/eu6i7WJeinw?si=jQt02iTQzwCA2OPJ&t=157) **This is because determinant is just how much area formed by 2 vectors , or we can also say , ***The factor by which linear transformation changes any area (of the grid squares)*****


# Cross Product of Vectors

## 1. Cross Product of 2D Vectors

The **cross product** of two **2D vectors** A = (Ax, Ay) and B = (Bx, By) results in a **scalar** value given by:

AxB = Ax * By - Ay * Bx

### Example (2D)
Let A = (3, 4) and B = (2, 1):

(3,4) x (2,1) = (3 * 1) - (4 * 2) = 3 - 8 = -5

The result is **-5**, indicating a clockwise direction.

---

## 2. Cross Product of 3D Vectors

The **cross product** of two **3D vectors** A = (Ax, Ay, Az) and B = (Bx, By, Bz) results in another **3D vector**, given by the determinant:

A x B =
|   i   j   k  |
|  Ax  Ay  Az  |
|  Bx  By  Bz  |

Expanding the determinant:

A x B =
( Ay * Bz - Az * By ) i -
( Ax * Bz - Az * Bx ) j +
( Ax * By - Ay * Bx ) k

### Example (3D)
Let A = (1, 2, 3) and B = (4, 5, 6):

A x B =
|  i   j   k  |
|  1   2   3  |
|  4   5   6  |

Expanding:

A x B = (2 * 6 - 3 * 5) i - (1 * 6 - 3 * 4) j + (1 * 5 - 2 * 4) k

= (-3, 6, -3)

The result is the vector **(-3, 6, -3)**.

---

## 3. Cross Product and Parallelogram Area

The magnitude of the cross product of two vectors gives the **area of the parallelogram** formed by them.

### How to Find the area of a parallelogram 
For two vectors A and B, the area of the parallelogram they form is given by:

Area = |A x B|

For 2D vectors:

Area = |Ax * By - Ay * Bx|

For 3D vectors:

Area of parallelogram formed by $A$ and $B$(where $A$ and $B$ are 3d vectors) : $A \times B = (A_yB_z - A_zB_y)i + (A_zB_x - A_xB_z)j + (A_xB_y - A_yB_x)k$
***This formula comes from the fact that the cross product gives a vector perpendicular to A and B, whose magnitude represents the parallelogram's area.***

But If you were looking for the actual cross product vector, you would drop the square root and keep the individual components, here's how it looks:
```math
\mathbf{A} \times \mathbf{B} =
\begin{bmatrix} A_x \\ A_y \\ A_z \end{bmatrix}
\times
\begin{bmatrix} B_x \\ B_y \\ B_z \end{bmatrix}
=
\begin{bmatrix}
A_y B_z - A_z B_y \\
A_z B_x - A_x B_z \\
A_x B_y - A_y B_x
\end{bmatrix}
```

Alternatively, using the determinant notation:

```math
\mathbf{A} \times \mathbf{B} =
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
A_x & A_y & A_z \\
B_x & B_y & B_z
\end{vmatrix}
```

Expanding this determinant:

```math
(A_y B_z - A_z B_y) \hat{i}
- (A_x B_z - A_z B_x) \hat{j}
+ (A_x B_y - A_y B_x) \hat{k}
```
***Now you say, why each cofactor is multiplied by a unit vector?***

Because Each of the 2×2 determinants (minors) computes a scalar value that corresponds to a component of the final vector. However, since the result of a cross product is a vector, we must associate each of these computed values with their respective unit vector direction: 
- The determinant $(A_yB_z - A_zB_y)$ gives the x-component $\rightarrow$ It must be multiplied by $\hat{i}$, means scaling $\hat{i}$ with some value.
- The determinant $(A_zB_x - A_xB_z)$ gives the y-component $\rightarrow$ It must be multiplied by $\hat{j}$ , means scaling $\hat{j}$ with some value.
- The determinant $(A_xB_y - A_yB_x)$ gives the z-component $\rightarrow$ It must be multiplied by $\hat{k}$ , means scaling $\hat{k}$ with some value.

**So its more for convention, to know which component is which.**

So, the result is the vector:

```math
\mathbf{A} \times \mathbf{B} =
\begin{bmatrix}
A_y B_z - A_z B_y \\
A_z B_x - A_x B_z \\
A_x B_y - A_y B_x
\end{bmatrix}
```

---

## 4. Volume of Parallelepiped

- Volume of parallelepiped formed by $A$ , $B$ and $C$(where $A$ , $B$ and $C$ are 3d vectors) :

   - $C \cdot (A \times B) = (A_yB_z - A_zB_y)C_x + (A_zB_x - A_xB_z)C_y + (A_xB_y - A_yB_x)C_z$

     - ***This formula is expansion of scalar triple product $C⋅(A×B)$.*** 
- It gives us the signed volume of parallelepiped.
   - "Signed" means that the scalar triple product $C \cdot (A \times B)$ can be positive or negative depending on the orientation of the vectors. The sign tells us about the handedness (orientation) of the coordinate system formed by $A$, $B$ and $C$.
       - Positive sign: Indicates a right-handed orientation.
       - Negative sign: Indicates a left-handed orientation.
  
- When you're interested in the actual volume of the parallelepiped, you take the absolute value of the scalar triple product:
  - Volume = $|C \cdot (A \times B)|$
     - Basically this ensures the volume is always a non-negative quantity, regardless of the sign produced by the scalar triple product.
- [Visualization of scalar triple product](https://youtu.be/BaM7OCEm3G0?si=6c2XIs-eDcbOik7S&t=615)
- [This is the same thing taking dot product between $\begin{bmatrix} x \\ y \\ z \end{bmatrix}$ and the vector that is perpendicular to $A$ and $B$ with the same length equal to the area of parallelogram formed by $A$ and $B$](https://youtu.be/BaM7OCEm3G0?si=oo4LtaGxrwKhmcmQ&t=653)
---
## Properties of Cross Product
- The **2D cross product** gives a **scalar** (signed area of the parallelogram formed by the vectors).
- The **3D cross product** gives a **vector** that is **perpendicular** to both original vectors (right-hand rule).
- If two vectors are **parallel**, their cross product is **zero**.
- The magnitude of the 3D cross product is:

  |A x B| = |A| |B| sin(theta)
  
  where theta is the angle between the vectors, and |A| and |B| are the magnitudes of the vectors.

- The absolute value of the cross product represents the **parallelogram's area** formed by the two vectors.

[2(v) X W  = 2(v X w)](https://youtu.be/eu6i7WJeinw?si=AdToCGzU2PK6KFen&t=277)

[v×w is bigger when the vectors are more perpendicular to eachother and smaller when the vectors are pointing in a similar direction.](https://www.3blue1brown.com/lessons/cross-products#properties)

[Cross Product of 3d vectors , the true cross product combines two different 3d vectors to give a new 3d vector](https://youtu.be/eu6i7WJeinw?si=OB0oKRFyU94hAnMS&t=295)
The 3d cross product does not return a number, it returns a vector. That new vector's length will be the area of that parallelogram

[Formula of computing cross product](https://www.3blue1brown.com/lessons/cross-products#computing)

[The idea of Duality](https://youtu.be/BaM7OCEm3G0?si=aijBh9QAiR6epKFJ&t=125)