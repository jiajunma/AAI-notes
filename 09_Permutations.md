---
marp: true
theme: default
paginate: true 
---

# Cycle Notations of Permutations in $S_n$

---

## Definition of $S_n$

**The Symmetric Group $S_n$:**

$S_n$ is the set of all permutations of the set $\{1, 2, 3, \ldots, n\}$:  

$$S_n = \{\sigma : \{1, 2, \ldots, n\} \to \{1, 2, \ldots, n\} \mid \sigma \text{ is bijective}\}$$

---

## Two-Line Notation

Traditional way to represent permutations:

$$
\sigma = \begin{pmatrix}
1 & 2 & 3 & 4 & 5 \\
3 & 5 & 1 & 4 & 2
\end{pmatrix}
$$

- Top row: original positions
- Bottom row: where each element maps to
- This permutation sends: 1→3, 2→5, 3→1, 4→4, 5→2

---

## Inverse of a Permutation

**In Two-Line Notation:**

If $\sigma = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 3 & 5 & 1 & 4 & 2 \end{pmatrix}$

Then $\sigma^{-1} = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 3 & 5 & 1 & 4 & 2 \end{pmatrix}^{-1} = \begin{pmatrix} 3 & 5 & 1 & 4 & 2 \\ 1 & 2 & 3 & 4 & 5 \end{pmatrix} = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 3 & 5 & 1 & 4 & 2 \end{pmatrix}$

**Problem of Two-line Notation:**
Too much space to write and difficult to invert.

**Solution:**
Cycle notation. 

---


## Orbit of a Permutation


Consider a permutation $\sigma \in S_n$. 
It is acting on a set $X = \{1, 2, \ldots, n\}$.

The **orbit** of an element $x \in \{1, 2, \ldots, n\}$ under $\sigma$ is defined as the orbit of the cyclic group $\langle \sigma \rangle$ acting on $X$:

$$\text{Orb}_\sigma(x) = \{y \in X \mid \exists n \in \mathbb{Z}, y = \sigma^n(x)\}$$

**Equivalence Relation:**

This induces an equivalence relation $\sim_\sigma$ on $X$ defined by:

$$x \sim_\sigma y \iff \exists n \in \mathbb{Z}, y = \sigma^n(x)$$

---
---

## Example: Orbit of a Permutation

Consider the permutation $\sigma \in S_6$ written in 
two-line notation:
$$
\sigma = \begin{pmatrix}
1 & 2 & 3 & 4 & 5 & 6 \\
3 & 4 & 5 & 2 & 1 & 6
\end{pmatrix}
$$

- Apply $\sigma$ repeatedly to 1: $1 → 3 → 5 → 1 → …$
  So, $\text{Orb}_\sigma(1) = \{1, 3, 5\}$.
- Apply $\sigma$ repeatedly to 2: $2 → 4 → 2 → …$
  So, $\text{Orb}_\sigma(2) = \{2, 4\}$.
- Apply $\sigma$ repeatedly to 6: $6 → 6 → …$
  So, $\text{Orb}_\sigma(6) = \{6\}$.

---
## Upshot
These orbits partition $X = \{1,2,3,4,5,6\}$ into disjoint cycles; each cycle in the cycle notation corresponds exactly to one orbit.

---
## Definition: Cycle

A **cycle** in $S_n$ is a permutation that cyclically permutes a subset of $\{1, 2, \ldots, n\}$ while fixing all other elements.

**Formal Definition:**

We write this cycle as $(a_1 \, a_2 \, a_3 \, \cdots \, a_k)$ such that
$$a_{i+1} = \sigma(a_i) \text{ for } i = 1, 2, \ldots, k-1 \text{ and } a_1 = \sigma(a_k).$$

* Length of the cycle: $k$

**Special Cases:**
- A **1-cycle** $(a)$ is the identity on $a$, often omitted in notation
- A **2-cycle** $(a \, b)$ is also called a **transposition**

---

## Example: Cycle from Two-Line Notation


Consider the permutation: 
$$
\sigma = \begin{pmatrix}
1 & 2 & 3 & 4 & 5 \\
3 & 2 & 4 & 1 & 5
\end{pmatrix}
$$

**Tracing the cycles:**
- Start with 1: $1 \to 3 \to 4 \to 1$ (forms a 3-cycle)
- Start with 2: $2 \to 2$ (fixed point, 1-cycle)
- Start with 5: $5 \to 5$ (fixed point, 1-cycle)

**In cycle notation:**
$$\sigma = (1 \, 3 \, 4)$$

---
## Lemma: Disjoint Cycles Commute

- Support of a cycle: the set of elements it permutes. For example, the cycle $(a_1 \, a_2 \, a_3 \, \cdots \, a_k)$ permutes the elements $a_1, a_2, \ldots, a_k$.

Let $\alpha, \beta \in S_n$ be cycles with disjoint supports:
$$\operatorname{supp}(\alpha) \cap \operatorname{supp}(\beta) = \varnothing.$$
Then
$$\alpha \beta = \beta \alpha.$$


---
Let $\alpha, \beta \in S_n$ be cycles with disjoint supports:
$$\operatorname{supp}(\alpha) \cap \operatorname{supp}(\beta) = \varnothing.$$
Then
$$\alpha \beta = \beta \alpha.$$

**Proof:** For any $x \in \{1,\dots,n\}$, consider three cases:
* If $x \in \operatorname{supp}(\alpha)$ and $x \notin \operatorname{supp}(\beta)$, then $\beta(x) = x$, so
  $$\alpha\beta(x) = \alpha(x), \quad \beta\alpha(x) = \beta(\alpha(x)) = \alpha(x).$$
* If $x \in \operatorname{supp}(\beta)$ and $x \notin \operatorname{supp}(\alpha)$, then $\alpha(x) = x$, so
  $$\alpha\beta(x) = \beta(x), \quad \beta\alpha(x) = \beta(x).$$
* If $x \notin \operatorname{supp}(\alpha) \cup \operatorname{supp}(\beta)$, then both fix $x$, so
  $$\alpha\beta(x) = x = \beta\alpha(x).$$

In all cases $\alpha\beta(x) = \beta\alpha(x)$, hence $\alpha\beta = \beta\alpha$.
$\square$

---

## Theorem: Every Permutation Is a Product of Disjoint Cycles

**Statement:** For every $\sigma \in S_n$, there exist disjoint cycles $c_1, c_2, \cdots, c_r$ such that
$\sigma = c_1\,c_2\, \cdots \,c_r,$.

 The decomposition is unique up to the order of the cycles and cyclic rotation within each cycle.

---

**Proof:**
- The action of $\sigma$ partitions $X=\{1,\ldots,n\}$ into orbits $\text{Orb}_\sigma(x)$.
- For each orbit, list the elements by following $\sigma$ until you return to the start; this produces a cycle.
- Outside each orbit, $\sigma$ fixes elements, so the full permutation is the product of these cycles.
- By the lemma above, disjoint cycles commute, so the product does not depend on the order of the cycles.
$\square$

---

## Example

Using the earlier permutation in $S_6$,
$$ \sigma = \begin{pmatrix}
1 & 2 & 3 & 4 & 5 & 6 \\
3 & 4 & 5 & 2 & 1 & 6
\end{pmatrix},
$$
we found orbits:
- $\text{Orb}_\sigma(1) = \{1,3,5\}$ gives the cycle $(1\,3\,5)$,
- $\text{Orb}_\sigma(2) = \{2,4\}$ gives the cycle $(2\,4)$,
- $\text{Orb}_\sigma(6) = \{6\}$ gives the cycle $(6)$ (a 1-cycle, usually omitted).

Thus,
$$\sigma = (1\,3\,5)(2\,4)(6) = (1\,3\,5)(2\,4).$$


---

## Useful Consequences

- Inverse: If $\sigma = (a_1\,a_2\,\dots\,a_k)\cdots$, then
  $$\sigma^{-1} = (a_k\,\dots\,a_2\,a_1)\cdots.$$
- Order: $\operatorname{ord}(\sigma) = \mathrm{lcm}$ of the lengths of its disjoint cycles.
