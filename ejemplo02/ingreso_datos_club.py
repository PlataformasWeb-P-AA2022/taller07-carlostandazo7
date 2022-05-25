#3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Club, Jugador #1
from configuracion import cadena_base_datos #2
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos) #4

#5
Session = sessionmaker(bind=engine)
session = Session()

# lectura de datos_club 

archivoClub = open("data/datos_clubs.txt", "r")

registrosC = archivoClub.readlines();

for r in registrosC:
    nombre = r.split(";")[0]
    deporte = r.split(";")[1]
    fundacion = r.split(";")[2].replace("\n", "")
    print(nombre)
    print(deporte)
    print(fundacion)
    c = Club(nombre=nombre, deporte=deporte, fundacion=fundacion)
    session.add(c)

# se confirma las transacciones
session.commit()
