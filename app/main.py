from fastapi import FastAPI # Importamos fastapi
from fastapi.middleware.cors import CORSMiddleware # Para que pueda soportar peticiones cruzadas, que es cuando
# intento hacerle peticiones a mi app desde dominios diferentes

app = FastAPI() # Creamos la app

app.add_middleware( #Los middleware interceptan las peticiones que hago para hacerles ciertas validaciones
    CORSMiddleware,
    allow_origins=["http://localhost:8080"], #Cuando lo suba a la nube AQUI es donde debo poner el dominio o IP,
    #si no no funciona. Tenerlo en cuenta para lo del despliegue
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health-check/")
def health_check():
    return "OK"

#Con solo este archivo ya la app esta lista para probar (¿Seguro??)

