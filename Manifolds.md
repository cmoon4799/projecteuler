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