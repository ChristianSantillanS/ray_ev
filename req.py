import aiohttp
import asyncio
import requests
from strgen import StringGenerator
import time
import ray
#ray.init()
start_time = time.time()
@ray.remote
def fac(n):
    res = 1
    for i in range (1,n+1):
        res*= i
    return res
@ray.remote
def fib(n):
    if n<= 1:
        return n
    else: 
        return fib(n-1)+ fib(n-2)
#@ray.remote
def evaluacion_remota(entrada):
    r = requests.get('http://127.0.0.1:8000/evaluar/'+entrada)
    return r.content
##@ray.remote
def generar_operacion(dificultad):
    funcion=[0,0,0,0,0]
    funcion[0]= StringGenerator('[ ]|(fac)|(fib)').render()
    funcion[1]= StringGenerator('[1-9]{%s}' % dificultad).render()
    funcion[2]= StringGenerator('[+-*/]').render()
    funcion[3]= StringGenerator('[ ]|(fac)|(fib)').render()
    funcion[4]= StringGenerator('[1-9]{%s}' % dificultad).render()
    operacions=funcion[0]+'('+funcion[1]+')'+funcion[2]+funcion[3]+'('+funcion[4]+')'
    return operacions


##print(operacion,resultado)

evaluar = evaluacion_remota(generar_operacion(1))

async def main():
    resultados=[]
    async with aiohttp.ClientSession() as session:
        for _ in range(100):
            operacion=generar_operacion(1)
            resultado = evaluacion_remota(operacion)
            deploy_url = f'http://127.0.0.1:8000/evaluar/{operacion.lower()}'
            async with session.get(deploy_url) as resp:
                deploy_url = await resp.json()
                print(operacion)
                print(resultado)
                print('--------------------------------')
                resultados.append(resultado)
    print (resultados)
asyncio.run(main())
print("-Tardo-- %s segundos ---" % (time.time() - start_time))