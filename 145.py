res = 68720  # those under 10**8

# 8 digit numbers
# d1 d2 d3 d4 d5 d6 d7 d8
# d8 d7 d6 d5 d4 d3 d2 d1
# d1 + d8 < 10
# d2 + d7 < 10
# d3 + d6 < 10
# d4 + d5 < 10


pairs = set()
for i in range(10):
    for j in range(10):
        if i + j < 10 and (i + j) % 2 == 1:
            pairs.add((i, j))

# d1, d8 can be any of the pairs except for those with 0s, i.e.
# (0, 1), (0, 3), (0, 5), (0, 7), (0, 9)
# (9, 0), (7, 0), (5, 0), (3, 0), (1, 0)
res += (len(pairs) - 10) * len(pairs) * len(pairs) * len(pairs)

print(res)
