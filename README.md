# Introduccion

Esto es un proyecto de investigacion donde estudiamos la escalabilidad


## Probando el sistema

Para instalar todos los requerimientos del sistema:

```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

### Consola
Para probar el servidor en consola:

1. Correr `deploy.py`
2. Abrir el Ray Dashboard en http://localhost:8265
3. En una consola nueva correr `python prueba_sync.py` que realiza la prueba sincrona
3. En una consola nueva correr `python prueba_async.py` que realiza la prueba asincrona
4. Revisar utilizacion en el Ray Dashboard en ambos casos.

**Para detener el archivo deploy.py** puedes teclear `Ctrl+C` para interrumpir la ejecucion.

**Nota**: Los archivos `prueba_sync.py` y `prueba_async.py` pueden recibir parametros. Para
ver los parametros, correr:

```
python prueba_sync.py -h
python prueba_async.py -h
```

Esto imprimira la documentacion de los parametros.


### Notebook

**TODO: Escribir esta seccion**

1. Inicializar el Notebook de Jupyer `jupyter notebook`
2. Abrir `Deploy.ipynb`
3. Ejecutamos `RUN ALL`.
