import numpy as np
import math


def function(x):
    # return math.sqrt(1+x**2)+np.exp(-2*x)
    return 3*x*math.sin(x)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_method(a, b, n, i):
    i += 1  # текущий номер итерации
    if i > n:
        return (a + b) / 2.0  # количество заданных итераций превышено, возвращаем середину получившегося отрезка

    x1 = a + (b - a) * fibonacci(n - i) / fibonacci(n - i + 2)  # значения x1 на текущем шаге
    x2 = a + (b - a) * fibonacci(n - i + 1) / fibonacci(n - i + 2)
    fx1 = function(x1)
    fx2 = function(x2)

    if fx1 <= fx2:
        return fibonacci_method(a, x2, n, i)  # вызываем метод на левой части отрезка
    else:
        return fibonacci_method(x1, b, n, i)  # вызываем метод на правой части отрезка

# Запрос ввода пользователем
a = float(input("Введите a: "))
b = float(input("Введите b: "))
n = int(input("Введите количество итераций: "))
i = 0  # начальное значение номера итерации
minimum = fibonacci_method(a, b, n, i)
print("Метод Фибоначчи")
print("Минимум:", minimum)
print("Значение функции в минимуме:", function(minimum))
