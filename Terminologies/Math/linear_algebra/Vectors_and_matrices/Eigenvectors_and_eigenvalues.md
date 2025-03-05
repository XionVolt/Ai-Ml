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
4. det(`A` - `lambda` * `I`) = `0` 

So from these formulas we get EigenValue(lambda) and then we can find EigenVector (v)

And Note : Lambda is EigenValue only if determinant of a matrix happens to be 0

[See this example so things become clear](https://youtu.be/PFDu9oVAE-g?si=xCtt1tyCbLkfMwxv&t=570)

