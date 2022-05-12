import requests

from pyrsistent import b
def sum(a, b):
    for n in (a, b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError
    return a + b
def res(a,b):
    for n in (a, b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError
    return a - b
def multip(a, b):
    for n in (a, b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError
    return a * b
def div(a, b):
    for n in (a, b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError
    return a / b
def expon(a, b):
    for n in (a, b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError
    return a ** b
def fact(a):
    for n in (a,):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError
    return math.factorial(a) 