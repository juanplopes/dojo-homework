def euclid(a, b):
    if not b: return (a, 1L, 0L)
    q = a/b
    g, x, y = euclid(b, a-q*b)
    return (g, y, x-q*y)

def solve(a, b, c):
    g, x, y = euclid(a, b)
    if c%g: return None
    a, b, c = a/g, b/g, c/g
    x, y = x*c, y*c
    return min(abs(x%b*a*g), abs(y%a*b*g))

def miojo(t, a, b):
    return solve(a, -b, t)

if __name__ == '__main__':
    t, a, b = map(int, raw_input().split())
    print miojo(t, a, b)
