import numpy as np
import math


def function(x):
    return math.sqrt(1+x**2)+np.exp(-2*x)
    # return 3*x*math.sin(x)


def fibonacci_method(a, b, epsilon, i=0):
    golden_ratio = (1 + np.sqrt(5)) / 2

    if abs(b - a) < epsilon:
        return (a + b) / 2.0, i

    x1 = b - (b - a) / golden_ratio
    x2 = a + (b - a) / golden_ratio
    fx1 = function(x1)
    fx2 = function(x2)

    if fx1 <= fx2:
        return fibonacci_method(a, x2, epsilon, i+1)
    else:
        return fibonacci_method(x1, b, epsilon, i+1)


a = float(input("Введите a: "))
b = float(input("Введите b: "))
epsilon = 1e-4
minimum, iterations = fibonacci_method(a, b, epsilon)
print("Метод Фибоначчи")
print("Минимум:", minimum)
print("Значение функции в минимуме:", function(minimum))
print("Количество итераций:", iterations)
