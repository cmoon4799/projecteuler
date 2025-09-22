from algos import is_square
import math

# find values of n such that 5n**2 + 4n + 1 is a square


def solve(limit):

    x, m = 2, 1
    res = []
    for _ in range(limit):
        # one of these is divisible by 5
        if (-2 + x) % 5 == 0:
            b = (-2 + x)//5
        else:
            b = (-2 - x)//5

        if is_square(b**2 + (2*b + 1)**2):
            res.append((2*b + 1, b))
        else:
            res.append((2*b - 1, b))

        x, m = 9*x + 20*m, 4*x + 9*m

    return res


res = 0
for h, b in solve(13)[1:]:
    res += int(math.sqrt(h**2 + b**2))
print(res)
