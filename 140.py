import sympy as sp

def a(x):
    return (3*x**2 + x)/(1 - x - x**2)

print(sp.simplify(a((sp.sqrt(5) - 1)/4)))
print(sp.simplify(a(sp.Rational(2, 5))))
print(sp.simplify(a((sp.sqrt(22) - 2)/6)))


# fundamental solution to x^2 - 5y^2 = 1 is (9, 4)
# fundamental solution to x^2 - 5y^2 = -1 is (2, 1)

# 3/9/26: must try negative solutions too...

s1 = [(9, 4)]
t1 = [(8, 13)] # 4
s2 = [(7, 1)]
t2 = [(1, 4)] # 44
s3 = [(8, 2)]
t3 = [(2, 5)] # 44
s4 = [(3, 1)]
t4 = [(1, 2)] # 4
s5 = [(2, 0)]
t5 = [(0, 1)] # 4
s6 = [(7, 3)]
t6 = [(3, 5)]
s7 = [(13, 5)]
t7 = [(5, 9)]
s8 = [(17, 7)]
t8 = [(7, 12)]
s9 = [(32, 14)]
t9 = [(14, 23)]


for _ in range(20):
    x = 9*s1[-1][0] + 5*4*s1[-1][1]
    y = 9*s1[-1][1] + 4*s1[-1][0]
    s1.append((x, y))
    t1.append((2*y, x + y))
    
    x = 9*s2[-1][0] + 5*4*s2[-1][1]
    y = 9*s2[-1][1] + 4*s2[-1][0]
    s2.append((x, y))
    s = y
    t = (x + y)//2
    if (x + y) % 2 == 0 and (3*s + t) % 11 == 0:
        t2.append((y, (x + y)//2))
        
    x = 9*s3[-1][0] + 5*4*s3[-1][1]
    y = 9*s3[-1][1] + 4*s3[-1][0]
    s3.append((x, y))
    s = y
    t = (x + y)//2
    if (x + y) % 2 == 0 and (3*s + t) % 11 == 0:
        t3.append((y, (x + y)//2))
    
    x = 9*s4[-1][0] + 5*4*s4[-1][1]
    y = 9*s4[-1][1] + 4*s4[-1][0]
    s4.append((x, y))
    t4.append((y, (x + y)//2))
    
    x = 9*s5[-1][0] + 5*4*s5[-1][1]
    y = 9*s5[-1][1] + 4*s5[-1][0]
    s5.append((x, y))
    t5.append((y, (x + y)//2))

    x = 9*s6[-1][0] + 5*4*s6[-1][1]
    y = 9*s6[-1][1] + 4*s6[-1][0]
    s6.append((x, y))
    t6.append((y, (x + y)//2))
    
    x = 9*s7[-1][0] + 5*4*s7[-1][1]
    y = 9*s7[-1][1] + 4*s7[-1][0]
    s7.append((x, y))
    s = y
    t = (x + y)//2
    if (x + y) % 2 == 0 and (3*s + t) % 11 == 0:
        t7.append((y, (x + y)//2))

    x = 9*s8[-1][0] + 5*4*s8[-1][1]
    y = 9*s8[-1][1] + 4*s8[-1][0]
    s8.append((x, y))
    s = y
    t = (x + y)//2
    if (x + y) % 2 == 0 and (3*s + t) % 11 == 0:
        t8.append((y, (x + y)//2))
    
    x = 9*s9[-1][0] + 5*4*s9[-1][1]
    y = 9*s9[-1][1] + 4*s9[-1][0]
    s9.append((x, y))
    s = y
    t = (x + y)//2
    if (x + y) % 2 == 0 and (3*s + t) % 11 == 0:
        t9.append((y, (x + y)//2))

res = []
for x, y in t1:
    print((x, y))
    print(sp.simplify(a(sp.Rational(x, y))))
    res.append(sp.simplify(a(sp.Rational(x, y))))

for x, y in t2:
    print((x, y))
    assert (2*y - x)**2 - 5*x**2 == 44
    print(sp.simplify(a(sp.Rational(x, y))))
    res.append(sp.simplify(a(sp.Rational(x, y))))

for x, y in t3:
    print((x, y))
    assert (2*y - x)**2 - 5*x**2 == 44
    print(sp.simplify(a(sp.Rational(x, y))))
    res.append(sp.simplify(a(sp.Rational(x, y))))
    
for i, (x, y) in enumerate(t4):
    print((x, y))
    print(s4[i])
    assert (2*y - x)**2 - 5*x**2 == 4
    print(sp.simplify(a(sp.Rational(x, y))))
    res.append(sp.simplify(a(sp.Rational(x, y))))

for i, (x, y) in enumerate(t5):
    print((x, y))
    print(s5[i])
    assert (2*y - x)**2 - 5*x**2 == 4
    print(sp.simplify(a(sp.Rational(x, y))))
    res.append(sp.simplify(a(sp.Rational(x, y))))

for i, (x, y) in enumerate(t6):
    print((x, y))
    print(s6[i])
    assert (2*y - x)**2 - 5*x**2 == 4
    print(sp.simplify(a(sp.Rational(x, y))))
    res.append(sp.simplify(a(sp.Rational(x, y))))

for i, (x, y) in enumerate(t7):
    print((x, y))
    print(s7[i])
    assert (2*y - x)**2 - 5*x**2 == 44
    print(sp.simplify(a(sp.Rational(x, y))))
    res.append(sp.simplify(a(sp.Rational(x, y))))

for i, (x, y) in enumerate(t8):
    print((x, y))
    print(s8[i])
    assert (2*y - x)**2 - 5*x**2 == 44
    print(sp.simplify(a(sp.Rational(x, y))))
    res.append(sp.simplify(a(sp.Rational(x, y))))

for i, (x, y) in enumerate(t9):
    print((x, y))
    print(s9[i])
    assert (2*y - x)**2 - 5*x**2 == 44
    print(sp.simplify(a(sp.Rational(x, y))))
    res.append(sp.simplify(a(sp.Rational(x, y))))

res = [x for x in sorted(set(res)) if int(x) == x]
for i, n in enumerate(res):
    print(i + 1, n)