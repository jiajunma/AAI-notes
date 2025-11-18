---
marp: true
theme: default
paginate: true
size: 16:9
fontsize: 16px
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

---

## Algorithm: Determining Cycle Notation

**Input:** A permutation $\sigma \in S_n$ (given in two-line notation or as a function)

**Output:** Cycle notation of $\sigma$

**Algorithm:**

1. Initialize an empty list of cycles: `cycles = []`
2. Initialize a set of unvisited elements: `unvisited = {1, 2, ..., n}`

---

3. While `unvisited` is not empty:
   - Pick an element $x$ from `unvisited`
   - Initialize a new cycle: `current_cycle = [x]`
   - Set $y = \sigma(x)$
   - While $y \neq x$:
     - Append $y$ to `current_cycle`
     - Remove $y$ from `unvisited`
      - Set $y = \sigma(y)$
   - Remove $x$ from `unvisited`
   - If length of `current_cycle` > 1:
     - Append `current_cycle` to `cycles`

---

4. Return `cycles`

**Time Complexity:** $O(n)$ — each element is visited exactly once.

---


## Example: Running the Algorithm

Consider $\sigma = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\ 4 & 7 & 6 & 8 & 2 & 3 & 5 & 1 & 10 & 9 \end{pmatrix}$

* **Iteration 1:** Start with $x = 1$
  - Cycle: $(1\,4\,8)$, unvisited: $\{2, 3, 5, 6, 7, 9, 10\}$
  
* **Iteration 2:** Start with $x = 2$
  - Cycle: $(2\,7\,5)$, unvisited: $\{3, 6, 9, 10\}$
  
* **Iteration 3:** Start with $x = 3$
  - Cycle: $(3\,6)$, unvisited: $\{9, 10\}$

* **Iteration 4:** Start with $x = 9$
  - Cycle: $(9\,10)$, unvisited: $\varnothing$

---

**Result:** $\sigma = (1\,4\,8)(2\,7\,5)(3\,6)(9\,10)$

**Verification:**
- Orbit of 1: $\{1, 4, 8\}$ with cycle length 3
- Orbit of 2: $\{2, 7, 5\}$ with cycle length 3
- Orbit of 3: $\{3, 6\}$ with cycle length 2
- Orbit of 9: $\{9, 10\}$ with cycle length 2
- Order of $\sigma$: $\operatorname{lcm}(3, 3, 2, 2) = 6$

---



## Multiplication of Permutations in Cycle Notation

**Convention:** We compose permutations from **right to left**.

If $\sigma = \alpha_1 \alpha_2 \cdots \alpha_r$ and $\tau = \beta_1 \beta_2 \cdots \beta_s$ are products of disjoint cycles, then
$$\sigma \tau = (\alpha_1 \alpha_2 \cdots \alpha_r)(\beta_1 \beta_2 \cdots \beta_s).$$

To compute the product, apply $\tau$ first, then $\sigma$.

---

## How to Compute Multiplication of Permutations

**Algorithm:**
1. **Apply from right to left:** For each element $x$, trace where it goes under the rightmost permutation first
2. **Continue left:** Apply the next permutation to the result from step 1
3. **Repeat:** Continue until all permutations have been applied
4. **Record the mapping:** Note where each element $x$ finally maps to
5. **Form cycles:** Group elements into cycles based on the final mapping

---

## Example 3: Product of Three Cycles

**Problem:** Compute $(1\,3\,5)(2\,4)(1\,2\,3)$ in $S_5$.

**Solution:** Apply $(1\,2\,3)$ → $(2\,4)$ → $(1\,3\,5)$ from right to left.

**Answer:** $(1\,3\,5)(2\,4)(1\,2\,3) = (1\,4\,2\,5)$


---

## Example : Conjugate a cycle

**Proposition:** Let $\sigma \in S_n$ be any permutation and $(a_1\,a_2\,\cdots\,a_k)$ be a $k$-cycle. Then
$$\sigma(a_1\,a_2\,\cdots\,a_k)\sigma^{-1} = (\sigma(a_1)\,\sigma(a_2)\,\cdots\,\sigma(a_k)).$$

**Proof:** 
We need to show that both sides have the same action on every element $x \in \{1,2,\ldots,n\}$.

* **Case 1:** Suppose $x = \sigma(a_i)$ for some $i \in \{1,2,\ldots,k\}$.  Then $\sigma^{-1}(x) = a_i$.

* **Case 2:** Suppose $x \neq \sigma(a_i)$ for all $i \in \{1,2,\ldots,k\}$.  Then $\sigma^{-1}(x) \neq a_i$ for all $i$ (since $\sigma$ is bijective).

--- 

## Theorem: Every Cycle Is a Product of Transpositions

**Statement:** Every $k$-cycle can be written as a product of $k-1$ transpositions.

Specifically, a $k$-cycle $(a_1\,a_2\,\cdots\,a_k)$ can be written as:
$$(a_1\,a_2\,\cdots\,a_k) = (a_1\,a_2)(a_2\,a_{3})\cdots (a_{k-1}\,a_k).$$


---

**Corollary:** Every permutation in $S_n$ can be written as a product of transpositions.

**Proof:** By the theorem on disjoint cycle decomposition, every permutation is a product of disjoint cycles. By the above theorem, each cycle is a product of transpositions. Therefore, every permutation is a product of transpositions.
$\square$


--- 
# Sign, Even and Odd permutations 
---

## Even and Odd Permutations

A permutation $\sigma \in S_n$ is called:
- even if it can be written as a product of an even number of transpositions,
- odd if it can be written as a product of an odd number of transpositions.

The definition is well-defined!

---

## Parity Is Well-Defined

**Theorem:** The parity (even/odd) of a permutation is well-defined: if
$\sigma = \tau_1 \cdots \tau_m = \rho_1 \cdots \rho_k$
are two factorizations of $\sigma$ into transpositions, then $m \equiv k \pmod{2}$.

---
**Proof:** 
Use group homomorphism to permutations matrix.

Define a group homomorphism $\phi: S_n \to \mathrm{GL}_n(\mathbb{R})$ by sending each permutation $\sigma$ to its **permutation matrix** $P_\sigma$, where
$$(P_\sigma)_{ji} = \begin{cases} 1 & \text{if } j = \sigma(i), \\ 0 & \text{otherwise}. \end{cases}$$

**Key Properties:**
- $\phi$ is a homomorphism: $\phi(\sigma\tau) = P_\sigma P_\tau$
- $\det(P_\sigma) = \operatorname{sgn}(\sigma)$


---

## Useful Formulas for Sign

- A $k$-cycle has sign
  $$\operatorname{sgn}((a_1\,a_2\,\dots\,a_k)) = (-1)^{k-1}.$$
- The sign is multiplicative:
  $$\operatorname{sgn}(\alpha\beta) = \operatorname{sgn}(\alpha)\operatorname{sgn}(\beta).$$
- For a product of disjoint cycles $c_1\cdots c_r$,
  $$\operatorname{sgn}(\sigma) = \prod_{i=1}^r \operatorname{sgn}(c_i).$$

---

## Alternating Group

The set of even permutations in $S_n$ forms a subgroup called the alternating group:
$$A_n = \{\sigma \in S_n \mid \operatorname{sgn}(\sigma) = +1\}.$$

Properties:
* $A_n$ is a normal subgroup of $S_n$ with index 2.
* $|A_n| = \dfrac{n!}{2}$.
* $A_n$ is simple for $n \geq 5$.

---

## Checking Parity via Inversions

Given $\sigma$ in two-line notation, write the bottom row as a list
$[\sigma(1), \sigma(2), \dots, \sigma(n)]$.
Define the number of inversions:
$$\mathrm{inv}(\sigma) = \#\{(i,j) \mid 1 \le i < j \le n,\ \sigma(i) > \sigma(j)\}.$$
Then
$$\operatorname{sgn}(\sigma) = (-1)^{\mathrm{inv}(\sigma)}.$$

Example (from earlier):
$$\sigma = \begin{pmatrix}
1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
4 & 7 & 6 & 8 & 2 & 3 & 5 & 1 & 10 & 9
\end{pmatrix}.$$
Here $\mathrm{inv}(\sigma) = 20$ (even), so $\sigma$ is even.
This matches the cycle decomposition $(1\,4\,8)(2\,7\,5)(3\,6)(9\,10)$ whose sign is
$(+1)\cdot(+1)\cdot(-1)\cdot(-1) = +1$.

---

## Example: Conjugate a Cycle

**Problem:** Compute $(2\,3\,5)(1\,2\,3\,4)(2\,3\,5)^{-1}$ in $S_5$.

**Solution using the Proposition:**

Let $\sigma = (2\,3\,5)$. By the proposition,
$$\sigma(1\,2\,3\,4)\sigma^{-1} = (\sigma(1)\,\sigma(2)\,\sigma(3)\,\sigma(4)).$$

Computing each image under $\sigma = (2\,3\,5)$:
- $\sigma(1) = 1$ (1 is fixed by $(2\,3\,5)$)
- $\sigma(2) = 3$
- $\sigma(3) = 5$
- $\sigma(4) = 4$ (4 is fixed by $(2\,3\,5)$)

Therefore:
$$(2\,3\,5)(1\,2\,3\,4)(2\,3\,5)^{-1} = (1\,3\,5\,4).$$

**Observation:** The conjugation relabels the elements in the 4-cycle according to $\sigma$, but preserves the cycle structure (it remains a 4-cycle).

---

# Conjugacy Classes in $S_n$
## Theorem: Conjugacy Classes and Partitions of n

- Two permutations in $S_n$ are conjugate if and only if they have the same cycle type.
- Equivalently, the conjugacy classes of $S_n$ are in bijection with the partitions of $n$.


--- 

# The alternating group $A_4$

The alternating group $A_4$ consists of all even permutations in $S_4$. It has order $|A_4| = \frac{4!}{2} = 12$.

1. **Identity:** $e$ (1 element)

2. **3-cycles** :
   - $(1\,2\,3)$, $(1\,3\,2)$, $(1\,2\,4)$, $(1\,4\,2)$, $(1\,3\,4)$, $(1\,4\,3)$, $(2\,3\,4)$, $(2\,4\,3)$
  8 elements total

3. **Products of two disjoint 2-cycles**:
   - $(1\,2)(3\,4)$, $(1\,3)(2\,4)$, $(1\,4)(2\,3)$ (3 elements total)

**Total:** $1 + 8 + 3 = 12$ elements ✓

---

## $A_4$ Is Not Simple

**Theorem:** $A_4$ is not a simple group.

**Proof:** We exhibit a nontrivial normal subgroup of $A_4$.

Let $K_4 = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$.

**Claim 1:** $K_4$ is a subgroup of $A_4$ (called the Klein four-group).
- Closed under multiplication: e.g., $(1\,2)(3\,4) \cdot (1\,3)(2\,4) = (1\,4)(2\,3)$
- Each element has order 2
- Identity is included
- $|K_4| = 4$

---

**Claim 2:** $K_4$ is normal in $A_4$.

We verify that $K_4$ is closed under conjugation by all elements of $A_4$.

**Key observation:** Elements of $V_4$ are products of two disjoint 2-cycles, and conjugating such an element by any permutation preserves this cycle type.

For any $\sigma \in A_4$ and any $(a\,b)(c\,d) \in V_4$:
$$\sigma(a\,b)(c\,d)\sigma^{-1} = (\sigma(a)\,\sigma(b))(\sigma(c)\,\sigma(d))$$

Therefore, $\sigma(a\,b)(c\,d)\sigma^{-1}$ is also a product of two disjoint 2-cycles in $A_4$, hence is in $V_4$.

---


## Semidirect Product Construction

**Motivation:** The semidirect product is a way to construct a group from two smaller groups, generalizing the direct product. It allows us to build groups where one subgroup acts on another by automorphisms.

---

## Definition: Semidirect Product

Let $N$ and $H$ be groups, and let $\phi: H \to \operatorname{Aut}(N)$ be a group homomorphism (called an **action** of $H$ on $N$ by automorphisms).

The **semidirect product** $N \rtimes_\phi H$ (or simply $N \rtimes H$ when $\phi$ is clear) is defined as:

**Set:** $N \rtimes H = N \times H$ (as sets)

**Group Operation:** For $(n_1, h_1), (n_2, h_2) \in N \rtimes H$,
$$(n_1, h_1) \cdot (n_2, h_2) = (n_1 \cdot \phi(h_1)(n_2), h_1 \cdot h_2)$$

where $\phi(h_1)(n_2)$ denotes the action of $h_1$ on $n_2$ via the homomorphism $\phi$.

---

## Properties of Semidirect Product

* **Identity:** $(e_N, e_H)$ where $e_N$ and $e_H$ are identities in $N$ and $H$ respectively

* **Inverse:** $(n, h)^{-1} = (\phi(h^{-1})(n^{-1}), h^{-1})$

* **Subgroups:**
   - $N \cong \{(n, e_H) \mid n \in N\}$ is a normal subgroup
   - $H \cong \{(e_N, h) \mid h \in H\}$ is a subgroup (not necessarily normal)

* **Order:** If $N$ and $H$ are finite, $|N \rtimes H| = |N| \cdot |H|$

---

## Special Case: Direct Product

When $\phi$ is the trivial homomorphism (i.e., $\phi(h) = \operatorname{id}_N$ for all $h \in H$), the semidirect product reduces to the **direct product**:
$$N \rtimes H = N \times H$$

with operation $(n_1, h_1)(n_2, h_2) = (n_1 n_2, h_1 h_2)$.


--- 

## Definition: Dihedral Group $D_n$

The **dihedral group** $D_n$ is the group of symmetries of a regular $n$-gon, including both rotations and reflections.

**Elements:**
- $n$ rotations: $\{e, r, r^2, \ldots, r^{n-1}\}$ where $r$ is rotation by $\frac{2\pi}{n}$ radians
- $n$ reflections: $\{s, sr, sr^2, \ldots, sr^{n-1}\}$ where $s$ is any reflection

**Relations:**
- $r^n = e$ (rotating $n$ times returns to the identity)
- $s^2 = e$ (reflecting twice returns to the identity)
- $srs^{-1} = r^{-1}$ (reflection reverses rotation direction)

**Order:** $|D_n| = 2n$

**Presentation:**
$$D_n = \langle r, s \mid r^n = s^2 = e, \, srs^{-1} = r^{-1} \rangle$$

---

## Example: Dihedral Group as Semidirect Product

The dihedral group $D_n$ can be expressed as:
$$D_n \cong \mathbb{Z}_n \rtimes \mathbb{Z}_2$$

where:
- $N = \mathbb{Z}_n = \langle r \rangle$ (rotations)
- $H = \mathbb{Z}_2 = \langle s \rangle$ (reflections, with $s^2 = e$)
- $\phi: \mathbb{Z}_2 \to \operatorname{Aut}(\mathbb{Z}_n)$ defined by:
  - $\phi(0)(r^k) = r^k$ (identity automorphism)
  - $\phi(1)(r^k) = r^{-k}$ (inversion automorphism)

This reflects the relation $srs^{-1} = r^{-1}$ in $D_n$.

---

## Example: Symmetric Group via Semidirect Product

For $n \geq 3$, we can write:
$$S_n \cong A_n \rtimes \mathbb{Z}_2$$

where:
- $N = A_n$ (alternating group, even permutations)
- $H = \mathbb{Z}_2 = \langle \tau \rangle$ for any transposition $\tau$
- $\phi: \mathbb{Z}_2 \to \operatorname{Aut}(A_n)$ given by conjugation:
  - $\phi(0) = \operatorname{id}_{A_n}$
  - $\phi(1)(\sigma) = \tau \sigma \tau^{-1}$

**Note:** This decomposition shows that $S_n$ is the internal semidirect product of $A_n$ and any transposition.
