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


def is_prime(n):
    """Deterministic Miller-Rabin. For a given n, if n is prime then
    a**(n - 1) = 1 (mod n). However, there are Fermat pseudoprimes that
    satisfy this equality. If a**d != -1 then a**(d*k) must be -1 for some
    k in the chain. If a**(d*k) = -1 for some k, this alone is not sufficient
    for primality, but for 64-bit integers, there is a deterministic set of bases
    for which this test indicates primality."""
    if n < 2:
        return False

    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small_primes:
        if n % p == 0:
            return n == p

    # write n - 1 = d * 2^s with d odd
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    # deterministic for 64-bit integers
    for a in (2, 3, 5, 7, 11, 13, 17):
        if a >= n:
            continue

        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False

    return True


# parametrization of pythagorean triples
# for m, n coprime and not both odd, a = m^2 - n^2, b = 2mn, c = m^2 + n^2
def p_triple(m, n):
    assert (math.gcd(m, n) == 1)
    assert ((m % 2) * (n % 2) != 1)

    return (m**2 - n**2, 2*m*n, m**2 + n**2)
