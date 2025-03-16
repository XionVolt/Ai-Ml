[See this video](https://youtu.be/TgKwz5Ikpc8?si=Yzf80x830omU_Fpp) or [Read this document](https://www.3blue1brown.com/lessons/abstract-vector-spaces) , by **3Blue1Brown** to understand abstract vector spaces

## Its too basic that -

A vector space is a set of vectors that satisfy certain rules under addition and scalar multiplication.

[Go to Functions](https://youtu.be/TgKwz5Ikpc8?si=wLjUzToGV4d4VbZc&t=127)

```math
(f+g)(x) = f(x) + g(x)
```

**_States that, value of the summed function on any given input `x` is the sum of the values of the individual functions ,`f of x + g of x`_**

[Scaling a function](https://youtu.be/TgKwz5Ikpc8?si=Y9R7dSvRoCkqHzMr&t=191)

```math
(2f)(x) = 2f(x)
```

Basically scale that function output by that scalar.
Again, this is analogous to scaling a vector coordinate by coordinate

Its like we should be able to take same useful constructs and problem solving techniques of linear algebra that were originally thought about in the context of arrows in space(**_vectors_**) and apply them to function as well

[Linear transformation for functions](https://youtu.be/TgKwz5Ikpc8?si=NaWkN9dX856xd9tQ&t=229)

- Basically that take some function and turns it to another . Example derivative in calculus, which transforms one function into anonther function

- Linear operators is the same thing, pointing to linear transformation of functions

[What does it mean for a transformation of functions to be linear](https://youtu.be/TgKwz5Ikpc8?si=pXEGfbCBwSqtWdcu&t=260)

[A transformation is linear if it satisfies two properties](https://youtu.be/TgKwz5Ikpc8?si=WJWoBkTVdOtGR-I6&t=280)

- [Additivity](https://youtu.be/TgKwz5Ikpc8?si=XqYpnRZaIUg-nYDD&t=288)
- [Scaling](https://youtu.be/TgKwz5Ikpc8?si=rwQvlV4mWtnS2YGj&t=305)

- Example derivative is linear because of this reason:

```math
L(v+w) = L(v) + L(w)
```

```math
\frac{d}{dx}(x^3+x^2) = \frac{d}{dx}(x^3) + \frac{d}{dx}(x^2)
```

**_What this equation saying is that, if you add two functions, then take a derivative of the sum of those functions, its same as first taking the derivative of each one separately and then adding the result._**

Similiary is for scale:

```math
\frac{d}{dx}(2x) = 2 \frac{d}{dx}(x)
```

**_Saying,if you first scale a function and then take a derivative its same as first taking the derivative and then scaling the result_**

- After seeing above two clips, we can say lienar transformations preserve the operations of vector additon and scalar multiplication

- **_And the idea that the grid lines remains parallel and evenly spaced after transformation is just an illustration what these two properties mean_**

- One of the most important consequences of these properties, which makes matrix vector multiplication possible is that a linear transformations is completely described by where it takes the basis vectors

**_Since any vector can be expressed by scaling and adding the basis vectors in some way, finding the transformed version of a vector comes down to scaling and adding those the transformed versions of the basis vectors in that same way_**

---

[Let's describe the derivative with a matrix](https://youtu.be/TgKwz5Ikpc8?si=IL7eNtbSBidpWOyY&t=411)

- Things to know:
  - Functional spaces have a tendency to be infinitely dimensional
  - Each of the polynomial in our space have finitely many terms, but the full space is going to include polynomials with arbitrarily large degree
- **So The first thing we have to do is to give coordinates to our space which require choosing a basis**

```math
1x^2 + 3x + 5\cdot1
```

- Since Polynomials are already written in the form of sum of scaled powers of variable x,(or any other variable but here x), so its pretty natural to just choose pure powers of x as the basis function

- Basis Function - A basis function is a fundamental function that serves as a building block to represent elements of a function space, similar to how basis vectors form a coordinate system in vector spaces.

<b>Basis function</b>

```math
\begin{bmatrix}
1\\
x\\
x^2\\
x^3\\
x^4\\
x^5\\
\cdot\\
\cdot
\end{bmatrix}
```

b<sub>0</sub>(x) = 1

b<sub>1</sub>(x) = x

b<sub>2</sub>(x) = x<sup>2</sup>

b<sub>3</sub>(x) = x<sup>3</sup>

b<sub>4</sub>(x) = x<sup>4</sup>

b<sub>5</sub>(x) = x<sup>5</sup>

... and so on.

Each b<sub>i</sub>(x) is a function that maps an input <i>x</i> to an output

A linear combination of these functions looks like:

```math
c_0b_0(x)+c_1b_1(x)+c_2b_2(x)+...
```

where c<sub>0</sub>, c<sub>1</sub>, c<sub>2</sub> ,... are scalars(coefficients)

## But Why are these chosen as basis functions?

1. **Linear Independence:** Each function 1, x, x<sup>2</sup>, x<sup>3</sup>, x<sup>4</sup>, x<sup>5</sup> is independent of the others, meaning none of them can be written as a combination of each other.

2. **Span:** Any polynomial can be expressed as a linear combination of these basis functions. For example:

```math
1x^2 + 3x + 5\cdot1
```

Here
c<sub>2</sub> = 1 (coefficient of x<sup>2</sup>)

c<sub>1</sub> = 3 (coefficient of x)

c<sub>0</sub> = 5 (coefficient of x<sup>0</sup>)

This means that every polynomial of degree
𝑛 can be expressed as:

```math
c_0+c_1x+c_2x^2+⋯+c_nx^n
```

where the coefficients c<sub>0</sub>, c<sub>1</sub>, c<sub>2</sub> ,... are scalars

3. **Standard Polynomial Basis:** These functions form the standard basis for the space of polynomials because they align with how polynomials are naturally written.

Thus, the set {x<sup>0</sup>, x<sup>2</sup>, x<sup>3</sup>, x<sup>4</sup>, x<sup>5</sup>} serves as a basis for the vector space of polynomials, meaning any polynomial can be uniquely represented as a sum of scalar multiples of these functions.

- When we treat polynomials as vectors they're going to have infinitely many coordinates, reason: Polynomial can have arbitraily large degree.

1. For example polynomial:

```math
1x^2 + 3x + 5\cdot1
```

would describe with coordinates

```math
\begin{bmatrix}
5\\
3\\
1\\
0\\
0\\
\cdot\\
\cdot
\end{bmatrix}
```

You'd read this as saying that it's 5 times first basis function + 3 times second basis function + 1 times third basis function and none of the other basis functions should be added from that point on...

2. Second example:
   The polynomial with

```math
4x^7 - 5x^2
```

described as :

```math
\begin{bmatrix}
0\\
0\\
-5\\
0\\
0\\
0\\
4\\
\cdot\\
\cdot
\end{bmatrix}
```

In general, since every individual polynomial has only finite many terms, so its corrdinates will be some finite number of string of numbers with an infinite set tail of zeroes.

For example

```math
a_nx^n + a_{n-1}x^{n-1} + \cdot\cdot\cdot + a_1x + a_0 =
\begin{bmatrix}
a_0\\
a_1\\
\cdot\\
\cdot\\
\cdot\\
a_{n-1}\\
a_n\\
0\\

\cdot\\
\cdot\\
\cdot
\end{bmatrix}
```

---

- [Describing derivative in coordinate system to compute derivative of each basis function](https://youtu.be/TgKwz5Ikpc8?si=3viGVf-gMdE_RvFc&t=547)

- [Construct a matrix(for represent derivative) by taking the derivative of each basis function](https://youtu.be/TgKwz5Ikpc8?si=PPUrW7I0TDJ23HlU&t=633)

----
<table>
<tr>
<th>Linear algebra concepts </th>
<th>Alternate names when applied to functions</th>
</tr>
<tr>
    <td>Linear transformations</td>
    <td>Linear Operators</td>
  </tr>
  <tr>
    <td>Dot products</td>
    <td>Inner Products</td>
  </tr>
  <tr>
    <td>Eigenvectors</td>
    <td>Eigenfunctions</td>
  </tr>
  <tr>
    <td>Matrix-vector multiplication</td>
    <td>Function composition</td>

</table>

- [Vector spaces by 3blue1brown](https://youtu.be/TgKwz5Ikpc8?si=3F1VsfotwD1RfuXn&t=731)

- [All axioms of vector spaces](https://youtu.be/TgKwz5Ikpc8?si=3F1VsfotwD1RfuXn&t=731)