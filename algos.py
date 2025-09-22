import math
from functools import lru_cache


@lru_cache
def fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b

    a, b = a, b
    for i in range(n):
        a, b = b, a + b
    return a


def is_cube(n):
    if n < 0:
        return round(abs(n) ** (1 / 3)) ** 3 == abs(n)
    return round(n ** (1 / 3)) ** 3 == n


def is_square(n: int) -> bool:
    if n < 0:
        return False
    root = math.isqrt(n)
    return root * root == n


def sieve(n):
    s = [0 for _ in range(n + 1)]

    p = []
    for i in range(2, n + 1):
        if s[i] == 0:
            p.append(i)
            for j in range(1, n // i + 1):
                s[i * j] = i

    return p


# parametrization of pythagorean triples
# for m, n coprime and not both odd, a = m^2 - n^2, b = 2mn, c = m^2 + n^2
def p_triple(m, n):
    assert (math.gcd(m, n) == 1)
    assert ((m % 2) * (n % 2) != 1)

    return (m**2 - n**2, 2*m*n, m**2 + n**2)
