---
marp: true
theme: default
paginate: true
size: 16:9
fontsize: 16px
---

# Polynomial Ring


Let $R$ be a commutative ring with unity. The **polynomial ring** $R[x]$ is the set of all expressions of the form:

$$
f(x) = a_0 + a_1 x + a_2 x^2 + \cdots + a_n x^n
$$

where $a_i \in R$ for all $i$, and $n \geq 0$. 

- The **degree** of a nonzero polynomial is the highest power of $x$ with a nonzero coefficient.

- $R[x]$ is an $R$-algebra.
- $R[x]$ is also a commutative ring.


---

## Sum and Multiplication in $R[x]$


$$
f(x) = a_0 + a_1 x + a_2 x^2 + \cdots + a_m x^m
$$
$$
g(x) = b_0 + b_1 x + b_2 x^2 + \cdots + b_n x^n
$$
where $a_i, b_j \in R$.

### Sum of Polynomials

The **sum** $f(x) + g(x)$ is:  

$$
f(x) + g(x) = (a_0 + b_0) + (a_1 + b_1)x + (a_2 + b_2)x^2 + \cdots
$$

If the degrees of $f(x)$ and $g(x)$ differ, we may assume that the coefficients of the missing terms are zero.

---

### Product of Polynomials

The **product** $f(x) \cdot g(x)$ is defined by convolution of coefficients:

$$
f(x) \cdot g(x) = c_0 + c_1 x + c_2 x^2 + \cdots + c_{m+n} x^{m+n}
$$

where for each $k$, the coefficient $c_k$ is given by:

$$
c_k = \sum_{i+j=k} a_i b_j
$$


---

## Example

- $\mathbb{Z}[x]$: Polynomials with integer coefficients.
- $\mathbb{C}[x]$: Polynomials with rational coefficients.

Not that standard example:
- $\mathbb{Z}_4[x]$: Polynomials with coefficients in $\mathbb{Z}_4$.

$(\bar{2}x) (\bar{2}x^2 +\bar{1}) = \bar{2}x$. 

---
# Zero Function $\neq$ Zero Polynomial in general

## Example 

$p$ is a prime. Consider $x^p - x \in \mathbb{Z}_p[x]$

**Note:** $\mathbb{Z}_p$ has finitely many elements. $R \ni 1_R$

**Polynomial evaluation map:**
$$
\begin{aligned}
\text{eval} : R[x] &\to \text{Fun}(R) \\
f = \sum c_i x^i &\mapsto \left(a \mapsto f(a) :=\sum c_i a^i\right)
\end{aligned}
$$

---

## Fermat's Little Theorem

$\forall a \in \mathbb{Z}_p$

$$a^p = a \text{ in } \mathbb{Z}_p$$

(Fermat's little theorem)

$\Rightarrow a^p - a = 0$

---

## Observation

$$x^p - x \neq 0 \text{ in } \mathbb{Z}_p[x]$$

**But** as a function on $\mathbb{Z}_p$, it is the **zero function**.

This shows that the polynomial evaluation map $R[x] \to \text{Fun}(R)$ is not always injective when $R$ is finite.

---
# Division Algorithm for Polynomials

**Theorem:** Let $R$ be a commutative ring with unity, and let $f(x), g(x) \in R[x]$ with $g(x) \neq 0$. Suppose the leading coefficient of $g(x)$ is a unit in $R$. Then there exist unique polynomials $q(x), r(x) \in R[x]$ such that:

$$
f(x) = g(x)q(x) + r(x)
$$

where either $r(x) = 0$ or $\deg(r) < \deg(g)$.

This is known as the **Division Algorithm for Polynomials**.

---

# Integral Domain

A commutative ring with unity $R$ is called an **integral domain** if it satisfies the following conditions:
1. $R$ is commutative (i.e., $ab = ba$ for all $a, b \in R$)
2. $R$ has no zero divisors (i.e., for any $a, b \in R$, if $ab = 0_R$, then either $a = 0_R$ or $b = 0_R$)

---

## Factor Theorem

**Theorem:** Let $f(x) \in R[x]$, where $R$ is an integral domain. Then $a \in R$ is a zero of $f(x)$ if and only if $(x - a)$ divides $f(x)$, i.e., there exists $g(x) \in R[x]$ such that:

$$
f(x) = (x - a)g(x)
$$

<details>
<summary><strong>Proof</strong></summary>

**(⇒)** Suppose $ f(a) = 0 $. By the division algorithm for polynomials, since $ R $ is a commutative ring with unity, we can write:

$$
f(x) = (x - a)q(x) + r
$$

where $q(x), r \in R[x]$ and $r$ is a constant (degree of remainder < degree of divisor).

Now evaluate at $ x = a $:

$$
f(a) = (a - a)q(a) + r = 0 \cdot q(a) + r = r
$$

$f(a) = 0$, it follows that $r = 0$

</details>

--- 
## Corollary

Let $R$ be an integral domain.
Nonzero polynomials $f(x) \in R[x]$ have at most $\deg(f)$ roots in $R$.

## The condition of being an integral domain is necessary.

---
# Ring of Dual Numbers

Let $R$ be a commutative ring with unity. The **ring of dual numbers** over $R$, denoted by $R[\epsilon]$, is the quotient ring:

$$
R[\epsilon] = R[x] / (x^2)
$$

Informally, this means that we introduce a new element $ \epsilon $ such that:

$$
\epsilon^2 = 0
$$

Every element in $R[\epsilon]$ can be written uniquely as:

$$
a + b\epsilon \quad \text{where } a, b \in R
$$

---

Addition and multiplication are defined as follows:

- **Addition:**  
  $$
  (a + b\epsilon) + (c + d\epsilon) = (a + c) + (b + d)\epsilon
  $$

- **Multiplication:**  
  $$
  (a + b\epsilon)(c + d\epsilon) = ac + (ad + bc)\epsilon + bd\epsilon^2 = ac + (ad + bc)\epsilon
  $$
  since $\epsilon^2 = 0$

This ring is useful in algebraic geometry and automatic differentiation because it allows us to keep track of first-order derivatives.

---
Now let $R = \mathbb{C}[\epsilon]$.

Consider the polynomial $f(x) = x^2 \in R[x]$.
Then $f(x)$ has infinitely many roots in $R$.

Indeed, for any $z \in \mathbb{C}$, $f(z\epsilon) = (z\epsilon)^2 = z^2\epsilon^2 = 0$.

---
## Corollary
Let $R$ be an integral domain.
If $R$ has infinitely many elements, then 
$f(x) \in R[x]$ is a zero polynomial if and only if $f(x) = 0$ for all $x \in R$.


---

# Formal power series ring

Let $R$ be a commutative ring with unity. The **formal power series ring** over $R$, denoted by $R[[x]]$, is the set of all infinite series of the form:

$$
f(x) = \sum_{i=0}^{\infty} a_i x^i = a_0 + a_1 x + a_2 x^2 + \cdots
$$

where each coefficient $a_i \in R$.

- Addition and multiplication in $R[[x]]$ are defined as for polynomials, but extended to allow infinitely many nonzero terms.

- The **order** of a nonzero formal power series $f(x) = \sum_{i=0}^{\infty} a_i x^i$, denoted $\operatorname{ord}(f)$, is the smallest integer $n \geq 0$ such that $a_n \neq 0$.

---

# Analytic functions over $\mathbb{C}$ 

A complex function is differentiable if it has a formal power series expansion. This means that in some neighborhood of a point, the function can be expressed as:

$$
f(z) = \sum_{n=0}^{\infty} a_n (z - z_0)^n
$$

where $z_0$ is a point in the complex plane and $a_n \in \mathbb{C}$. Such functions are called **analytic** at $z_0$, and if they are analytic everywhere in the complex plane, they are called **entire** functions.

---

Analytic functions are infinitely differentiable, and their derivatives can be computed term-by-term from their power series:

$$
f'(z) = \sum_{n=1}^{\infty} n a_n (z - z_0)^{n-1}
$$

This property makes them particularly well-behaved and useful in various areas of mathematics and physics.


---

# Units in Formal Power Series Ring

Recall $u$ is called a **unit** in a ring $R$ if there exists $v \in R$ such that $uv = vu = 1_R$.

# Theorem 
 A formal power series $f(x)$ is a **unit** in $R[[x]]$ if and only if its constant term $a_0$ is a unit in $R$.

---

# Laurent Series Ring

Let $R$ be a commutative ring with unity. The **Laurent series ring** over $R$, denoted by $R((x))$, is the set of all series of the form:
$$
f(x) = \sum_{i=k}^{\infty} a_i x^i = \cdots + a_{-2} x^{-2} + a_{-1} x^{-1} + a_0 + a_1 x + a_2 x^2 + \cdots
$$
where $k$ is a integer.

- Addition and multiplication in $R((x))$ are defined as for polynomials, but extended to allow infinitely many nonzero terms.
- The **order** of a nonzero Laurent series $f(x) = \sum_{i=k}^{\infty} a_i x^i$, denoted $\operatorname{ord}(f)$, is the smallest integer $n \geq k$ such that $a_n \neq 0$.


---

# Units in Laurent Series  

A Laurent series $f(x)$ is a **unit** in $R((x))$ if and only if its leading coefficient $a_{k}$ is a unit in $R$.



