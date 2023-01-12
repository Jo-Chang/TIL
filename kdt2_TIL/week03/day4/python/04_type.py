def f(x, y):
    return x + y

def g(x: int, y: int) -> int:
    return x + y

f(1, 2)
g(1, 2)

def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
    
f(1, 2, 3, 4, e = 5, f = 6)