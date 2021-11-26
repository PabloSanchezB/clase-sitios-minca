from pydantic import BaseSettings
from typing import Optional #Importamos tipos de datos
from functools import lru_cache #Nos permite hacer cache del archivo de configuracion para que siempre que lo
#utilicemos nos este haciendo peticiones

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1" #La version de la api que vamos a trabajar, que será la URI basica que todos los
    #servicios van a tener
    PROJECT_NAME: str = "Sitios en minca"
    POSTGRES_SERVER: str = "localhost" #La ruta donde esta el servidor de postgres
    POSTGRES_USER: str = "fastapi"
    POSTGRES_PASSWORD: str = "123123"
    POSTGRES_DB: str = "minca"
    SQLALCHEMY_DATABASE_URI: Optional[str] = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
    # La linea de arriba es la cadena de coneccion para conectarnos a postgres, el usuario y contraseña, el servidor 
    # y el nombre de la DB
    class Config:
        case_sensitive = True #Le decimos que sea case sensitive para que obligatoriamente sean mayusculas


@lru_cache #Creamos un cache sobre la peticion a los settings. El lru permite que una vez cargados los settings,
#ya no sea necesario llamarlos de nuevo, para asi no estar cargando los settings de la clase Settings todas las
#veces, es para optimizar la carga de los settings
def get_settings():
    return Settings()

settings = get_settings()


