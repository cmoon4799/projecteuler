# Analysis

## Power Series
If we have a power series $\sum_n a_n(x - a)^n$, we can calculate its radius of convergence through its coefficients; to do so, we can measure the exponential growth of $a_n$ or in other words, $|a_n|^{1/n}$. For example, if $\limsup |a_n|^{1/n} = 2$ then $\limsup |a_n(x - a)^n|^{1/n} = |x - a|\limsup |a_n|^{1/n} = 2|x - a|$; by the root test, if $|x - a| < 1/2$, the series converges absolutely and if $|x - a| > 1/2$, the series diverges hence its radius is 1/2.

It turns out that the derivative has the same radius of convergence. The root test of $\sum_n na_n(x - a)^{n - 1}$ gives us $\limsup |na_n|^{1/n}$; $n^{1/n} \rightarrow 1$ so $\limsup |na_n|^{1/n} = \limsup |a_n|^{1/n}$. However, we must justify that the term by term differentiation is equal to the derivative of the power series.

To justify term by term differentiation, we can use the following theorem. Let $f_n \in C^1$ on the interval $[a, b]$. Suppose $f_n(x_0)$ converges for some $x_0 \in [a, b]$, and $f_n' \rightarrow g$ uniformly. Then $f_n \rightarrow f$ uniformly for some differentiable function $f$ and $f' = g$.
Proof: By FTOC, $\int_{x_0}^x f_n'(t)\,dt = f_n(x) - f_n(x_0)$; we can see that $\int_{x_0}^x f_n'(t)\,dt + f_n(x_0)$ converges uniformly to $\int_{x_0}^x g(t)\,dt + c$ where c is the limit of $f_n(x_0)$. To see this, it is enough to show that $\int_{x_0}^x f_n'(t)\,dt$ converges uniformly to $\int_{x_0}^x g(t)\,dt$.

Let $N$ be such that for all $n \geq N$, $|g - f_n'| < \epsilon/(b - a)$. Then $$\bigg|\int_{x_0}^x g\,dt - \int_{x_0}^x f_n'\,dt\bigg| = \bigg|\int_{x_0}^x g - f_n'\,dt\bigg| \leq \int_{x_0}^x \bigg|g(t) - f_n'(t)\bigg|\,dt < \frac{\epsilon}{b - a}|x - x_0| \leq \epsilon$$ for all $n \geq N$. Because $\int_{x_0}^xf_n'(t)\,dt$ converges uniformly and $f_n(x_0) \rightarrow c$, their sum converges uniformly to $\int_{x_0}^xg(t)\,dt + c = f$. By continuity of uniform convergence of continuous functions, $g$ is continuous and $f' = g$ by FTOC.