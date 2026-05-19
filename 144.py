def dp(a, b):
    return sum(x * y for x, y in zip(a, b))


def reflect(u, v):
    """Reflect vector u across vector v."""
    M = 2 * dp(u, v) / dp(v, v)
    return tuple(M * vi - ui for ui, vi in zip(u, v))


def intersect(x, y, u):
    """Determine the first point on the ellipse that the line emanating from (x, y)
    with direction u intersects"""
    a, b = u
    t = (-8*x*a - 2*y*b)/(4*a**2 + b**2)
    e = x + a*t
    f = y + b*t

    return (e, f)


def bounce(x, y, u):
    """Bounce from a point x, y on the ellipse with direction u"""

    e, f = intersect(x, y, u)
    v = (-u[0], -u[1])
    v = reflect(v, (4*e/f, 1))
    return (e, f, v)


# starting from (0, 10.1) to (1.4, -9.6)
x = 1.4
y = -9.6
u = (-1.4, 19.7)
u = reflect(u, (-7/12, 1))

bounces = 0
while not (-.01 <= x <= .01 and y > 0):
    x, y, u = bounce(x, y, u)
    bounces += 1
    print(x, y, u, bounces)

print(bounces)
