#Parece que aqui el profe esta poniendo lo que en la guia dice que va en el directorio models en
# el archivo place.py

from sqlalchemy import Column, Integer, String
#tipos de datos de sqlalchemy
from app.database.session import Base #Segun la guia, Base no esta en session, sino en otro modulo
#llamado base_class que no hemos creado aqui

#Y con la clase Place creamos la entidad

class Place(Base): #Modelo de los sitios turisticos de Minca. Al heredar de Base, indica que Place debe 
    #traducirse a una tabla del modelo relacional
    __tablename__ = "places" #Nombre de la tabla a nivel de base de datos (en plural)
    id = Column(Integer, primary_key=True, index=True) #index indica que se va a indexar para que las
    #busquedas sean mas rapidas
    name = Column(String, index=True)
    description = Column(String, index=True) #En la guia esta este index, pero no en lo que hizo el profe en la
    #clase.....
    image = Column(String)

