***Hyperplane*** is a flat surface that is one dimension lower than the space it's in.
[See this clip how first line comes for 2d, then we say we assume plane as line in 3d and then for n dimensions we say this line a hyperplane](https://youtu.be/3qzWeokRYTA?si=X0n-36ckwz8mfp_9&t=109)


[See this](https://youtu.be/FqznGyvfiIM?si=8t_AI78mAsmQQZvE)

$y = mx + b$

***In this particular equation: `b` is intercept(means when `x` is zero where line cuts `y` axis, `m` is the slope, `x` and `y` are representing $Δ x , Δy$)***


[How this eqaution $ax+by+c=0$ is same as $y=mx+b$](https://youtu.be/FqznGyvfiIM?si=6NCwpdqbBsJmOYct&t=145)

-----
- We can write this equation as this also: 
Start with the slope-intercept form  

```math
y = mx + c
```
Rearrange it to move all terms to one side:

```math
mx - y + c = 0
```

This matches the genral form 

where: 
$A = m$,
$B = -1$,
$C = c$

**$ax+by+c=0$** 

can also be written as:
```math
w_1 x_1 + w_2 x_2 + w_3 = 0
```

(where **w3** is ***c***, **w1** is ***a***, **w2** is ***b*** and **x1** is ***x*** and **x2** is ***y***) This is equation of ***hyperplane***

$w^T \cdot x + b = 0$

We can write this because here we can dot product of vector ***w*** with vector ***x***.

```math
w^T   =\begin{bmatrix}
w_1\\
w_2\\
w_3
\end{bmatrix}
\cdot
x = \begin{bmatrix}
x_1\\
x_2\\
x_1
\end{bmatrix}
```

#### For n-dimension plane
```math
w_1 x_1 + w_2 x_2 + w_3 x_3 + ... + w_n x_n + b = 0
```
The vector w($\begin{bmatrix} w_1 & w_2 & w_3 & ... & w_n \end{bmatrix}$) is also called ***weight vector*** is perpendicular (normal) to the plane.


- If line passes through origin, we can write this as:
```math
w^T \cdot x + b = 0
```
***$w^T$ is a standard convention linear algebra is to treat weight vectors as column vectors***


```math 
w_1x_1 + w_2x_2 + b = 0
```

Because here both b and x is 0
We can write this as:
```math
w^T \cdot x = 0
```
***So when we write this equation we can say our line passes through origin***
***[And we already know that cosine becomes 0(cos90) also, see its geometrical intuition](https://youtu.be/FqznGyvfiIM?si=2NBERlDTMcFR4Kyk&t=727) you will also find how w vector is perpendicular to the plane***


$w.x = w^T.x = \lvert{w}\rvert \cdot \lvert{x}\rvert \cdot \cos\theta 
 = 0$


-----
$$
\begin{cases}
    y = mx + b \\
    x = \frac{y - b}{m} \\
    m = \frac{\Delta y}{\Delta x}
\end{cases}
$$

----
It also worth to note: In higher dimension b is also called ***offset or bias*** that because in high dimensions it represent ***how far the hyperplane is shifted away from the origin. It determines the position of the hyperplane in space***
