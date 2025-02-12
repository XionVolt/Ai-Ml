[Read this docs](https://www.3blue1brown.com/lessons/matrix-multiplication) 
or [watch this video](https://youtu.be/rHLEWRxRGiM?si=_Z4cRBagLngLWiuC) by `3blue1brown` if you wanna see/revise about linear transformations in 3D . 
Basically its same as 2D space but in 3D space `k` hat also comes into play . 
And same reasoning applied for find input matrix in 3D (or higher dimensions) . 
Example now we have 3D space :
```
i = | 1 | 0 | 0 |
j = | 0 | 1 | 0 |
k = | 0 | 0 | 1 |
```
we transformed space so basis vector land somewhere else in 3D space .

And now we have to find the transformation matrix of this transformation . `A` = 
``` 
i = | a | b | c | 
j = | d | e | f |
k = | g | h | i |
``` 

`v` = 
```
| x |
| y |
| z |
```
And now we wanna find some input vector `v` , transformed by this transformation `A` .
```
v' = x * i + y * j + z * k
```
that gives 
```
v' = x * | a | + y * | d | + z * | g | 
         | b |       | e |       | h |
         | c |       | f |       | i |   
```

[Example](https://youtu.be/rHLEWRxRGiM?si=_3KFX259Fs9AfSVe&t=194)

**We know Each of `v` coordinates can be thought of instructions for how to scale each basis vector so when they added together they get your vector**.

Multiply matrix by matrix in 3D(and above dimensions) is also same as we do in 2D . And you can think about matrix multiplication in 3D space in same way as you think in 2D space , *think of each 3D matrix as a certain transformation of in 3D space*. And *think about 3D matrix maltiplication as applying two or n number of transformations one after another on 3D space* .
