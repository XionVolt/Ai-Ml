# Read this to deep dive into topics of Linear transformations and matrices by `3blue1brown`: 
https://www.3blue1brown.com/lessons/matrix-multiplication

[See the corresponding video that also made by `3blue1brown`](https://youtu.be/XkY2DOUCWMU?si=grsKfZeDuTa46GMS)

Oftentimes, you find yourself wanting to describe the effects of applying one linear transformation, then applying another. For example, maybe you 
want to describe what happens when you rotate the plane **90 degrees , counterclockwise**, then to apply a **shear**. The overall effect here, from 
start to finish, is another linear transformation, distinct from the rotation and the shear. This new linear transformation is commonly called the 
***“composition”*** of the two separate transformations we applied(***composition*** of *rotation* and *shear*).
[Example](https://youtu.be/XkY2DOUCWMU?si=OynN8796dWY5dpzg&t=121)

[It is a short way to find transformation of given vector after applying(multiplying) the n amount of those mutliple linear transformations on that given vector in respective order](https://youtu.be/XkY2DOUCWMU?si=RZQzAEd_ygdwRnRo&t=184)
**Basically multiply composition matrix to input vector you will get transformed vector** 

[Composition matrix is product of n number of transformation matrices](https://youtu.be/XkY2DOUCWMU?si=DEiOkgXNgfNyiebc&t=223)

[You first apply transformation represented by matrix on the right , then apply transformation represented by matrix on the left..., on your grid](https://youtu.be/XkY2DOUCWMU?si=8MjcKX5jMvmuw8IS&t=245)
- Its like a function taking value computed from 
      - And this is only the reason that order we put 2 matrices(or more) when we multiply them , that order matters  [See this visually](https://youtu.be/XkY2DOUCWMU?si=Cl2zS90uuAj4Eopu&t=447)


[This is how you can calculate composition matrix](https://youtu.be/XkY2DOUCWMU?si=kbzRdrB6kwqqVTZp&t=290)
- Basically after seeing this clip we can say matrix multiplication is way to find ultimate position(coordinates) of `i`,`j` ,`k` ..., `n` hat. 
    - And once we calculate our composition matrix we can find any vector final location given to us , that we get after applying n amount of linear transformations on that vector in respective order.

- Composition matrix records the effects of applying n amount of linear transformations to `i`,`j` (basically we can say , apply to plane) in 2D space. And obviously this thing applicable to 3D space and above too . 
So think of Matrix multiplication of applying one transformation then another . 

- **Matrix multiplication is associative** : Means if we have 3 matrices A,B,C and then A * (B * C) = (A * B) * C , as both things saying the one thing first apply C then apply B then apply A . Simple ! Because what it’s saying is that if you first apply (C then B), then A, it’s the same as applying C, (then B then A) . 

- **Matrix Mutiplication is commutative , often** : Means if we have 2 matrices A,B then ***A * B*** not equal to ***B * A*** , but Note:  There are some examples of matrices commuting that are not commuting.
Example :
```
| 0  -1 | * | -2  0 |     =  | -2  0 |   *  | 0  -1 | 
| 1   0 |   | 0  -2 |        | 0  -2 |      | 1   0 |
```

- And scalar matrix multiplication is also commutative , means if we have 2 scalars a,b then a*b = b*a (where a is any matrix, and b is any scalar) .  

- `I * any matrix = any matrix * I = any matrix` , where **I** is the identity matrix.  , so we can say its also commutative . It commutes with every other matrix . 

- Since the identity matrix is always commutative and scalar-matrix multiplicative is always commutative, we know a scaling matrix is always commutative:
***(aI)M=aMI=M(aI)*** (where *a* is scalar and M is any matrix and I is identity matrix)

