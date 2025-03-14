[See this video](https://youtu.be/uQhTuRlWMxw?si=qAQeSHNvwqsnerpQ) 
**or** [Read this docs](https://www.3blue1brown.com/lessons/inverse-matrices)  , by **3Blue1Brown** to understand determinant .

- So we know till now linear algebra is useful for describing the manipulation of space, which is useful for things like computer graphics and robotics.
- Its also useful for solving system of linear equations 
[Read this part from docs](https://www.3blue1brown.com/lessons/inverse-matrices#linear-systems-of-equations)

So now let's learn about something we call ***inverse*** of a matrix . By understanding inverse 

[Here is a first glimpse of inverse](https://youtu.be/uQhTuRlWMxw?si=vguZqrvQlOHxPjZB&t=234)

[This is why A<sup>-1</sup>.  A = I](https://youtu.be/uQhTuRlWMxw?si=VlYnYxfwvfqigHfb&t=284) , where ***A*** is any transformed matrix and ***A<sup>-1</sup>***  is inverse of that transformation represented by that transformed matrix ***A*** . And ***I*** is Identity matrix . 

## Now let's look at one exmample : 
Suppose we have 2 linear equations :
1. ```2x+5y=-3```
2. ```4x+0y=0```
- Now you can package all the equations together into one vector equation where you have the matrix containing all the constant coefficients, and a vector containing all the variables, and their matrix-vector product equals some different, constant vector.
```
            Coefficient matrix  |    Variables    =  Constant vector
2x+5y=-3        | 2 5 |               | x |          | -3 |
4x+0y=0   ->    | 4 0 |               | y |          |  0 |
                    A                   b      =        v
```
We get equation ```Ab = v```

Now this equation is saying , we have Some transformation ***A*** (matrix) but we don't know input vector(means ***b*** version before transformation applied to ***b***) ***b*** (vector) , but we are given a ***L(b)***(transformed ***b***) that is ***v*** (vector) here . 
Its nostalgic because we solve this type of problem before also . 

So after this we can further solve equation => 

***b = A <sup>-1</sup> * v***
And what this is means geometrically that you playing the transformation A in reverse (transformation in reverse has a special name ***inverse***) and then following ***v*** , and in this way ***v*** will ultimately comes in its untransformed form ( means in initial form ,***v*** before transformed) state (***b***) .

- Note : The system has unique solution in only case , when determinant of the matrix is not 0 , means space not squished to a lower dimension .

So in this way we can solve solve system of 2 equations with just vectors and matrix , without using elimination or substitution !

[See this to understand why inverse of a matrix is not possible if determinant of the matrix is 0](https://youtu.be/uQhTuRlWMxw?si=RZ4a8Gz6d_bAWQ76&t=403)

[Understand what is rank](https://youtu.be/uQhTuRlWMxw?si=9rzt-mtjb-LemMQU&t=481)
- Rank simply means : Number of dimensions in the output of a transformation
- The rank of the matrix tells us how many dimensions remain after transformation:
- For example : When the output of a transformation is a line, means its 1 dimensional, we say transformation has a rank of one . One more example : If all vectors land on some 2d plane, we say transformation has a rank of 2 .
**For example for 2D transformation**
   - Rank 2 (full rank) → No collapse (matrix is invertible).
   - Rank 1 → Collapse to a line.
   - Rank 0 → Collapse to a point (zero vector).

-  Full Rank Matrix : Matrix that has full maximum rank (i.e. its rank is equal to the number of columns) 
- For a full rank transformation, the only vector that land at origin is the zero vector itself. [But for matrices that aren't full rank, which squish to a lower dimension,the null space(the vector that land at origin) are some other vectors too along with zero vector](https://youtu.be/uQhTuRlWMxw?si=27DDhIKkz9ilD17W&t=595)

[Understand what is Column Space (Also Called the Image or Range of a Matrix) and null (or kernel) space](https://youtu.be/uQhTuRlWMxw?si=d733RKL5h2EJ91TI&t=532)
- The span of column vectors of the matrix is called column space of that matrix.
- The set of all possible outputs for any matrix (when transformed) , whether its a line , a plane , 3D space or whatever , is called a column space of that matrix  . 
- The set of all vectors that becomes null (after the transformation) in the sense they land at 0 vector is called null space(or kernel) of your matrix . 
    - In terms of linear system of equations , when v (constant vector) happens to be zero vector , the null space gives you all of the possible solutions(means all possible values of variables vector) to the equation .


Note : Rank, Null Space, and Linear Systems are deeply explained in another markdown file . What is trivial and non-trivial also explained below there . 