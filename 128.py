from bisect import bisect_right

BN = 10000000
prime_sieve = [0 for _ in range(BN)]
primes = set()
for i in range(2, BN):
    if prime_sieve[i] == 0:
        primes.add(i)
        for j in range(1, BN//i):
            prime_sieve[i*j] = i

print(sorted(list(primes))[:10])

# determine ring base


def rb_(n):
    return 3*n**2 - 3*n + 2

# solve 3n2 - 3n + 2 - k = 0


rb = [rb_(i) for i in range(5000000)]
rb[0] = 1

# determine neighbors of k
# 1. determine the ring base of k


def find_neighbors(n):
    if n == 1:
        return [2, 3, 4, 5, 6, 7]

    # ring base of n, binary search on rb_
    i = bisect_right(rb, n) - 1  # ring level
    base = rb[i]

    j = (n - base)//i  # corner number: n is between corners j and j + 1
    k = n - base - j*i  # distance from corner

    # print(base, i, j, k)
    # print(rb[i + 1])
    # non corner hexagon
    neighbors = []

    if k == 0:
        # non-top corner
        if j > 0:
            neighbors.extend(
                [rb[i + 1] + j*(i + 1) - 1, rb[i + 1] + j*(i + 1), rb[i + 1] + j*(i + 1) + 1])
            neighbors.extend([n - 1, n + 1])
            neighbors.extend([rb[i - 1] + j*(i - 1)])

        # top corner
        else:
            neighbors.extend([n + 1, rb[i + 1] - 1])
            neighbors.extend([rb[i + 1], rb[i + 1] + 1, rb[i + 2] - 1])
            neighbors.append(rb[i - 1])

    elif n == rb[i + 1] - 1:
        neighbors.extend([rb[i], n - 1])
        neighbors.extend([rb[i - 1], rb[i] - 1])
        neighbors.extend([rb[i + 2] - 1, rb[i + 2] - 2])

    else:
        neighbors.extend([rb[i - 1] + j*(i - 1) + k,
                          rb[i - 1] + j*(i - 1) + k - 1])
        neighbors.extend([rb[i + 1] + j*(i + 1) + k,
                          rb[i + 1] + j*(i + 1) + k + 1])
        neighbors.extend([n - 1, n + 1])

    return neighbors


def pd(n):
    neighbors = find_neighbors(n)
    p = 0
    for i in neighbors:
        if abs(i - n) in primes:
            p += 1
    return p


print(rb[:10])

print(find_neighbors(17), pd(17))

c = 0
for i in range(1, 10**9):
    if pd(rb[i] - 1) == 3:
        c += 1
        print(rb[i] - 1, c)
        if c == 2000:
            break
    if pd(rb[i]) == 3:
        c += 1
        print(rb[i], c)
        if c == 2000:
            break
