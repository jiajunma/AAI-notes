---
marp: true
theme: default
paginate: false
---



# Permutation Group 

## Definition
A permutation of a set A is a function $\phi : A \rightarrow A$ that is both one-to-one and onto.

## Theorem
Let A be a nonempty set, and let $S_A$ be the collection of all permutations of A. Then $S_A$ is a group under permutation multiplication.

---
# $S_n$ 

**Definition** Let A be the finite set {1, 2, ..., n}. The group of all permutations of A is the **symmetric group on n letters**, and is denoted by $S_n$.

---
## Elements of $S_3$

The group $S_3$ is the symmetric group on 3 elements.  

1. The identity: $\mathrm{id} = (1)$ (leaves everything fixed)
2. The transpositions (2-cycles):
   - $(12)$: swaps 1 and 2
   - $(13)$: swaps 1 and 3
   - $(23)$: swaps 2 and 3
3. The 3-cycles:
   - $(123)$: sends $1\to2$, $2\to3$, $3\to1$
   - $(132)$: sends $1\to3$, $3\to2$, $2\to1$
In conclusion, 
$$
S_3 = \left\{
    (1),\ 
    (12),\ 
    (13),\ 
    (23),\ 
    (123),\ 
    (132)
\right\}
$$

---

## Order of $S_n$

The symmetric group $S_n$ has $n!$ elements.

**Reason:**  
A permutation of $n$ elements is a bijective map from the set $\{1, 2, \dots, n\}$ to itself. To specify such a function $\sigma$, we arrange $\sigma(1)\sigma(2)\cdots \sigma(n)$ in order; thus, there are $n!$ possibilities (the number of ways to order $n$ objects).

Therefore,
$$
|S_n| = n!
$$


---

# Group Action

## Definition

Let $X$ be a set and $G$ a group. An **action of $G$ on $X$** is a map $* : G \times X \rightarrow X$ such that:

1. **$ex = x$** for all $x \in X$,
2. $(g_1g_2)(x) = g_1(g_2x)$ for all $x \in X$ and all $g_1, g_2 \in G$.

Under these conditions, $X$ is a **$G$-set**.

---

**Note:** A $G$-set consists of:
- $G$ is a group
- $X$ is a set
- $*: G \times X \rightarrow X$, satisfies the above conditions

## Example

**Permutation** group $S_X$ acts on $X$

(The symmetric group $S_X$ acts on the set $X$)

---
## Claim

For each $g \in G$, the map $\sigma_g : X \to X$ defined by $\sigma_g(x) = g x$ is a bijection.

**Proof Sketch:**  
Since each group element $g$ has an inverse $g^{-1}$, the map $\sigma_{g^{-1}}$ serves as the inverse of $\sigma_g$:
$$
\sigma_g(\sigma_{g^{-1}}(x)) = g(g^{-1}x) = (gg^{-1})x = ex = x
$$
and
$$
\sigma_{g^{-1}}(\sigma_g(x)) = g^{-1}(g x) = (g^{-1}g)x = ex = x
$$
Thus, $\sigma_g$ is indeed a bijection (permutation) of $X$ for each $g \in G$.

---

# Group action vs. homomorphism to $S_X$
$$
\set{G-set structure on X} \leftrightarrow \set{homo. f: G \to S_X}
$$

---

# Orbit

## Definition

Let $G$ act on a set $X$, and let $x \in X$. The **orbit of $x$ under $G$**, denoted by $G \cdot x$ or $\text{Orb}_G(x)$, is the set:

$$
G \cdot x = \{gx \mid g \in G\}
$$

That is, the orbit of $x$ is the set of all elements of $X$ that can be reached from $x$ by applying some element of $G$.

---

# Stabilizer

## Definition

Let $G$ act on a set $X$, and let $x \in X$. The **stabilizer of $x$**, denoted by $G_x$ or $\text{Stab}_G(x)$, is the set:

$$
G_x := \text{Stab}_G(x) := \{g \in G \mid gx = x\}
$$

That is, the stabilizer of $x$ is the set of all elements of $G$ that fix $x$.

**Note:** The stabilizer $G_x$ is a subgroup of $G$.

---

# Fixed Point Set

## Definition

Let $G$ act on a set $X$, and let $g \in G$. The **fixed point set of $g$**, denoted by $X^G$, is the set:

$$
X^G = \{x \in X \mid \forall g, gx = x\}
$$

That is, the fixed point set of $G$ is the set of all elements of $X$ that are fixed by every $G$.

--- 

# Example: Group Action by Left Translation

Let $G$ be a group. Consider the set $X = G$ itself, and define the action of $G$ on $X$ by **left translation**:

$$
g \cdot x = gx
$$

for all $g, x \in G$.

- This is a group action: 
    - The identity acts as the identity: $e \cdot x = ex = x$.
    - It respects the group law: $g_1 \cdot (g_2 \cdot x) = g_1(g_2x) = (g_1g_2)x = (g_1g_2) \cdot x$.

- The orbit of any $x \in G$ is $G$ itself.
- The stabilizer of $x$ is just $\{e\}$, because only the identity fixes $x$ under left multiplication.

--- 

# Example: Group Action by Right Translation Viewed as a Left Action

We can also consider the **right translation** as a group action, but to fit left actions, we describe it as follows:

Let $G$ be a group, and let $X = G$. Define, for $g \in G$ and $x \in X$,
$$
g \cdot x = xg^{-1}
$$

This defines a **left group action**:
- The identity acts as $e \cdot x = xe^{-1} = x$.
- For $g, h \in G$, $g \cdot (h \cdot x) = g \cdot (x h^{-1}) = (x h^{-1}) g^{-1} = x (hg)^{-1} = (hg) \cdot x$.


**Orbits and stabilizers:**
- The orbit of any $x \in G$ is $G$ itself.
- The stabilizer of $x$ is again $\{e\}$, since $g \cdot x = x$ means $xg^{-1} = x$ $\implies$ $g = e$.

---
# Example: Group Action by Conjugation on $G$ Itself

Let $G$ act on itself by **conjugation**:
$$
g \cdot x = gxg^{-1}
$$
for $g, x \in G$.

- **Orbits:** The orbit of $x \in G$ under this action is the set of all elements conjugate to $x$, called the **conjugacy class** of $x$:
    $$
    \operatorname{Orb}_G(x) = \{gxg^{-1} : g \in G\}
    $$

- **Stabilizer:** The stabilizer of $x$ is the **centralizer** of $x$ in $G$:
    $$
    \operatorname{Stab}_G(x) = \{g \in G: gxg^{-1} = x\} = Z_G(x)
    $$

- **Fixed points:** The fixed points are those $x \in G$ such that $gxg^{-1} = x$ for all $g \in G$, i.e., the elements of the **center** $Z(G)$.

---

# Example: $G$ acts on its Subgroups by Conjugation

 Consider the set $X$ of all subgroups of $G$.

We can define an action of $G$ on $X$ as follows: for $g \in G$, $H \leq G$,
$$
g \cdot H = gHg^{-1} = \{ghg^{-1} : h \in H\}
$$


**Stabilizer:** The stabilizer of $H$ is its **normalizer** in $G$:
$$
\operatorname{Stab}(H) = \{g \in G : gHg^{-1} = H\} = N_G(H)
$$

A subgroup $H$ is *normal* in $G$ if and only if $gHg^{-1} = H$ for all $g \in G$, i.e., its orbit is a singleton.
**Fixed Point Set:** The **fixed points** of the conjugation action are those subgroups $H \leq G$ for which $gHg^{-1} = H$ for all $g \in G$. But this is precisely the definition of a **normal subgroup**. 

---
# Example: $GL_n(\mathbb{R})$ acts on $\mathbb{R}^n$

Let $G = GL_n(\mathbb{R})$, the group of invertible $n \times n$ real matrices, and let $X = \mathbb{R}^n$.

Define the action by **matrix multiplication**:
$$
A \cdot \mathbf{v} = A \mathbf{v}
$$
for $A \in GL_n(\mathbb{R})$, $\mathbf{v} \in \mathbb{R}^n$.

- The group action rules hold:
    1. **Identity:** $I \cdot \mathbf{v} = I \mathbf{v} = \mathbf{v}$.
    2. **Compatibility:** $(AB)\cdot \mathbf{v} = AB\mathbf{v} = A(B\mathbf{v}) = A\cdot (B\cdot \mathbf{v})$.

**Orbits:**
- The orbit of the zero vector $\mathbf{0}$ is just $\{\mathbf{0}\}$.
- {all nonzero vector $\mathbf{v} \neq 0$}. 

---
# Example: $GL_n(\mathbb{C})$ acts on $M_n(\mathbb{C})$ by Conjugation

Let $G = GL_n(\mathbb{C})$, the group of invertible $n\times n$ complex matrices, and let $X = M_n(\mathbb{C})$, the set of all $n \times n$ complex matrices.

We define the action by **conjugation**:
$$
A \cdot X = AXA^{-1}
$$
for $A \in GL_n(\mathbb{C})$, $X \in M_n(\mathbb{C})$.

**Orbits:**
- The orbit of a matrix $X$ under this action is the set of all matrices similar to $X$; that is, all matrices $Y$ such that $Y = AXA^{-1}$ for some $A\in GL_n(\mathbb{C})$.
- Two matrices are in the same orbit if and only if they are **similar**, i.e., have the same Jordan canonical form.

---

# Jordan Canonical Form and the Orbit Structure

- The **Jordan canonical form** of a matrix $X$ over $\mathbb{C}$ is a "canonical" representative for the similarity class (the $GL_n(\mathbb{C})$-orbit) of $X$.
- Every matrix $X \in M_n(\mathbb{C})$ is conjugate to a unique Jordan matrix (up to block order).

**Consequences:**
- The set of $GL_n(\mathbb{C})$-orbits on $M_n(\mathbb{C})$ corresponds to the set of all possible Jordan canonical forms (block types).

---
# Example: $O_n(\mathbb{R})$ acts on symmetric matrices

Let $G = O_n(\mathbb{R})$, the group of $n \times n$ real orthogonal matrices ($A^T A = I$), and let $X = \mathrm{Sym}_n(\mathbb{R})$, the set of real symmetric $n \times n$ matrices ($S^T = S$).

We define the group action by **conjugation**:
$$
A \cdot S = ASA^T
$$
for $A \in O_n(\mathbb{R})$, $S \in \mathrm{Sym}_n(\mathbb{R})$.

---

**Orbits:**
- The orbit of a symmetric matrix $S$ is the set of all symmetric matrices with the same **eigenvalues** (with multiplicities) as $S$.
- This is due to the **Spectral Theorem**: Every real symmetric matrix is diagonalizable by an orthogonal matrix.
- Thus, each orbit corresponds to the set of symmetric matrices with a given unordered set of real eigenvalues.

---

# Example: $U_n$ acts on Hermitian matrices by conjugation

Let $G = U_n$, the group of $n \times n$ unitary matrices ($U^* U = I$), and let $X = \mathrm{Herm}_n(\mathbb{C})$, the space of Hermitian $n \times n$ matrices ($H^* = H$).

We define the group action by **conjugation**:
$$
U \cdot H = UHU^*
$$
for $U \in U_n$, $H \in \mathrm{Herm}_n(\mathbb{C})$.

---

**Orbits:**
- The orbit of a Hermitian matrix $H$ consists of all Hermitian matrices with the same spectrum (the same set of real eigenvalues with multiplicities).
- This follows from the **Spectral Theorem for Hermitian matrices**: every Hermitian matrix is diagonalizable by a unitary matrix, i.e., for every $H$ there exists $U \in U_n$ such that $UHU^* = D$ is diagonal with real entries.
- Thus, the $U_n$-orbit of $H$ is determined by its set of eigenvalues.

**Summary:**  
The set of $U_n$-orbits on $\mathrm{Herm}_n(\mathbb{C})$ is in bijection with the unordered $n$-tuples of real numbers (multisets of eigenvalues).




