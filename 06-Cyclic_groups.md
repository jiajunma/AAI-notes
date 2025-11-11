---
marp: true
theme: default
paginate: false
---

# Left Cosets and Left Coset Space

---

## Definition: Left Coset

Let $G$ be a group and $H$ a subgroup of $G$.

For any $g \in G$, the **left coset** of $H$ containing $g$ is:
$$gH = \{gh : h \in H\}$$

---

## Properties of Left Cosets

1. **$g \in gH$** (since $e \in H$)
2. **$gH = H$ if and only if $g \in H$**
3. **$gH = g'H$ if and only if $g^{-1}g' \in H$**
4. **Two left cosets are either identical or disjoint**
5. **All left cosets have the same cardinality**: $|gH| = |H|$

---

## Left Coset Space

The **left coset space** (or **quotient set**) is:
$$G/H = \{gH : g \in G\}$$

The number of distinct left cosets is called the **index** of $H$ in $G$:
$$[G : H] = |G/H|$$

---

## Lagrange's Theorem

If $G$ is a finite group and $H$ is a subgroup of $G$, then:
$$|G| = |H| \cdot [G : H]$$

**Corollary**: The order of any subgroup divides the order of the group.

---

## Normal Subgroups

A subgroup $H$ of $G$ is **normal** (denoted $H \trianglelefteq G$) if:
$$gH = Hg \quad \text{for all } g \in G$$

Equivalent definition: 
- $gh g^{-1} \in H$ for all $h\in H$ and $g\in G$
- $gHg^{-1} = H$ for all $g \in G$

When $H$ is normal, the left and right cosets coincide.

---

## Quotient Group

If $H \trianglelefteq G$, then the **quotient group** $G/H$ is a group under the operation:
$$(gH)(g'H) = (gg')H$$

The identity element is $H$, and the inverse of $gH$ is $g^{-1}H$.


---

## Group Homomorphism, Kernel and Image
A **group homomorphism** is a function $f : G \to H$ between groups $G$ and $H$ such that for all $g_1, g_2 \in G$,
$$
f(g_1g_2) = f(g_1)f(g_2)
$$

- The **kernel** of $f$ is the set:
  $$
  \ker(f) = \{g \in G : f(g) = e_H\}
  $$
  where $e_H$ is the identity in $H$.
The kernel $\ker(f)$ is always a normal subgroup of $G$. 

- The **image** of $f$ is the set:
  $$
  \operatorname{im}(f) = \{f(g) : g \in G\}
  $$
The **image** $\operatorname{im}(f)$ of a group homomorphism $f: G \to H$ is always a subgroup of $H$.


---

# Isomorphism Theorems

---

## First Isomorphism Theorem

Let $f: G \to H$ be a group homomorphism.

Then:
$$G / \ker(f) \cong \operatorname{im}(f)$$

**Key idea**: Every homomorphism factors through its kernel.

---

## Applications of First Isomorphism Theorem

**Example**: $\mathbb{Z}/n\mathbb{Z} \cong \mathbb{Z}_n$

Define $\phi: \mathbb{Z} \to \mathbb{Z}_n$ by $\phi(k) = k \bmod n$.

Then $\ker(\phi) = n\mathbb{Z}$ and $\operatorname{im}(\phi) = \mathbb{Z}_n$.

---
# Order of an element

An element $g \in G$ is said to have *finite order* if
$$
\exists n >0 \text{such that $g^n = 1$}
$$
Otherwise an element is called *infinite order*. 

*Lemma*
$$
|g| = |\langle g \rangle|
$$
Proof: 
- Consider the map $f : \mathbb{Z} \to G$ sending $n$ to $g^n$. 
- Consider the kernel of $f$. 

---
*Lemma:* $|g|$ divides $|G|$ if $G$ is finite. 

We write $|g| = 0$ if $g$ has infinite order. Then 

*Lemma:* $g^k = 1$ if and only if $k \in |g| \mathbb{Z}$, i.e. $|g|$ divides $k$. 

--- 
# Subgroups of $\mathbb{Z}$. 

*Theorem:* Every subgroups of $\mathbb{Z}$ has the form $n \mathbb{Z}$ for some $n\in \mathbb{N}$. 

---

## Second Isomorphism Theorem

Let $H$ be a subgroup and $N$ a normal subgroup of $G$.

Then:
$$HN/N \cong H/(H \cap N)$$

*Proof* Consider the map 
$$
H \rightarrow G/N
$$ 
given by $h \mapsto hN$. 

**Note**: $HN = \{hn : h \in H, n \in N\}$ is a subgroup when $N \trianglelefteq G$.


**Fact** $HN$ is a subgroup of $G$ if and only if $N \in Norm_G(H)$. 

---

## Third Isomorphism Theorem

Let $N$ and $M$ be normal subgroups of $G$ with $N \subseteq M$.

Then:
$$(G/N)/(M/N) \cong G/M$$

*Proof* Consider the map 
$$
G/N \rightarrow G/M
$$