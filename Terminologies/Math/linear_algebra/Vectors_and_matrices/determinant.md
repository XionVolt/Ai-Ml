[See this video](https://youtu.be/Ip3X9LOh2dk?si=z14WuRVtXWjANGRt) 
**or** [Read this docs](https://www.3blue1brown.com/lessons/determinant)  , by **3Blue1Brown** to understand determinant .

## What's the determinant?
The factor by which linear transformation changes any area (of the grid squares) is called the ***determinant*** of the transformation .  [For Example](https://youtu.be/Ip3X9LOh2dk?si=T_rc0yz8YPh40k81&t=169)

## What if determinant = 0 ?
It means that the linear transformation squishes the area by 0 , if its then the transformation associated with that matrix squishes everything into smaller dimension . 

Note : If two column vectors in a 2×2 matrix are collinear, they lie along the same line, meaning they span only 1D space instead of 2D.
In that case also determinant is 0 .  Means transformation squishes everything into lower dimension (1D space here) .
Since one dimension is lost, every transformed vector gets squashed onto a single line (1D instead of 2D).
- Bascially what we wanna say above,If a transformation matrix has linearly dependent columns, its determinant is zero.

And this thing apply to any dimension . If you not understand this at once try to Visualize it . 


## Invert orientation of space ?
[See this video clip to understand](https://youtu.be/Ip3X9LOh2dk?si=_W2_ZuLslYlHyBng&t=230)

## See why , determinant of 2d matrix is ad - bc ?
[See this video clip to understand](https://youtu.be/Ip3X9LOh2dk?si=7epBZxUNjo9eTcrT&t=456)

## Determinant Important property
`det(M1M2) = det(M1) * det(M2)` , where M1 and M2 are matrices

This saying : **If you multiply two matrices together, the determinant of the resulting matrix is the same as the product of the determinants of the original two matrices.**

- In python we have ***numpy.linalg.det(Matrix)*** to find determinant of matrix.


