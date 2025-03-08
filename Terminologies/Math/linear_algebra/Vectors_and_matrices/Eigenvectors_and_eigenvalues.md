[Read this documentation by 3blue1brown to know about eigenvalues and eigenvectors](https://www.3blue1brown.com/lessons/eigenvalues)

[Video for visualization](https://youtu.be/PFDu9oVAE-g?si=SbFauUrbJ7Fm3_YJ)

[Most of the vectors are going to get knocked off their span during the transformation , see this clip](https://youtu.be/PFDu9oVAE-g?si=nfvM19IPh24fcWnl&t=87)

[But some vectors do remain on their own span , even after the transformation](https://youtu.be/PFDu9oVAE-g?si=QoGpZc_69YWJPA-r&t=117)

[And if some vector remains on its own same span (assume that vector is `v`), then also other vectors on that line (in which that `v` vector located) will also remain on their own span , and all those vectors stretch or squish by same factor as the `v` vector stretch or squish](https://youtu.be/PFDu9oVAE-g?si=yrwO1egbu7O9w4pa&t=146)

[EignenVector and EigenValue : Basically EigenVectors are all those special vectors that we talk about above , that remain on the same span (that they were before) even after the some transformation, and EigenValues are the factors by which those vectors stretch or squish, so we can say each EigenVector has a corresponding EigenValue](https://youtu.be/PFDu9oVAE-g?si=qkoUJJ6lMFRB3pUc&t=202)

[Geometrically why this is a useful thing to think about](https://youtu.be/PFDu9oVAE-g?si=uhIhj1ohZPoJU_Pj&t=245)

[So , How to compute EigenVectors and their EigenValues](https://youtu.be/PFDu9oVAE-g?si=4bO_ZG06uGMYu2O2&t=327)
- EigneVector formula : `A` `v` = `lambda` * `v`
  - then `A` `v` - `lambda` * `v` = `0` 
  - then = `(A - lambda * I) * v` 
  - then =  `(A - lambda * I) * v` = `0` ((where `A` is transformation matrix, `v` is Eigenvector, `lambda` is a number a corresponding EigenValue, and `I` is identity matrix))

[What this expression is saying : Matrix vector product gives the same result as just scaling Eigenvector by EigenValue(lambda) ](https://youtu.be/PFDu9oVAE-g?si=6fec1rmytwBbUhIk&t=339)

- So finding a EigenVectors and their EigenValues of matrix A comes down to finding the value of `v` and `lambda` that make this expression equal to zero as we seen above

   - [Again From here it comes](https://youtu.be/PFDu9oVAE-g?si=2lWFCpOi_1HGgHFU&t=360)
- Something Intresting : After multiplying lambda by `I` , our `I` becomes a scalar matrix (a matrix whose all diagonal elements are equal and non-diagonal elements are zero) so its a great intution to think where this name (`scalar`) comes from , because its just scaling a vector `v` same like a lambda was doing. 

[Find EigenVector and EigenValue geometically](https://youtu.be/PFDu9oVAE-g?si=jcgUU2zWEnJAYqST&t=422)
After seeing above clip , we get final formula  : `det(A - lambda * I) = 0` 
So from start our formula comes like this : 
1. `A` `v` = `lambda` * `v`
2. `A` `v` - `lambda` * `I` * `v` = `0`
3. (`A` - `lambda` * `I`) * `v` = `0` (By taking `v` a common)
4. det(`A` - `lambda` * `I`) = `0` (This gives us a system where we can solve for 
λ by setting 
det
(
𝐴
−
𝜆
𝐼
)
=
0


so from the last formula we get EigenValue(lambda) and then we can find EigenVector (v)
#### Now you probably think why only diagonal elements are subtracted from lambda : 

- This is simply because in this last formula we first multiply `lambda` by `I` 
- `I` become scalar matrix(or it may remain identity matrix if `lambda` is a one) and we know all its elements are equal **but its non-diagonal elements are zero** 
- So actually we are just subtracting two matrixes `A` - `I` , so its obvious that only diagonal elements subtraction makes sense because all the non diagonal elements are zero so subtraction them makes no sense

That `I` matrix is like this after scale or squish by lambda(assume its in 2d ) :
```
| 𝜆  0 | 
| 0  𝜆 |
```
And we are just subtracting (`A`(some transformation matrix) - `I`) like this :
```
| a b | -  | 𝜆  0 |  =  | a - 𝜆   b |
| c d |    | 0  𝜆 |     | c   d - 𝜆 |
```
- So as you can see above that's why we just subtract only diagonal elements of transformation matrix `A` , because in real its `A` - `I` is happening .
- Now By doing this we get some Quadratic polynomial - 
```
ad-bc = 0
= (a-λ)(d-λ) - bc = 0 
```
After solving this equation we get EigenValue(lambda) , and its easy peasy after to find EigenVector(v) using that EigenValue(lambda)


And Note : 
- Lambda is EigenValue only if determinant of a matrix happens to be 0
- The fact that polynomial doesn't have real roots means there are no EigenVectors of that matrix

[See this example so things become clear](https://youtu.be/PFDu9oVAE-g?si=xCtt1tyCbLkfMwxv&t=570)
[Basically this is how you can get EigenValue by Quadratic Equation](https://youtu.be/PFDu9oVAE-g?si=yegSc9k489hqzk4w&t=592)

[What if transformation doesn't have eigenVectors](https://youtu.be/PFDu9oVAE-g?si=1cxAd5DF_uTQtdQg&t=647)

[A single eigenValue can have more that a line full of eigenVectors](https://youtu.be/PFDu9oVAE-g?si=rf3lx1oE0F4EM9I_&t=745)

[EigenBasis](https://youtu.be/PFDu9oVAE-g?si=49vxVa30HKtXV5p_&t=782)

Any time a matrix has zeros everywhere other than the diagonal, it's called a "diagonal matrix", and the way to interpret it is that all the basis vectors are eigenvectors, and the diagonal entries of the matrix give you their corresponding eigenvalues.
Example of such matrix:
```
|  7   0   0   0  |
|  0   5   0   0  |
|  0   0   5   0  |
|  0   0   0   7  |

```

There are a number of things that make diagonal matrices nicer to work with. One big one is that it's easier to compute what will happen if you multiply this matrix by itself a whole bunch of times.
[Example](https://youtu.be/PFDu9oVAE-g?si=xeBJz9Q679mtrylK&t=837)

[How to describe same transformation but in different coordinate system which have EigenVectors have its columns (basis vectors)](https://youtu.be/PFDu9oVAE-g?si=2dFi2OtfmBCvO7H3&t=899)

[But What's the motive of doing this (first choose the different basis for your coordinate system  ,then make the matrix whose columns are those EigenVectors, then describe the transformation in terms of that matrix(coordinate system))](https://youtu.be/PFDu9oVAE-g?si=dNtVw9BSRGfzdYE4&t=940)
- The whole point of doing this with EigenVectors is that this new matrix is guaranteed to to be diagonal matrix with its cooresponding eigenValues on the diagonal.This is because it represents working in a coordinate system where what happens to basis vectors is that they get scaled during the transformation . 
***''*** **A set of basis vecotrs which are eigenVectors is called, EigenBasis** ***''***
[Example of its use case](https://youtu.be/PFDu9oVAE-g?si=CPvhTa7SWQtb81nk&t=964)

[But Note: You can't do this with all transformations: A shear for example doesn't have enough eigenVectors to span the full space](https://youtu.be/PFDu9oVAE-g?si=Wq9CIybH3P4Ssirz&t=976)