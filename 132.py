from algos import sieve
from sympy.ntheory.residue_ntheory import n_order


primes = sieve(1_000_000)

# determine if p is a factor of R(N)


def valid(p, N):
    if p == 2 or p == 5:
        return False
    return N % n_order(10, p) == 0


s = 10
for p in primes[3:]:
    if p > 100_000:
        break
    o = n_order(10, p)
    # order must not have prime factors other than 2 or 5
    while o % 2 == 0:
        o //= 2
    while o % 5 == 0:
        o //= 5

    if o != 1:
        s += p
        print(p)

print(s)
