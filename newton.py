import numpy as np
import math


def function(x):
    # return math.sqrt(1+x**2)+np.exp(-2*x)
    return 3*x*math.sin(x)


def function1(x):
    # return x/(math.sqrt(1+x**2))-2/(np.exp(2*x))
    return 3*math.sin(x)+3*x*math.cos(x)


def function2(x):
    # return 1/(math.sqrt(1+x**2)*(1+x**2))+4/(np.exp(2*x))
    return 6 * math.cos(x) - 3 * x * math.sin(x)


def Newton_method(a, b, eps):
    x = (b - a) / 2.0  # начальное приближение
    while abs(function1(x)) > eps:  # теорема о сходимости
        x = x - (function1(x) / function2(x))  # xn+1 = xn - ...
    return x


# Начальные значения
a = float(input("Enter a: "))
b = float(input("Enter b: "))
eps = 1e-6  # Точность

# Выполнение метода Ньютона
x_min = Newton_method(a, b, eps)

print("Метод Ньютона")
print("Минимум:", x_min)
print("Значение функции в минимуме:", function(x_min))
