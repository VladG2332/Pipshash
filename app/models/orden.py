from app import db

# Modelo Orden
class Orden(db.Model):
    __tablename__ = 'orden'
    id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    pizzas = db.relationship('Pizzas', backref='pizza', lazy=True)