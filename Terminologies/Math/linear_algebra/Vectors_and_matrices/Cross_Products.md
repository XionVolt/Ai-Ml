[Documentation by 3blue1brown](https://www.3blue1brown.com/lessons/cross-products)

[See video for visualization by 3blue1brown](https://www.youtube.com/watch?v=8O7yCjF4XU0)

[How to take dot product(geometrically)](https://youtu.be/eu6i7WJeinw?si=q-K6RNPXXwFZvzzl&t=40)



In cross Product(also called the perpendicular or wedge product) order of Vectors(how they multiplying) change signs .
Example: 

$$
\overrightarrow{a} \times \overrightarrow{b} = - \overrightarrow{b} \times \overrightarrow{a}
$$
***If `a` is on right side then dot product is postive else negative , `a` and `b` can be any vecotor*** 

[Remember ordering like when dot product is postive and when negative](https://youtu.be/eu6i7WJeinw?si=sPK3c7f-JxthAP-E&t=99)

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

### How to Find the Area of a Parallelogram
For two vectors A and B, the area of the parallelogram they form is given by:

Area = |A x B|

For 2D vectors:

Area = |Ax * By - Ay * Bx|

For 3D vectors:

Area = sqrt((Ay * Bz - Az * By)^2 + (Ax * Bz - Az * Bx)^2 + (Ax * By - Ay * Bx)^2)

This formula comes from the fact that the cross product gives a vector perpendicular to A and B, whose magnitude represents the parallelogram's area.

---

## Properties of Cross Product
- The **2D cross product** gives a **scalar** (signed area of the parallelogram formed by the vectors).
- The **3D cross product** gives a **vector** that is **perpendicular** to both original vectors (right-hand rule).
- If two vectors are **parallel**, their cross product is **zero**.
- The magnitude of the 3D cross product is:

  |A x B| = |A| |B| sin(theta)
  
  where theta is the angle between the vectors.

- The absolute value of the cross product represents the **parallelogram's area** formed by the two vectors.


