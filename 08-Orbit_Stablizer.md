---
marp: true
theme: default
paginate: true 

---
## Morphisms and Isomorphisms of G-sets

* Recall: $G$-set is a set $X$ equipped with an action $\cdot: G \times X \to X$.

* Morphism ($G$-equivariant map): A function $f: X \to Y$ between $G$-sets such that
  $$f(g \cdot x) = g \cdot f(x)\quad \text{for all } g \in G,\; x \in X.$$

* Example:  
  Identity maps $id : X \to X$ is a $G$-equivariant map. 

* Example 2 (closure under composition): Let $X, Y, Z$ be $G$-sets and let $f: X \to Y$, $g: Y \to Z$ be $G$-equivariant. Then $g \circ f: X \to Z$ is $G$-equivariant.

---
## Isomorphisms of G-sets

* Isomorphism of $G$-sets: A bijective $G$-equivariant map $f: X \to Y$.
  Equivalently, $f$ is an isomorphism iff there exists $h: Y \to X$ with
  $$h(g \cdot y) = g \cdot h(y)\quad \text{for all } g \in G,\; y \in Y$$
  and $h \circ f = id_X$ and $f \circ h = id_Y$.

  In this case we write $X \cong Y$ as $G$-sets.

--- 
# Left coset as an $G$-set

## Left Cosets as a $G$-set

* Let $H$ be a subgroup of $G$. The set of left cosets $G/H = \{gH : g \in G\}$ has a natural $G$-set structure.

* **Group Action**: Define $\cdot: G \times G/H \to G/H$ by:
  $$g \cdot (hH) = (gh)H$$

* **Well-defined**: This action is well-defined because if $h_1H = h_2H$, then:
  $$g \cdot (h_1H) = (gh_1)H = (gh_2)H = g \cdot (h_2H)$$

---

## Every Orbit is Isomorphic to Left Cosets




**Theorem**: Let $G$ act on a set $X$, and let $x \in X$. Then the orbit $G \cdot x$ is in bijection with the set of left cosets $G/S_x$, where $S_x$ is the stabilizer of $x$.

$$G/S_x \cong G \cdot x$$

Proof: Define a $G$-equivariant bijection $\varphi: G/S_x \to G \cdot x$ by:

---

## The Bijection



Define $\varphi: G/S_x \to G \cdot x$ by:

$$\varphi(gS_x) = g \cdot x$$

* **Well-defined**: If $gS_x = hS_x$, then $g^{-1}h \in S_x$, so: $$h \cdot x = (g \cdot g^{-1}h) \cdot x = g \cdot (g^{-1}h \cdot x) = g \cdot x$$

* **Injective**: If $g \cdot x = h \cdot x$, then $g^{-1}h \cdot x = x$, so $g^{-1}h \in S_x$, thus $gS_x = hS_x$

* **Surjective**: Every element in $G \cdot x$ has form $g \cdot x$ for some $g \in G$

* **$G$-equivariant**: For any $g, h \in G$:
$$\varphi(g \cdot (hS_x)) = \varphi((gh)S_x) = (gh) \cdot x = g \cdot (h \cdot x) = g \cdot \varphi(hS_x)$$
---


## Consequence: Orbit-Stabilizer Theorem

**Theorem**:   
Since $|G/S_x| = \frac{|G|}{|S_x|}$ (for finite groups), we get:

$$|G \cdot x| \cdot |S_x| = |G|$$

Recall $S_x := \{g \in G : g \cdot x = x\}$ is the stabilizer of $x$.

**Key Insight**: The size of an orbit times the size of its stabilizer equals the size of the group!

---
## Example Application: Size of $S_n$. 
  Prove $|S_n| = n!$ using the orbit-stabilizer theorem.

  
**Solution**: Consider the action of $S_n$ on the set $X = \{1, 2, \ldots, n\}$ by permutation.


* Pick $x = n \in X$. The orbit is $S_n \cdot n = X$ (since any element can be moved to any position).

* The stabilizer $Stab_{S_n}(n)= \{\sigma \in S_n : \sigma(n) = n\}$ consists of permutations fixing $n$, which is isomorphic to $S_{n-1}$.

* By the orbit-stabilizer theorem:
  $$|S_n| = |S_n \cdot n| \cdot |Stab_{S_n}(n)| = |S_n| = n \cdot |S_{n-1}| = n \cdot (n-1)!$$

* Last equation is true by induction: $|S_{n-1}| = (n-1)!$.

---
## Class Equation (via conjugation action)

* Conjugation action: Let $G$ act on itself by
  $$g \cdot x := gxg^{-1} \quad \text{for } g,x \in G.$$

* Orbits: The orbits are the conjugacy classes
  $$\mathrm{Cl}(x) := \{gxg^{-1} : g \in G\}.$$

* Stabilizers: The stabilizer of $x$ is its centralizer
  $$C_G(x) := \{g \in G : gx = xg\}.$$

* Orbit–Stabilizer gives
  $$|\mathrm{Cl}(x)| = [G : C_G(x)] = \frac{|G|}{|C_G(x)|}.$$

---
## The Class Equation

**Theorem (Class Equation):**  
Let $Z(G)$ denote the center of $G$. For a finite group $G$, choosing a set $\{x_i\}$ of representatives of non-central conjugacy classes, we have
$$
|G| \;=\; |Z(G)| \;+\; \sum_i [G : C_G(x_i)]
\;=\; |Z(G)| \;+\; \sum_i \frac{|G|}{|C_G(x_i)|}.
$$

*Proof idea:*  
$G$ is the disjoint union of its conjugacy classes. Elements of $Z(G)$ have singleton conjugacy classes, while non-central elements lie in orbits of size $[G:C_G(x)]$. Summing orbit sizes gives the formula.

---
## Class Equation an application 

**Theorem:**  
 Center of $p$-groups is nontrivial:

  * If $|G| = p^n$, then every index $[G:C_G(x)]$ is a power of $p$, hence divisible by $p$ for every non-central element $x$.
  * From the class equation, $|G| \equiv |Z(G)| \pmod{p}$, so $|Z(G)| \equiv 0 \pmod{p}$.
  * $Z(G)$ is nonempty (since it contains at least the identity element).
  * Therefore $|Z(G)| \ge p$, implying $Z(G)$ is nontrivial.
