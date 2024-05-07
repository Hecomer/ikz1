import numpy as np
import math


def function(x):
    # return math.sqrt(1+x**2)+np.exp(-2*x)
    return 3*x*math.sin(x)


def broken_method(a, b, L, eps):
    x = (a + b) / 2.0
    p = (1.0 / 2) * (function(a) + function(b) + L * (a - b))
    delta = (1 / (2 * L)) * (function(a) - p)
    x1 = x - delta
    x2 = x + delta

    if 2 * L * delta < eps:
        if function(x1) < function(x2):
            return x1, function(x1)
        else:
            return x2, function(x2)
    else:
        p = (1 / 2.0) * (function(a) + function(b) + L * (a - b))
        xm1, pm1 = broken_method(a, x, L, eps)
        xm2, pm2 = broken_method(x, b, L, eps)

        if pm1 < pm2:
            return xm1, pm1
        else:
            return xm2, pm2

# Начальные значения
a = float(input("Enter a: "))
b = float(input("Enter b: "))
L = 10
eps = 1e-5

min_x, min_value = broken_method(a, b, L, eps)

print("Метод Ломанных")
print("Минимум:", min_x)
print("Значение функции в минимуме:", min_value)
