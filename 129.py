# from sympy import totient, factorint, n_order
# from math import sqrt, floor, gcd
# from concurrent.futures import ProcessPoolExecutor


# # find the order of 10 mod n
# def least_power(n):
#     m = totient(n)

#     for k in get_divisors(m):
#         if mod_exp(10, k, n) == 1:
#             return k


# def get_divisors(n):
#     factors = factorint(n)  # Get prime factorization as {p: exp}
#     divisors = {1}  # Start with 1

#     for p, exp in factors.items():
#         new_divisors = set()
#         for d in divisors:
#             for e in range(exp + 1):
#                 new_divisors.add(d * (p ** e))
#         divisors = new_divisors

#     return sorted(divisors)


# def mod_exp(a, m, n):
#     res = 1
#     a = a % n  # Ensure `a` is in range

#     while m > 0:
#         if m & 1:  # If `m` is odd, multiply `res` by `a`
#             res = (res * a) % n
#         a = (a * a) % n  # Square `a` and reduce mod `n`
#         m >>= 1  # Equivalent to `m //= 2`

#     return res


# # # Worker function for parallel processing
# # def check_least_power(i):
# #     if i % 2 == 0 or i % 5 == 0:
# #         return None  # Skip numbers divisible by 2 or 5

# #     result = least_power(i)
# #     print(i, result)
# #     if result > 10**6:
# #         print(result)
# #         return "STOP"  # Signal to break early

# #     return None

# # # Parallel execution


# def main():
#     # with ProcessPoolExecutor() as executor:
#     #     for res in executor.map(check_least_power, range(3, 1000000)):
#     #         if res == "STOP":
#     #             break  # Stop if we exceed 10^6

#     i = 2
#     while True:
#         i += 1
#         if gcd(i, 10) != 1:
#             continue

#         val = n_order(10, i)
#         print(i, val)
#         if val >= 10**6:
#             print(i, val)
#             break


# if __name__ == "__main__":
#     main()


#
# Solution to Project Euler problem 129
# Copyright (c) Project Nayuki. All rights reserved.
#
# https://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
#

import itertools


# Let n >= 1 be arbitrary but assume that it is coprime with 10.
# We want to find the smallest k such that R(k) = 0 mod n, and we'll show that 1 <= k <= n.
#
# Let "the sequence" of n values be (R(1) mod n, R(2) mod n, R(3) mod n, ..., R(n) mod n).
# For the sake of contradiction, assume that none of the values in the sequence are 0.
#
# Each number in the sequence is an integer in the range [1, n).
# The range has n - 1 elements, but there are n elements in the sequence.
# Hence by the pigeonhole principle, there exist two distinct indexes
# in the sequence where the elements have the same value.
#
# Suppose the two distinct indexes (1-based) are i and j.
# So the two values in question are R(i) mod n and R(j) mod n.
# Suppose WLOG that j > i. Then clearly R(j) - R(i) = 0 mod n,
# and so R(j) - R(i) = 1...10...0 = R(j - i) * 10^i = 0 mod n.
#
# Since 10 is coprime with n, 10 (and its powers) are invertible modulo n.
# Multiply everything in the equation by 10^-i, and we get R(j - i) = 1...1 = 0 mod n.
#
# We know 1 <= j - i <= n - 1. Then R(i - j) mod n, which is 0, is in the sequence.
# This contradicts our assumption that none of (R(1), R(2), ... R(n)) is 0 mod n.
#
# Therefore if we want to find an n whose solution k is such that
# k > 1000000, then we need to have n > 1000000.
def compute():
    LIMIT = 10**6
    for n in itertools.count(LIMIT):
        if least_divisible_repunit(n) > LIMIT:
            return str(n)


# Returns the smallest k such that R(k) is divisible by n.
def least_divisible_repunit(n):
    if n % 2 == 0 or n % 5 == 0:
        return 0
    k = 1
    s = 1  # Loop invariant: Equal to R(k) mod n
    p = 1  # Loop invariant: Equal to 10^k mod n
    while s % n != 0:
        k += 1
        p = p * 10 % n
        s = (s + p) % n
    return k


if __name__ == "__main__":
    print(compute())
