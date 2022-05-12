import ray
import requests
from ray import serve
ray.init()
serve.start()
def fact(n):
    res = 1
    for i in range(1,n+1):
        res*= i
        return res
def fib(n):
    if n<= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
def div(a,b):
    return a/b
@serve.deployment
def evaluar(entrada):
    print(entrada.url.path)
    op = entrada.url.path.split("/")[-1]
    return eval(op)
evaluar.deploy()

eval('2+4+fac(5)' )
eval('2*7+fib(5)' )

