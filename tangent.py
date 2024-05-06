import numpy as np
import math


def function(x):
    # return math.sqrt(1+x**2)+np.exp(-2*x)
    return 3*x*math.sin(x)


def function1(x):
    # return x/(math.sqrt(1+x**2))-2/(np.exp(2*x))
    return 3*math.sin(x)+3*x*math.cos(x)


def Tangent_method(a, b, eps):
    x = a
    while abs(function1(x)) > eps:
        if function1(a) * function1(b) >= 0:
            if ((function1(a) > 0 and function1(b) > 0) or function1(a) == 0):
                x = a  # xn+1 = an
            elif ((function1(a) < 0 and function1(b) < 0) or function1(b) == 0):
                x = b  # xn+1 = bn
        else:
            x = (b * function1(b) - a * function1(a) + function(a) - function(b)) / (function1(b) - function1(a))
        if function1(x) >= 0:
            b = x
        else:
            a = x
    return x

# Начальные значения
a = float(input("Enter a: "))
b = float(input("Enter b: "))
eps = 1e-4  # Точность

x_min = Tangent_method(a, b, eps)

print("Метод касательных")
print("Минимум:", x_min)
print("Значение функции в минимуме:", function(x_min))
