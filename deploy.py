import requests
import ray
from strgen import StringGenerator
from ray import serve
from starlette.requests import Request
from starlette.responses import Response
ray.init()
serve.start()
def fac(n):
    res = 1
    for i in range (1,n+1):
        res*= i
    return res
def fib(n):
    if n<= 1:
        return n
    else: 
        return fib(n-1)+ fib(n-2)
eval('2+4+fac(5)' )
@serve.deployment
def evaluar(request):
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
    operacion = request.url.path.split("evaluar/")[-1]
    return eval(operacion)
evaluar.deploy()
def evaluacion_remota(entrada):
    r = requests.get('http://127.0.0.1:8000/evaluar/'+entrada)
    return r.content
evaluacion_remota('2+2*6')
def generar_operacion(dificultad):
    funcion=[0,0,0,0,0]
    funcion[0]= StringGenerator('[ ] |(fac)|(fib)').render()
    funcion[1]= StringGenerator('[1-9]{%s}' % dificultad).render()
    funcion[2]= StringGenerator('[+-*/%]').render()
    funcion[3]= StringGenerator('[ ]|(fac)|(fib)').render()
    funcion[4]= StringGenerator('[1-9]{%s}' % dificultad).render()
    operacions=funcion[0]+'('+funcion[1]+')'+funcion[2]+funcion[3]+'('+funcion[4]+')'
    return operacions
generar_operacion(3)
operacion=generar_operacion()
resultado = evaluacion_remota(operacion)
print(operacion,resultado)
evaluacion_remota(operacion=generar_operacion())