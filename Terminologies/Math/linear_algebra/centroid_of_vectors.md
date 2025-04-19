
# 📌 Centroid (Average Vector) of 2D Vectors

## 🔢 1. Centroid of 2 Vectors = Midpoint

If you have two 2D vectors:
- **A** = (x₁, y₁)
- **B** = (x₂, y₂)

Then their **centroid (average vector)** is:
```
((x₁ + x₂)/2, (y₁ + y₂)/2)
```

✅ This is also the **midpoint** between them in 2D space.

### Example:
A = (2, 4), B = (6, 8)

Centroid = ((2 + 6)/2, (4 + 8)/2) = (4, 6)

---

## 🔢 2. Centroid of 3 or More Vectors

If you have **n vectors**:
- A₁ = (x₁, y₁)
- A₂ = (x₂, y₂)
- A₃ = (x₃, y₃)
- ...
- Aₙ = (xₙ, yₙ)

Then their **centroid** is:
```
C = ( (x₁ + x₂ + ... + xₙ)/n , (y₁ + y₂ + ... + yₙ)/n )
```

### Example with 3 Vectors:
- A = (2, 3)
- B = (4, 7)
- C = (6, 1)

```
x_avg = (2 + 4 + 6)/3 = 4  
y_avg = (3 + 7 + 1)/3 ≈ 3.67
```

✅ Centroid = **(4, 3.67)**

---

## 🧠 Geometric & Practical Meaning

- The centroid is the **mean position** of all the points (vectors).
- It is the **balance point** (center of mass if points have equal weight).
- In geometry: geometric center.
- In machine learning: cluster center (e.g., in k-means).
- Works for **any number of dimensions**.

---

## ✅ Summary

| Case         | Centroid Formula                                   |
|--------------|----------------------------------------------------|
| 2 Vectors    | ((x₁ + x₂)/2, (y₁ + y₂)/2)                          |
| n Vectors    | ((Σxᵢ)/n, (Σyᵢ)/n) for i from 1 to n                |