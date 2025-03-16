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

----------
**We also have second formula of finding dot product, ∣a∣∣b∣cosθ** 

- **∣a∣** is the magnitude (length) of vector a,
- **∣b∣** is the magnitude of vector b,
- **θ** is the angle between the two vectors.

This formula is useful when dealing with angles between vectors or when working in physics and geometry.


a = (3,4)
b = (5,12)

Step 1: Find the magnitudes of a and b

The magnitude of a vector 
(
𝑥
,
𝑦
)
(x,y) is:

```math
∣a∣ =  \sqrt{3^2+4^2} = \sqrt{9+16} = \sqrt{25} = 5    
```

```math
∣b∣ =  \sqrt{5^2+12^2} = \sqrt{25+144} = \sqrt{169} = 13
```
Step 2: Find the dot product using the first formula

```math
a.b = 3\times5 + 4\times12 = 15 + 48 = 63
```

Step 3: Find the angle between the two vectors using the second formula

```math
cosθ = \frac{a.b}{∣a∣∣b∣} = \frac{63}{5\times13} = \frac{63}{65}
```

Step 4: Solve for θ

```math
θ = \cos^{-1}\left(\frac{63}{65}\right)
```

Approximating
```math
θ \approx cos^{-1}(0.9692) \approx 14.48°
```


This formula is useful when dealing with angles between vectors or when working in physics and geometry.
