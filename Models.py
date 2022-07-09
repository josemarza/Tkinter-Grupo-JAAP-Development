from sqlalchemy import create_engine, Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Boolean

Base = declarative_base()

# Creamos la tabla de vendedor 01
class Vendedor01(Base):
    __tablename__ = 'vendedor_01'
    vend1_id = Column(Integer, primary_key=True)
    vend1_ci = Column(String(10), nullable=False)
    vend1_nombre_apellido = Column(String(80), nullable=False)
    vend1_direccion = Column(String(120), nullable=False)
    vend1_telefono = Column(String(15), nullable=False)
    vend1_email = Column(String(50))
    def __repr__(self) -> str:
        return f"Cliente Titular 01: { self.vend1_id}" 

# Creamos la tabla de vendedor 02
class Vendedor02(Base):
    __tablename__ = 'vendedor_02'
    vend2_id = Column(Integer, primary_key=True)
    vend2_ci = Column(String(10), nullable=False)
    vend2_nombre_apellido = Column(String(80), nullable=False)
    vend2_direccion = Column(String(120), nullable=False)
    vend2_telefono = Column(String(15), nullable=False)
    vend2_email = Column(String(50))
    def __repr__(self) -> str:
        return f"Cliente Titular 01: { self.vend2_id}" 

# Creamos la tabla de cliente titular 01
class ClienteTitular01(Base):
    __tablename__ = 'cliente_titular_01'
    ct1_id = Column(Integer, primary_key=True)
    ct1_ci = Column(String(10), nullable=False)
    ct1_nombre_apellido = Column(String(80), nullable=False)
    ct1_direccion = Column(String(120), nullable=False)
    ct1_telefono = Column(String(15), nullable=False)
    ct1_email = Column(String(50))
    def __repr__(self) -> str:
        return f"Cliente Titular 01: { self.ct1_id}" 

class ClienteTitular02(Base):
    __tablename__ = 'cliente_titular_02'
    ct2_id = Column(Integer, primary_key=True)
    ct2_ci = Column(String(10), nullable=False)
    ct2_nombre_apellido = Column(String(80), nullable=False)
    ct2_direccion = Column(String(120), nullable=False)
    ct2_telefono = Column(String(15), nullable=False)
    ct2_email = Column(String(50))
    def __repr__(self) -> str:
        return f"Cliente Titular 02: { self.ct2_id}" 

class Codeudor01(Base):
    __tablename__ = 'codeudor_01'
    cd1_id = Column(Integer, primary_key=True)
    cd1_ci = Column(String(10), nullable=False)
    cd1_nombre_apellido = Column(String(80), nullable=False)
    cd1_direccion = Column(String(120), nullable=False)
    cd1_telefono = Column(String(15), nullable=False)
    cd1_email = Column(String(50))
    def __repr__(self) -> str:
        return f"Codeudor 01: { self.cd1_id}"
 
class Codeudor02(Base):
    __tablename__ = 'codeudor_02'
    cd2_id = Column(Integer, primary_key=True)
    cd2_ci = Column(String(10), nullable=False)
    cd2_nombre_apellido = Column(String(80), nullable=False)
    cd2_direccion = Column(String(120), nullable=False)
    cd2_telefono = Column(String(15), nullable=False)
    cd2_email = Column(String(50))
    def __repr__(self) -> str:
        return f"Codeudor 02: { self.cd2_id}"

class Codeudor03(Base):
    __tablename__ = 'codeudor_03'
    cd3_id = Column(Integer, primary_key=True)
    cd3_ci = Column(String(10), nullable=False)
    cd3_nombre_apellido = Column(String(80), nullable=False)
    cd3_direccion = Column(String(120), nullable=False)
    cd3_telefono = Column(String(15), nullable=False)
    cd3_email = Column(String(50))
    def __repr__(self) -> str:
        return f"Codeudor 02: { self.cd3_id}"

class Vehiculo(Base):
    __tablename__ = 'vehiculo'
    vehic_id = Column(Integer, primary_key=True)
    vehic_chasis = Column(String(17), nullable=False)
    vehic_marca = Column(String(20), nullable=False)
    vehic_modelo = Column(String(20), nullable=False)
    vehic_anho = Column(Integer, nullable=False)
    vehic_tipo = Column(String(20), nullable=False)
    vehic_color = Column(String(20))
    vehic_combustible = Column(String(20))
    vehic_kilometraje = Column(Integer)
    vehic_estado = Column(String(20))
    def __repr__(self) -> str:
        return f"Codeudor 02: { self.vehic_id}"

class PlanDePago(Base):
    __tablename__ = 'plan_de_pago'
    plan_pago_id = Column(Integer, primary_key=True)
    plan_pago_entrega = Column(Integer, nullable=False)
    plan_pago_cant_cuotas = Column(Integer, nullable=False)
    plan_pago_monto_cuota = Column(Integer, nullable=False)
    plan_pago_cant_refuerzos = Column(Integer, nullable=False)
    plan_pago_monto_refuerzos = Column(Integer, nullable=False)
    plan_pago_id_vehic = Column(Integer, ForeignKey("vehiculo.vehic_id", ondelete="CASCADE"))
    def __repr__(self) -> str:
        return f"Codeudor 02: { self.plan_pago_id}"

if __name__ == '__main__':
    engine = create_engine('sqlite:///C:\\Users\\User\\Desktop\\Grupo JAAP Development\\Grupo-JAAP-Development\\db_jaap\\db.db', echo=True)
    Base.metadata.create_all(engine)

