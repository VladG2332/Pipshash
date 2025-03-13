import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv 

# Cargar las variables de entorno
load_dotenv()

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db = SQLAlchemy(app)

# Importar modelos para que SQLAlchemy los reconozca
from app.models import Repartidores
from app.models import Pizzas
from app.models import Pedidos
from app.models import Orden


# Importar y registrar blueprints
from app.routes.repartidores import repartidores_bp
from app.routes.pizzas import pizzae_bp
from app.routes.pedidos import pedidos_bp

# Registrar blueprint
app.register_blueprint(repartidores_bp, url_prefix='/repartidores')
app.register_blueprint(pizzae_bp, url_prefix='/pipshash')
app.register_blueprint(pedidos_bp, url_prefix='/pedidos')

# Ruta principal

from app.routes.pizzas import pizzae_bp



#Ruta Raiz
@app.route('/')
def index():
    repas = Repartidores.query.all()
    lista_repas = [{"id": repa.id, "nombre": repa.nombre, "placa_moto": repa.placa_moto, "imagen": repa.imagen} for repa in repas]
    pizzas = Pizzas.query.all()
    lista_pizzas = [{"id": pizza.id, "nombre": pizza.nombre, "masa": pizza.masa, "queso": pizza.queso, "imagen": pizza.imagen} for pizza in pizzas]
    pedidos = Pedidos.query.all()
    ordenes = Orden.query.all()
    return render_template('home.html', repas=lista_repas, pizzas=lista_pizzas, pedidos=pedidos, ordenes=ordenes, repasl=repas)