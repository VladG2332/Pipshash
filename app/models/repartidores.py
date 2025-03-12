from app import db

# Modelo Repartidor
class Repartidor(db.Model):
    __tablename__ = 'repartidores'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(200), nullable=False)
    placa_moto = db.Column(db.String(20), nullable=False, unique=True)
    capacidad = db.Column(db.Integer, nullable=False)
