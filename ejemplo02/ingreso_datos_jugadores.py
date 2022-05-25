from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Club, Jugador
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

archivoJugador = open("data/datos_jugadores.txt", "r")

registrosJ = archivoJugador.readlines();

for r2 in registrosJ:
        club_id = r2.split(";")[0]
        posicion = r2.split(";")[1]
        dorsal = r2.split(";")[2]
        nombre = r2.split(";")[3]
        print(club_id)
        print(posicion)
        print(dorsal)
        print(nombre)
        j = Jugador(club_id=club_id, posicion=posicion, dorsal=dorsal, nombre=nombre)
        session.add(j)
        
session.commit()

