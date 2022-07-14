import asyncio
import cProfile
import ray
from strgen import StringGenerator
from ray import serve
from starlette.requests import Request
from starlette.responses import Response
import requests
from strgen import StringGenerator
ray.init(num_cpus=8)

serve.start(RAY_IGNORE_UNHANDLED_ERRORS=1)

@serve.deployment(num_replicas=1)
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
    operacion = request.url.split("evaluar/")[-1]
    return eval(operacion)
evaluar.deploy()

handle= evaluar.get_handle(sync=False)
def generar_operacion(dificultad):
    funcion=[0,0,0,0,0]
    funcion[0]= StringGenerator('[ ]|(fac)|(fib)').render()
    funcion[1]= StringGenerator('[1-9]{%s}' % dificultad).render()
    funcion[2]= StringGenerator('[+-*/]').render()
    funcion[3]= StringGenerator('[ ]|(fac)|(fib)').render()
    funcion[4]= StringGenerator('[1-9]{%s}' % dificultad).render()
    operacions=funcion[0]+'('+funcion[1]+')'+funcion[2]+funcion[3]+'('+funcion[4]+')'
    return operacions

async def prueba_de_carga_sync(num_operaciones=20,complejidad=1):
    res=[]
    for _ in range(num_operaciones):
        op= generar_operacion(complejidad)
        #res.append(handle.remote(op))
        await handle.remote(op)
    #ray.get(res)
#asyncio.run(prueba_de_carga_sync(300))
    await prueba_de_carga_sync(300)


def main():
    ray.init()
    cProfile.run('prueba_de_carga_sync(num_operaciones=20,complejidad=1)')  # obtener tabla 2