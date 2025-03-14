from app import db

# Modelo Repartidores
class Pizzas(db.Model):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    masa = db.Column(db.String(200), nullable=False)
    queso = db.Column(db.Integer, nullable=False)
    imagen = db.Column(db.String(255), nullable=True)
    pizzas = db.relationship('Orden', backref='pizza', lazy=True)
