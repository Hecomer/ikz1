import math
import numpy as np
import matplotlib.pyplot as plt


def function(x):
    return math.sqrt(1+x**2)+np.exp(-2*x)
    # return 3*x*math.sin(x)


def pamparam_method(func, a, b, tol=1e-4, max_iter=1000):
    n = 0
    while (b - a) / 2 > tol and n < max_iter:
        x1 = (a + b) / 2 - tol / 2
        x2 = (a + b) / 2 + tol / 2
        if func(x1) < func(x2):
            b = x2
        else:
            a = x1
        n += 1
    return (a + b) / 2


a = float(input("Enter a: "))
b = float(input("Enter b: "))

minimum = pamparam_method(function, a, b)
print("Метод деления отрезка пополам")
print("Минимум:", minimum)
print("Значение функции в минимуме:", function(minimum))
