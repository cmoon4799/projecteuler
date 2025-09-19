

# 136
We determined that n = (-x + 3a)(x + a). If we let e = (-x + 3a) and f = (x + a) then x = (3f - e)/4 and a = (e + f)/4. This implies e = -f (mod 4) and n must be 0 or 3 (mod 4).

For odd n, it is sufficient for n to be a prime 3 (mod 4). If n is not prime, let n = ef for e, f != 1. Then x, a defined as above is a suitable solution. Hence, it is necessary for n to be prime.

For even n, it must be that n = ef such that both e, f are 0 (mod 4) or 2 (mod 4). Suppose ord_n(2) >= 4. e = 4, f = n/4 is a suitable decomposition; for it to be the only such decomposition, it must be that f <= 4e/3.