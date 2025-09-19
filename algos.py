def is_cube(n):
    if n < 0:
        return round(abs(n) ** (1/3)) ** 3 == abs(n)
    return round(n ** (1/3)) ** 3 == n


def sieve(n):
    s = [0 for _ in range(n + 1)]

    p = []
    for i in range(2, n + 1):
        if s[i] == 0:
            p.append(i)
            for j in range(1, n//i + 1):
                s[i*j] = i

    return p
