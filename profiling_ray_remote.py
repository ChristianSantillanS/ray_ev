import cProfile
import requests
import ray
import time
from strgen import StringGenerator
from ray import serve
from starlette.requests import Request
from starlette.responses import Response
def evaluar(op):
    def fib(n):
        if n<= 1:
            return n
        else: 
            return fib(n-1)+ fib(n-2)
    def fac(n):
        res = 1
        for i in range (1,n+1):
            res*= i
        return res
    operacion = op
    return eval(operacion)
def generar_operacion(dificultad):
    funcion=[0,0,0,0,0]
    funcion[0]= StringGenerator('[ ]|(fac)|(fib)').render()
    funcion[1]= StringGenerator('[1-9]{%s}' % dificultad).render()
    funcion[2]= StringGenerator('[+-*/]').render()
    funcion[3]= StringGenerator('[ ]|(fac)|(fib)').render()
    funcion[4]= StringGenerator('[1-9]{%s}' % dificultad).render()
    operacions=funcion[0]+'('+funcion[1]+')'+funcion[2]+funcion[3]+'('+funcion[4]+')'
    return operacions
@ray.remote
def ray_evaluador(op):
    return evaluar(op)
def prueba_de_carga_async_de_ray_remote():
    ray.get([ray_evaluador.remote(generar_operacion(1)) for _ in range(100)])

def main():
    ray.init()
    cProfile.run('prueba_de_carga_async_de_ray_remote()')  # obtener tabla 1
