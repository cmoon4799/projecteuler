import math

LIMIT = 150_000_000


def sieve(n):
    s = [0 for _ in range(n + 1)]

    p = []
    for i in range(2, n + 1):
        if s[i] == 0:
            p.append(i)
            if i * i <= n:
                for j in range(i * i, n + 1, i):
                    s[j] = i
    return p


p = sieve(LIMIT + 27)


def is_prime(n):
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


k = [1, 3, 7, 9, 13, 27]
k_ = [17, 19, 21, 23]

res = 0
for n in range(10, LIMIT, 10):
    if n % 3 == 0 or n % 7 == 0 or n % 13 == 0:
        continue
    if n % 11 in (2, 3, 8, 9):
        continue
    if all(is_prime(n**2 + c) for c in k) and all(not is_prime(n**2 + c) for c in k_):
        print(n)
        res += n

print(res)
