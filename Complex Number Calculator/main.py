class C:
    def __init__(s, r, i):
        s.r = r
        s.i = i

    def __add__(a, b):
        return C(a.r + b.r, a.i + b.i)

    def __sub__(a, b):
        return C(a.r - b.r, a.i - b.i)

    def __mul__(a, b):
        r = a.r * b.r - a.i * b.i
        i = a.r * b.i + a.i * b.r
        return C(r, i)

    def __truediv__(a, b):
        d = b.r**2 + b.i**2
        r = (a.r * b.r + a.i * b.i) / d
        i = (a.i * b.r - a.r * b.i) / d
        return C(r, i)

    def __str__(s):
        if s.i < 0:
            return f"{s.r}{s.i}i"
        return f"{s.r}+{s.i}i"

a = C(float(input("a real: ")), float(input("a imag: ")))
b = C(float(input("b real: ")), float(input("b imag: ")))

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
