# Eucliean Spaces

## Problems
**1.2** Let
$
f(x)= \begin{cases}
    e^{-1/x}, & x > 0 \\
    0, & x \leq 0
\end{cases}
$

a. Show by induction that for $x > 0$ and $k \geq 0$, the $k$ th derivative $f^{(k)}(x)$ is of the form $p_{2k}(1/x)e^{-1/x}$ for some polynomial $p_{2k}(y)$ of degree $2k$ in $y$.

For the base case, when $k = 0$, $e^{-1/x} = p_0(1/x)e^{-1/x}$. By Chain Rule, $\frac{d}{dx}p_{2k}(1/x)e^{-1/x} = p_{2k}'(1/x)(-x^{-2})e^{-1/x} + p_{2k}(1/x)e^{-1/x}x^{-2} = e^{-1/x}(p_{2k}'(1/x)(-x^{-2}) + p_{2k}(1/x)x^{-2})$ where $p_{2k}'(1/x)(-x^{-2}) + p_{2k}(1/x)x^{-2}$ is a degree $2k+ 2$ polynomial. $\blacksquare$

b. Prove that $f$ is $C^\infty$ on $\mathbb{R}$ and that $f^{(k)}(0) = 0$ for all $k \geq 0$.

For $x < 0$, $f(x) = 0$ so all derivatives are 0. For $x > 0$, (a) shows that $f^{(k)}(x) = p_{2k}(1/x)e^{-1/x}$. We can see that $\lim_{x \rightarrow 0+} p_{2k}(1/x)e^{-1/x} = 0$ as exponential decay beats out polynomial growth. Further, because $f$ is constant for $x < 0$, $\lim_{x \rightarrow 0-} f(x) = 0$. Therefore, $f^{(k)}$ extends continuously to 0 by defining $f^{(k)}(0) = 0$.

Thus $f$ is $C^k$ for any $k \geq 0$ and hence smooth.

**1.3** Let $U \subset $\mathbb{R}^n$ and $V \subset \mathbb{R}^n$ be open subsets. A $C^\infty$ map $F: U \rightarrow V$ is called a diffeomorphism if it is bijective and has a $C^\infty$ inverse $F^{-1}: V \rightarrow U$.

a. Show that the function $f: (-\pi/2, \pi/2) \rightarrow \mathbb{R}, f(x) = \tan x$ is a diffeomorphism.

The map is bijective with inverse given by the smooth function $\arctan x$. Therefore, $\tan x$ is a diffeomorphism. $\blacksquare$

b. Let $a, b$ be real numbers with $a < b$. Find a linear function $h: (a, b) \rightarrow (-1, 1)$, thus proving that any two finite open intervals are diffeomorphic. 

Let $h = \frac{2(x - a)}{b - a} - 1$ which admits an inverse $h^{-1} = \frac{b - a}{2}x + \frac{b + a}{2}$. Both maps are $C^\infty$ and therefore $h$ is a diffeomorphism. $\blacksquare$

c. The exponential function $\text{exp}: \mathbb{R} \rightarrow (0, \infty)$ is a diffeomorphism. Use it to show that for any real numbers $a$ and $b$, the intervals $\mathbb{R}, (a, \infty)$, and $(-\infty, b)$ are diffeomorphic.

The linear map $h: x + a$ is a diffeomorphism between $(0, \infty)$ and $(a, \infty)$. The linear map $g: -x + b$ is a diffeomorphism between $(0, \infty)$ and $(-\infty, b)$. Thus, because diffeomorphisms are transitive, $\mathbb{R}, (a, \infty)$, and $(-\infty, b)$ are diffeomorphic. $\blacksquare$

**1.6** Prove that if $f: \mathbb{R}^2 \rightarrow \mathbb{R}$ is $C^\infty$, then there exist $C^\infty$ functions $g_{11}, g_{12}, g_{22}$ on $\mathbb{R}^2$ such that $$f(x, y) = f(0, 0) + \frac{\partial f}{\partial x}(0, 0)x + \frac{\partial f}{\partial y}(0, 0)y + x^2g_{11}(x, y) + \text{}$$ $$xyg_{12}(x, y) + y^2g_{22}(x, y)$$

**1.6** Prove that if $f: \mathbb{R}^2 \to \mathbb{R}$ is $C^\infty$, then there exist $C^\infty$ functions $g_{11}, g_{12}, g_{22}$ on $\mathbb{R}^2$ such that

$$
f(x,y) = f(0,0) + \frac{\partial f}{\partial x}(0,0)x + \frac{\partial f}{\partial y}(0,0)y + x^2g_{11}(x,y) + xyg_{12}(x,y) + y^2g_{22}(x,y).
$$

Since $f$ is $C^\infty$ on $\mathbb{R}^2$, it is smooth on a star-shaped region with respect to $(0,0)$. By Taylor's theorem with remainder, there exist smooth functions $h_1,h_2$ on $\mathbb{R}^2$ such that

$$
f(x,y) = f(0,0) + xh_1(x,y) + yh_2(x,y),
$$

where $h_1(0,0) = \frac{\partial f}{\partial x}(0,0)$ and $h_2(0,0) = \frac{\partial f}{\partial y}(0,0)$.

Now apply Taylor's theorem with remainder again to $h_1$ and $h_2$. Since $h_1$ and $h_2$ are smooth, there exist smooth functions $g_{11},g_{12},g_{21},g_{22}$ on $\mathbb{R}^2$ such that

$$
h_1(x,y) = h_1(0,0) + xg_{11}(x,y) + yg_{12}(x,y)
$$

and

$$
h_2(x,y) = h_2(0,0) + xg_{21}(x,y) + yg_{22}(x,y).
$$

Substituting these expressions into the formula for $f$, we get

$$
\begin{aligned}
f(x,y)&= f(0,0) + x\left(h_1(0,0) + xg_{11}(x,y) + yg_{12}(x,y)\right) + y\left(h_2(0,0) + xg_{21}(x,y) + yg_{22}(x,y)\right) \\
&= f(0,0) + xh_1(0,0) + yh_2(0,0) + x^2g_{11}(x,y) + xy g_{12}(x,y) + xy g_{21}(x,y) + y^2g_{22}(x,y).
\end{aligned}
$$

Using $h_1(0,0) = \frac{\partial f}{\partial x}(0,0)$ and $h_2(0,0) = \frac{\partial f}{\partial y}(0,0)$, we obtain

$$
f(x,y) = f(0,0) + \frac{\partial f}{\partial x}(0,0)x + \frac{\partial f}{\partial y}(0,0)y + x^2g_{11}(x,y) + xyg_{12}(x,y) + y^2g_{22}(x,y).
$$

where we substitute $g_{12} + g_{21}$ with $g_{12}$, which is smooth as the sum of smooth functions is smooth. $\blacksquare$

**1.7 (A function with removable singularity)** A removable singularity is a point where a function is not defined but can be redefined to become smooth. Let $f: \mathbb{R}^2 \rightarrow \mathbb{R}$ be a $C^\infty$ function with $f(0, 0) = \partial f / \partial x (0, 0) = \partial f / \partial y (0, 0) = 0$. Define

$$
g(t, u) = \begin{cases}
    \frac{f(t, tu)}{t} & t \neq 0 \\
    0 & t = 0
\end{cases}
$$

Prove that $g(t, u)$ is $C^\infty$ for $(t, u) \in \mathbb{R}^2$.

By 1.6, we have $f(x, y) = x^2g_{11}(x, y) + xyg_{12}(x, y) + y^2g_{22}(x, y)$ and thus, $f(t, tu) = t^2g_{11}(t, tu) + t^2ug_{12}(t, tu) + t^2u^2g_{22}(t, tu)$. Thus, $\frac{f(t, tu)}{t} = tg_{11}(t, tu) + tug_{12}(t, tu) + tu^2g_{22}(t, tu)$.

Define $G(t, u) = tg_{11}(t, tu) + tug_{12}(t, tu) + tu^2g_{22}(t, tu)$. $G$ is smooth on all of $\mathbb{R}^2$ as it is built from smooth functions using addition, multiplication, and composition with the smooth map $(t, u) \mapsto  (t, tu)$. For $t \neq 0$, $G(t, u) = \frac{f(t, tu)}{t} = g(t, u)$ and for $t = 0$, $G(0, u) = 0 = g(0, u)$. Therefore, $g = G$ and thus $g$ is a smooth function on $\mathbb{R}^2$. $\blacksquare$

**Intuition**: Because $f(0, 0) = 0, f_x(0, 0) = 0, f_y(0, 0) = 0$, $f$ has no constant term and no linear term at $(0, 0)$ so its Taylor expansion begins at quadratic order $f(x, y) = x^2g_{11}(x, y) + xyg_{12}(x, y) + y^2g_{22}(x, y)$. Then along the curve $(x, y) = (t, tu)$, every term gains at least $t^2$:

$$f(t, tu) = t^2(\text{smooth thing})$$

that is smooth and equals 0 when $t = 0$. Overall,

$$\text{vanishing order} \geq \text{order of denominator} \implies \text{removable singularity}$$

Conceptually, while ordinary limit checking proves continuity, Taylor's theorem with remainder is stronger because it provides a new smooth formula across the domain.

# Tangent Vectors in $\mathbb{R}^n$ as Derivations
A secant plane to a surface in $\mathbb{R}^3$ is determined by three points on the surface. As the three points approach a point $p$, if the secant planes approach a limiting position, then the limiting plane is known as the tangent plane. The three points should not become collinear. A cone at its tip is an example of a point without a limiting plane. Tangent vectors are those that lie in the tangent plane.

Our goal is to find a characterization of tangent vectors that generalizes to manifolds.

The tangent space $T_p(\mathbb{R}^n)$ at $p \in \mathbb{R}^n$ is the vector space of all tangent vectors based at the point $p$. $T_p(\mathbb{R}^n)$ can naturally be identified with $\mathbb{R}^n$. For example, the vector $v = (-1, 2)$, rooted at $p$ pointing 1 unit left and two units up, can be thought of as $(-1, 2) \in \mathbb{R}^2$.

If $f$ is smooth in a neighborhood at $p$ and $v$ is a tangent vector at $p$, the directional derivative is defined as

$$D_vf = \lim_{t \rightarrow 0} \frac{f(c(t)) - f(p)}{t} = \frac{d}{dt} \bigg|_{t = 0} f(c(t))$$

where $c(t) = (p^1 + tv^1, \ldots, p^n + tv^n)$ is a parameterization of a line through $p$ with direction $v$. By the Chain Rule,

$$D_vf = \sum_{i = 1}^n \frac{dc^i}{dt}(0)\frac{\partial f}{\partial x^i}(p) = \sum_{i = 1}^n v^i \frac{\partial f}{\partial x^i}(p)$$

We write $D_v = \sum v^i \frac{\partial}{\partial x^i} |_p$ as the map that sends a function $f$ to the number $D_vf$.

Consider the set of all pairs $(f, U)$ where $U$ is a neighborhood of $p$ and $f:U \rightarrow \mathbb{R}$ is a smooth function. $(f, U)$ is equivalent to $(g, V)$ if there is an open set $W \ subset U \cap V$ containing $p$ such that $f = g$ when restricted to $W$. This iss an equivalence relation and the equivalence class of $(f, U)$ is called the **germ** of $f$ at $p$. $C_p^\infty$ or $C_p^\infty(\mathbb{R}^n)$ refers to the set of all germs of smooth functions at $p$.

$$f(x) = \frac{1}{1 - x}$$

with domain $\mathbb{R} - 1$ and $$g(x) = 1 + x + x^2 + \ldots$$ on the interval $(-1, 1)$, have the same germ for any point in $(-1, 1)$.

An algebra over a field $K$ is a vector space $A$ over $K$ with map $\mu: A \times A \rightarrow A$ that satisfies associativity, distributivity, and homogeneity ($r(a \cdot b) = (r a) \cdot b  = a \cdot (rb)$). That is $A$ is a ring $A$ that is also a vector space over $K$.

A map $L: V \rightarrow W$ between vector spaces over a field $K$ is a linear map if for any $r \in K$ and $u, v \in V$, $L(u + v) = L(u) + L(v)$ and $L(ru) = rL(u)$.

## Derivations at a Point

The map $D_v: C_p^\infty \rightarrow \mathbb{R}$ gives a $\mathbb{R}$-linear map that satisfies the Leibniz rule

$$D_v(fg) = (D_vf)g(p) + f(p)D_vg$$

as partial derivatives have this property. Any linear map $D: C_p^\infty \rightarrow \mathbb{R}$ satisfying the Leibniz rule is called a **derivation at $p$**. Denote the set of all derivations at $p$ as $D_p(\mathbb{R}^n)$. This set is a real vector space.

Directional derivatives at $p$ are all derivations so there is a map $\phi: T_p(\mathbb{R}^n) \rightarrow D_p(\mathbb{R}^n)$ that maps $v \mapsto D_v = \sum v_i \frac{\partial}{\partial x^i} |_p$.

**Lemma** If $D$ is a point derivation of $C_p^\infty$ then $D_(c) = 0$ for any constant function $c$.
Proof: By Leibniz, $D(1) = D(1 \cdot 1) = D(1) \cdot 1 + 1 \cdot D(1) = 2D(1)$ and $D(1) = 0$.

**Theorem** The linear map $\phi: T_p(\mathbb{R}^n) \rightarrow D_p(\mathbb{R}^n)$ is an isomorphism of vector spaces.

Proof: To show injectivity, let $D_v = 0$ for some $v \in T_p(\mathbb{R}^n)$. Applying $D_v$ to the coordinate function $x^j$ shows that $0 = D_v(x^j) = \sum_i v_i \frac{\partial}{\partial x^i} |_p = v_j$. Thus, $v = 0$.

To show surjectivity, let $D$ be a derivation and let $(f, V)$ be a representative germ of $D$. We can assume $V$ is a ball and hence star shaped. By Taylor's theorem with remainder, there are smooth functions $g_i(x)$ such that

$$f(x) = f(p) + \sum (x^i - p^i)g_i(x), g_i(p) = \frac{\partial}{\partial x^i}(p)$$

Applying $D$ to both sides we have $Df(x) = \sum (Dx^i)g_i(p) + \sum (p^i - p^i)Dg_i(x) = \sum(Dx^i)\frac{\partial}{\partial x^i}(p)$. Therefore, $D = D_v$ for $v = (Dx^1, \ldots, Dx^n)$.

## Vector Fields
A vector field $X$ on an open subset $U$ of $\mathbb{R}^n$ is a function that assigns to each point $p$ a tangent vector $X_p$ in $T_p(\mathbb{R}^n)$. Since $T_p(\mathbb{R}^n)$ has basis $\{\partial / \partial x^i |_p\}$, the vector $X_p$ is a linear combination

$$X_p = \sum a^i(p)\frac{\partial}{\partial x^i} \bigg|_p, p \in U, a^i(p) \in \mathbb{R}$$

## Vector Fields as Derivations
For a smooth vector field $X$ on an open subset $U$ of $\mathbb{R}^n$ and $f$ is a smooth function then we can view $X$ as an operator that maps smooth functions on $U$ to smooth functions on $U$ where $(Xf)(p) = X_pf$.