# from collections import Counter
# from math import sqrt, floor, ceil


# def cover(w, l, h, k):
#     return (k - 1)*4*(l + w + h) + 2*(l*w + w*h + l*h) + (k - 1)*(k - 2)*4


# ubg = 18000


# # def C(n):
# #     matches = 0
# #     # for k == 1
# #     # number of solutions to 2*(l*w + w*h + l*h) = n
# #     for w in range(1, n//4 + 1):
# #         for l in range(w, (n//2 - w + 1)//2 + 1):
# #             h = (n//2 - l*w)/(l + w)
# #             if h == floor(h) and l <= h:
# #                 matches += 1

# #     # for k == 2
# #     # number of solutions to 4(l + w + h) + 2*(l*w + w*h + l*h) = n
# #     for w in range(1, n//4 + 1):
# #         for l in range(w, (n//2 - w + 1)//2 + 1):
# #             h = (n - 2*l*w - 4*l - 4*w)/(4 + 2*(l + w))
# #             if h == floor(h) and l <= h:
# #                 matches += 1

# #     # for w in range(1, n//4 + 1):
# #     #     for l in range(w, (n//2 - w + 1)//2 + 1):
# #     #         h = (-2*l*(w + 4) + n - 8*(w + 3))/(2*(l + w + 4))
# #     #         if h == floor(h) and l <= h:
# #     #             matches += 1

# #     for k in range(3, 100):
# #         lb = sqrt(3/2)*sqrt(n + 2*k**2 - 2) - 3*(k - 1)
# #         ub = (n - 4*(k - 1)*(k - 2) - 6) / \
# #             (4*(k - 1)) if k != 1 else n

# #         lb = max(ceil(lb), 3)
# #         ub = min(floor(ub), n)

# #         print("lb, ub: ", lb, ub)
# #         if ub < 0 or lb > ub:
# #             break
# #         for s in range(lb, ub + 1):
# #             p = (n - (k - 1)*(k - 2)*4 - (k - 1)*4*s)/2
# #             for w in range(1, s//3 + 1):
# #                 for l in range(w, (s - w)//2 + 1):
# #                     h = s - w - l
# #                     h_ = (p - l*w)/(l + w)
# #                     if h == h_:
# #                         matches += 1
# #     return matches


# def C(n):
#     count = 0
#     max_dim = 100  # You may need to increase this later
#     for w in range(1, max_dim):
#         for l in range(w, max_dim):
#             for h in range(l, max_dim):
#                 k = 1
#                 cubes = cover(w, l, h, k)
#                 while cubes <= n:
#                     if cubes == n:
#                         count += 1
#                     k += 1
#                     cubes = cover(w, l, h, k)
#     return count


# print(C(22), C(46), C(78), C(118), C(154))
# n = 10
# while True:
#     print(n, C(n))
#     if C(n) == 1000:
#         break
#     n += 1

from collections import defaultdict


def cover(w, l, h, k):
    return 2 * (w*l + l*h + h*w) + 4 * (k - 1) * (w + l + h) + 4 * (k - 1) * (k - 2)


def find_least_n(target):
    counts = defaultdict(int)
    max_dim = 10000  # tune this
    max_layers = 200  # tune this

    for w in range(1, max_dim):
        for l in range(w, max_dim):
            for h in range(l, max_dim):
                for k in range(1, max_layers):
                    n = cover(w, l, h, k)
                    if n > 20000:  # you can tune this bound upward as needed
                        break
                    counts[n] += 1

    for n in sorted(counts):
        if counts[n] == target:
            return n


print(find_least_n(1000))
