[Numerical Method of dot Product](https://www.3blue1brown.com/lessons/dot-products#numerical-method)
- Numerically, if you have two vectors of the same dimension, two lists of numbers with the same lengths, taking their dot product means pairing up all the coordinates, multiplying those pairs together, and adding the result.

[Geometric-interpretation](https://youtu.be/LyGKycYT2v0?si=HnuKVmH5HFIBR_ku)

Important points: 
- v.w = w.v (where v and w are vectors)
- v.w>0 when they point in similar directions.
- v.w=0 when they are perpendicular,  meaning the projection of one onto the other is the zero vector.
- v.w<0 when they point in opposite directions.


1x2 matrix . 2d Vector , can also be solved by dot product . Basically here we determining where our 2D vector lands in output space . Which we can find using Vector dot product or our traditional matrix vector multiplication .
We can do this : because both have same dimension .
```
a = | 1  2 | 
            
            
v =  | 4 | 
     | 3 |
```
where a is any matrix  representing a linear transformation that takes a 2d vector from the input space and gives a number to the output space .

```
a * v Same as multiplying matrix `a` by a vector `v` by making matrix column vector or make a vector `v` a row vector .
means a * v same as doing this : | 1 | * | 4 |
                                 | 2 |   | 3 |
so in this way also we can find where our 2D vector(v) lands in output space .
``` 