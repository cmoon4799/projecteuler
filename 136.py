from algos import sieve
import math

N = 50_000_000
primes = sieve(N)

res = 2
for p in primes[1:]:
    k0 = math.floor(math.log2(N/p))
    for k in range(k0 + 1):
        if k == 0 and (p % 4 != 3):
            continue
        if k == 1 or k == 3:
            continue
        if k > 4:
            e = 4
            f = 2**(k - 2)*p
            if f > 4*e/3:
                break
            else:
                res += 1
        else:
            res += 1

print(res)
