#Aqui es donde se establece la conección a la base de datos
from sqlalchemy import create_engine #El create engine es el que hace a coneccion a la base de datos
from sqlalchemy.orm import sessionmaker #orm convierte a modelo relacional. El sessionmaker crea las sesiones
#de tipo orm
from sqlalchemy.ext.declarative import declarative_base #Creamos una clase que se decore con este 
#declarative_base y creamos las bases
from app.core.config import settings #Importamos nuestros settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
#Vemos que create_engine recibe como primer parametro la cadena de coneccion a la base de datos
#El pool pre ping hace un ping a la base de datos antes de establecer la conección
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Un objeto SessionLocal creado con la funcion sessionmaker. engine es la variable que acabamos de crear para
#crear la concección
Base = declarative_base()


