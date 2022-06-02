import requests
import ray
import time
from strgen import StringGenerator
from ray import serve
from starlette.requests import Request
from starlette.responses import Response
ray.init()
serve.start()

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
print('Probando...: %s' % evaluacion_remota('2+2*6'))

while True:
    time.sleep(30)
    print(serve.list_deployments())
