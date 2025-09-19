from algos import sieve
from sympy import mod_inverse


primes = sieve(1_001_000)


def valid(p1, p2):
    k = len(str(p1))
    it = mod_inverse(10, p2)
    it = it**k % p2

    r = -p1 * it % p2
    return r


s = 0
for i in range(1, len(primes)):
    p1 = primes[i]
    p2 = primes[i + 1]
    if p1 == 3:
        continue

    if p1 > 1_000_000:
        break

    t = p1 + 10**len(str(p1)) * valid(p1, p2)
    print(p1, p2, t)
    s += t

print(s)
