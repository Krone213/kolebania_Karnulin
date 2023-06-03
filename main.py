import timeit
import mpmath


def M(b, zap):
    a = 1
    while mpmath.fabs(a - b) > mpmath.mpf(10) ** (-zap):
        a, b = (a + b) / 2, mpmath.sqrt(a * b)

    return (a + b) / 2


def riad(l, c, p):
    t = mpmath.pi * 2 * mpmath.sqrt(l / mpmath.mpf(9.81))
    s = mpmath.mpf(1)
    n = mpmath.mpf(0)
    sp = mpmath.mpf(-1)
    while True:
        n += 1
        s += (mpmath.power(mpmath.fac2(2 * n - 1) / mpmath.fac2(2 * n),2) ) * (mpmath.power((mpmath.sin(c / 2)), (2 * n)))
        if sp == s:
            return s * t
        sp = s


def toch(l, c, p):
    mpmath.mp.dps = p + 2
    mpmath.mp.pretty = True
    return (mpmath.pi * 2 / (M(mpmath.cos(c / 2), p))) * mpmath.sqrt(l / 9.81)


c = mpmath.mpf(input("Введите угол в радианах:"))
l = mpmath.mpf(input("Введите длину:"))
p = int(input("Введите точность:"))

print("Точная формула:")
start = timeit.default_timer()
print("Период =", toch(l, c, p), "с")
end = timeit.default_timer() - start
print("Время выполнения:", end, "с")

print("Через ряд:")
start = timeit.default_timer()
print("Период =", riad(l, c, p), "с")
end = timeit.default_timer() - start
print("Время выполнения:", end, "с")
