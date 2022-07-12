from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from Models import Vehiculo, ClienteTitular01, Vendedor01



class Controller:
    def __init__(self) -> None:
        engine = create_engine('sqlite:///C:\\Users\\User\\Desktop\\Grupo JAAP Development\\Grupo-JAAP-Development\\db_jaap\\db.db')
        
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def nuevo_vehiculo(self, 
            _vehic_chasis,
            _vehic_marca, 
            _vehic_modelo, 
            _vehic_anho,
            _vehic_tipo,
            _vehic_color,
            _vehic_combustible,
            _vehic_kilometraje,
            _vehic_estado):
            vehiculo = Vehiculo(
                vehic_chasis=_vehic_chasis,
                vehic_marca = _vehic_marca, 
                vehic_modelo = _vehic_modelo, 
                vehic_anho = _vehic_anho,
                vehic_tipo = _vehic_tipo,
                vehic_color = _vehic_color,
                vehic_combustible = _vehic_combustible,
                vehic_kilometraje = _vehic_kilometraje,
                vehic_estado = _vehic_estado
            )
            self.session.add(vehiculo)
            self.session.commit()

     
    
    
    
    
    )
