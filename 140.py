import sympy as sp

def a(x):
    return (3*x**2 + x)/(1 - x - x**2)

print(sp.simplify(a((sp.sqrt(5) - 1)/4)))
print(sp.simplify(a(sp.Rational(2, 5))))
print(sp.simplify(a((sp.sqrt(22) - 2)/6)))


# fundamental solution to x^2 - 5y^2 = 1 is (9, 4)
# fundamental solution to x^2 - 5y^2 = -1 is (2, 1)


s1 = [(9, 4)]
t1 = [(8, 13)]
s2 = [(7, 1)]
t2 = [(1, 4)]
for _ in range(20):
    x = 9*s1[-1][0] + 5*4*s1[-1][1]
    y = 9*s1[-1][1] + 4*s1[-1][0]
    s1.append((x, y))
    t1.append((2*y, x + y))
    
    x = 9*s2[-1][0] + 5*4*s2[-1][1]
    y = 9*s2[-1][1] + 4*s2[-1][0]
    s2.append((x, y))
    if (x + y) % 2 == 0:
        t2.append((y, (x + y)//2))

res = []
for x, y in t1:
    print((x, y))
    print(sp.simplify(a(sp.Rational(x, y))))
    res.append(sp.simplify(a(sp.Rational(x, y))))

print("t2...")
for x, y in t2:
    print((x, y))
    assert x*x - 5*y*y == 44
    print(sp.simplify(a(sp.Rational(x, y))))
    res.append(sp.simplify(a(sp.Rational(x, y))))

res.sort()
for i, n in enumerate(res):
    print(i + 1, n)