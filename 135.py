

def f(a, z):
    return 2*a*z + 3*a**2 - z**2


c = {i: [] for i in range(1_000_000)}

N = 500_000
for z in range(N):
    print("z: ", z)
    for a in range(z//3, N):
        v = f(a, z)
        if v < 0:
            continue
        if v >= N:
            # print("breaking v: ", v)
            break
        c[v].append((a, z))

res = 0
for i in range(N):
    if len(c[i]) == 10:
        if res < 100:
            print(c[i])
        res += 1

print(res)
