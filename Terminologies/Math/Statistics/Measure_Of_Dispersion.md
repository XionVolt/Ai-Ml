- [What is Dispersion?](https://youtu.be/5_TuK1yCPD4?si=UT3StHZ5PYE73oI6&t=31)
    - **Dispersion measures the extent to which the items vary from some central value(***mean,median or mode***)** 
    -  ***Dispersion is also known as scatter, spread or variation***
----

- [Why we need dispersion](https://youtu.be/5_TuK1yCPD4?si=nHCd5YKZCtYpPh_s&t=257)

***A good dispersion is a low dispersion***

----

[Measures of Dispersion](https://youtu.be/5_TuK1yCPD4?si=Fj8ie8NyXkBRe9yE&t=522)

<table>
<tr>
<th>Absolute Measure(Unit same)</th>
<th>Relative Measure(Unit free)</th>
</tr>

<tr>
<td>Range</td>
<td>Coefficient of Range</td>
</tr>

<tr>
<td>Quartile Range</td>
<td>Coefficient of quartile Range</td>
</tr>

<tr>
<td>Mean Deviation</td>
<td>Coefficient of Mean Deviation</td>
</tr>

<tr>
<td>Standard Deviation</td>
<td>Coefficient of Standard Deviation</td>
</tr>

<tr>
<td>Variance</td>
<td>Coefficient of Variance</td>
</tr>
</table>


----

- [Variance and Standard deviation](https://youtu.be/l_YszNIJfFA?si=yQQrsCVxfsoQkUd-&t=141)
    - [What is Variance?](https://youtu.be/x0rmUXWtSS8?si=PnAb-Als9r3FJNme)
        ***Variance is the average of the squared differences from the mean***
         - Population Variance
        ```math
            \sigma^2 = \frac{1}{N} \sum_{i=1}^{n} (x_i - \mu)^2 \  \textbf{ (} \mu \textbf{ is the population mean)}
        ```
        - Sample Variance
        ```math
            S^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2 \textbf{ (n-1 also called Bessel's correction or Degree of Freedom)} 
        ```

     - [What is standard deviation](https://youtu.be/x0rmUXWtSS8?si=HfZcP9HjDGDslylt&t=201)
     ***Standard deviation is the square root of the variance***
        - Population Standard Deviation
        ```math
            \sigma = \sqrt{\frac{1}{N} \sum_{i=1}^{n} (x_i - \mu)^2}
        ```

        - Sample Standard Deviation
        ```math
            S = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}
        ```
-  [Plotting of Standard deviation](https://youtu.be/x0rmUXWtSS8?si=SyNdcafNC5Vy9NFf&t=235) 
- [What's the meaning of large and small standard deviation?](https://youtu.be/x0rmUXWtSS8?si=6UKOpPDcE8ylspYZ&t=265)

----

[What **variance** and **Standard deviation** values describe](https://youtu.be/l_YszNIJfFA?si=WEkX8FuRyQSVRxyO&t=827)

If Variance is a big number means spread of the data points is big and, if small means curve(peak) height is high and data points are close to each other.

----

[What is **MAD**(***Mean absolute deviation***?)](https://youtu.be/yCDevFTNbC0?si=Ytw1e_PyDMoyb0A4&t=7)

#### Formula
```math
    MAD = \frac{1}{n} \sum_{i=1}^{n} |x_i - \mu|
```
$\mu$ is the Population mean, $n$ is the number of data points

[But there are cases where MAD is not enough, then we use standard deviation, see](https://youtu.be/yCDevFTNbC0?si=R2Z6e9YseFMUKHPZ&t=217)
*See last column in this video clip($Score-Avg^2$), now you will understand why we say **variance** is a ***Average*** of squared differences from mean*