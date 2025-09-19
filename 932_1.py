import math


def solve_even(n):
    ans = 0
    n = n//2
    for a in range(10**(n - 1), 10**n):
        s = math.sqrt(4*(10**n - 1)*a + 1)
        k = int(s - 2*a + 1)
        b = k//2
        if s == int(s) and k >= 0 and k % 2 == 0 and 10**(n - 1) <= b < 10**n:
            ans += a*10**n + b
    return ans


def solve_odd(n):
    m = (n - 1)//2
    ans = 0
    # a is an m digit number, b is an m + 1 digit number
    for a in range(10**(m - 1), 10**m):
        s = math.sqrt(4*(10**(m + 1) - 1)*a + 1)
        k = int(s - 2*a + 1)
        b = k//2
        if s == int(s) and k >= 0 and k % 2 == 0 and 10**m <= b < 10**(m + 1):
            ans += a*10**(m + 1) + b

    # a is an m + 1 digit number, b is an m digit number
    for a in range(10**m, 10**(m + 1)):
        s = math.sqrt(4*(10**m - 1)*a + 1)
        k = int(s - 2*a + 1)
        b = k//2
        if s == int(s) and k >= 0 and k % 2 == 0 and 10**(m - 1) <= b < 10**m:
            ans += a*10**m + b

    return ans


# solving for n digit 2025-numbers
def solve(n):
    return solve_even(n) if n % 2 == 0 else solve_odd(n)


ans = 0
for n in range(2, 17):
    ans += solve(n)
    print(n, ans)
