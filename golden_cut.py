import math
import numpy as np
import matplotlib.pyplot as plt


def function(x):
    # return math.sqrt(1+x**2)+np.exp(-2*x)
    return 3*x*math.sin(x)


def golden_section_method(a, b, eps=1e-6):
    golden_ratio = (math.sqrt(5) - 1) / 2

    x1 = b - golden_ratio * (b - a)
    x2 = a + golden_ratio * (b - a)
    f_x1 = function(x1)
    f_x2 = function(x2)

    while abs(b - a) > eps:
        if f_x1 < f_x2:
            b = x2
            x2 = x1
            x1 = b - golden_ratio * (b - a)
            f_x2 = f_x1
            f_x1 = function(x1)
        else:
            a = x1
            x1 = x2
            x2 = a + golden_ratio * (b - a)
            f_x1 = f_x2
            f_x2 = function(x2)

    return (a + b) / 2, function((a + b) / 2)


a = float(input("Enter a: "))
b = float(input("Enter b: "))
xmin, fmin = golden_section_method(a, b)
print("Метод золотого сечения")
print("Минимум: ", xmin)
print("Значение функции в минимуме: ", fmin)
