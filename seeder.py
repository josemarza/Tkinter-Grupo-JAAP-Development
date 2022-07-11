from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from Models import Vehiculo, ClienteTitular01, Vendedor01

if __name__ == "__main__":
    engine = create_engine('sqlite:///C:\\Users\\User\\Desktop\\Grupo JAAP Development\\Grupo-JAAP-Development\\db_jaap\\db.db')
    Session = sessionmaker(bind=engine)
    session=Session()

    vehiculo = Vehiculo(
            vehic_chasis = 'BU306-0004076123456789',
            vehic_marca = 'Toyota',
            vehic_modelo = 'Toyoace',
            vehic_anho = '2001',
            vehic_tipo = 'Furgon Carguero',            
            vehic_color = 'Blanco',
            vehic_combustible = 'Gasoil',            
            vehic_kilometraje = 360000,
            vehic_estado = 'Usado, recién importado'
        )
    session.add(vehiculo)
    session.commit()
