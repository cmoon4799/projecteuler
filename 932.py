from sympy import factorint, mod_inverse
from itertools import chain, combinations
import math

# choose a, an n-digit number
# for its divisors, choose g | a such that if p | g then p^ord_a(p) | g
# that is, (g, a) = 1

# b'*g = 1 (mod a')
# suppose b' = k (mod a') -> b' = k + a'l
# choose l such that g*b' is an n-digit number
# verify that ab is 2025 number?


def solve(n):
    for a in range(10**(n - 1), 10**n):
        pf = factorint(a)

        # compute g
        for i in range(len(pf) + 1):
            g_primes = combinations(pf, i)
            for g_prime in g_primes:
                g = math.prod([p**pf[p] for p in g_prime])

                a_ = a//g
                g_inv = mod_inverse(g, a_) if a_ != 1 else 0  # residue of b_

                # b = g*(g_inv + a_*l) for some l
                # b must be an n-digit number
                lb = (10**(n - 1) - g*g_inv + g*a_)//(g*a_)
                for l in range(lb, 10**n):
                    b = g*(g_inv + a_*l)
                    if b < 10**(n - 1):
                        continue
                    if b >= 10**n:
                        break
                    if (10**n)*a + b == (a + b)**2:
                        print(a, b)


solve(8)


def solve(n):
    for a in range(10**(n - 1), 10**n):
        s = math.sqrt(4*(10**n - 1)*a + 1)
        if s**2 == a and (s - 2*a + 1) >= 0 and (s - 2*a + 1) % 2 == 0 and 10**(n - 1) <= (s - 2*a + 1)//2 < 10**n:
            print(a, (s - 2*a + 1)//2)
