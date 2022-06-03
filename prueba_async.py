import argparse
import aiohttp
import asyncio
import requests
from strgen import StringGenerator
import time
import ray

    
def generar_operacion(dificultad):
    funcion=[0,0,0,0,0]
    funcion[0]= StringGenerator('[ ]|(fac)|(fib)').render()
    funcion[1]= StringGenerator('[1-9]{%s}' % dificultad).render()
    funcion[2]= StringGenerator('[+-*/]').render()
    funcion[3]= StringGenerator('[ ]|(fac)|(fib)').render()
    funcion[4]= StringGenerator('[1-9]{%s}' % dificultad).render()
    operacions=funcion[0]+'('+funcion[1]+')'+funcion[2]+funcion[3]+'('+funcion[4]+')'
    return operacions

async def pruebadecarga_async(num_operaciones=20,complejidad=1):
    resultados=[]
    operaciones=[]
    async with aiohttp.ClientSession() as session:
        for _ in range(num_operaciones):
            operacion=generar_operacion(complejidad)
            deploy_url = f'http://127.0.0.1:8000/evaluar/{operacion.lower()}'
            async with session.get(deploy_url) as resp:
                deploy_url = await resp.json()
                resultados.append(deploy_url)
                operaciones.append(operacion)


parser = argparse.ArgumentParser(description="Prueba asincrona de carga en ray serve")
parser.add_argument('operaciones', type=int, metavar='operaciones', nargs='?',
        default=100)
parser.add_argument('complejidad', type=int, metavar='complejidad', nargs='?',
        default=1)


# El siguiente chequeo revisa si el script esta corriendo en la consola.
if __name__ == '__main__':
    args = parser.parse_args()
    start_time = time.time()
    print('Corriendo %d operaciones de complejidad %d' % (args.operaciones, args.complejidad))
    asyncio.run(pruebadecarga_async(num_operaciones=args.operaciones, complejidad=args.complejidad))

    print("-Tardo-- %s segundos ---" % (time.time() - start_time))

