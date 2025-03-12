[See this video](https://youtu.be/TgKwz5Ikpc8?si=Yzf80x830omU_Fpp) or [Read this document](https://www.3blue1brown.com/lessons/abstract-vector-spaces) , by **3Blue1Brown** to understand abstract vector spaces

## Its too basic that - 
A vector space is a set of vectors that satisfy certain rules under addition and scalar multiplication.

[Go to Functions](https://youtu.be/TgKwz5Ikpc8?si=wLjUzToGV4d4VbZc&t=127)

```math
(f+g)(x) = f(x) + g(x) 
```
***States that, value of the summed function on any given input `x` is the sum of the values of the individual functions ,`f of x + g of x`***

[Scaling a function](https://youtu.be/TgKwz5Ikpc8?si=Y9R7dSvRoCkqHzMr&t=191)

```math
(2f)(x) = 2f(x)
```
Basically scale that function output by that scalar.
Again, this is analogous to scaling a vector coordinate by coordinate

Its like we should be able to take same useful constructs and problem solving techniques of linear algebra that were originally thought about in the context of arrows in space(***vectors***) and apply them to function as well

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
***What this equation saying is that, if you add two functions, then take a derivative of the sum of those functions, its same as first taking the derivative of each one separately and then adding the result.*** 

Similiary is for scale:
```math
\frac{d}{dx}(2x) = 2 \frac{d}{dx}(x)
```
***Saying,if you first scale a function and then take a derivative its same as first taking the derivative and then scaling the result***

- After seeing above two clips, we can say lienar transformations preserve the operations of vector additon and scalar multiplication

- ***And the idea that the grid lines remains parallel and evenly spaced after transformation is just an illustration what these two properties mean*** 

- One of the most important consequences of these properties, which makes matrix vector multiplication possible is that a linear transformations is completely described by where it takes the basis vectors

***Since any vector can be expressed by scaling and adding the basis vectors in some way, finding the transformed version of a vector comes down to scaling and adding those the transformed versions of the basis vectors in that same way***

-----

[Let's describe the derivative with a matrix](https://youtu.be/TgKwz5Ikpc8?si=IL7eNtbSBidpWOyY&t=411)
- Things to know:
     - Functional spaces have a tendency to be infinitely dimensional 
     - Each of the polynomial in our space have finitely many terms, but the full space is going to include polynomials with arbitrarily large degree
- **So The first thing we have to do is to give coordinates to our space which require choosing a basis**

```math
1x^2 + 3x + 5\cdot1
```

- Since Polynomials are already written in the form of sum of scaled powers of variable x,(or any other variable but here x), so its pretty natural to just choose pure powers of x as the basis function
Basis Function
<u>Basis function</u>


