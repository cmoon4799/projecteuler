from algos import is_cube, sieve


primes = sieve(1_000_000)
primes = set(primes)
res = 0
for m in range(1, 1_000_000):
    p = (3*m**2 + 3*m + 1)
    if p in primes:
        n = m**3
        print(n, p)
        res += 1
        continue

print(res)
