from app import db

# Modelo Pedidos
class Pedidos(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True)
    orden_id = db.Column(db.Integer, db.ForeignKey('orden.id'), nullable=False)
    repartidor_id = db.Column(db.Integer, db.ForeignKey('repartidores.id'), nullable=False)
    pedidos = db.relationship('Orden', backref='pedido', lazy=True)
