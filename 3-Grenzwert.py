"""Numerik Aufgabe 3"""
import math

def func(x):
    """Numerisch zu berechnende Funktion"""
    return (math.tan(x) - x) / x ** 3

for i in range(1, 10):
    print(func(10 ** -i))
