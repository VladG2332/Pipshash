from app import db

# Modelo Pizzas
class Pizzas(db.Model):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    masa = db.Column(db.Text, nullable=False)
    queso = db.Column(db.Text, nullable=False)
    
    