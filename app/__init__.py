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

<<<<<<< HEAD
# Importar modelos para que SQLAlchemy los reconozca
from app.models import Repartidor

# Importar y registrar blueprints
from app.routes.repartidores import repartidores_bp

# Registrar blueprint
app.register_blueprint(repartidores_bp, url_prefix='/repartidores')

# Ruta principal
=======
from app.models import Pizzas
from app.models import Repartidores
from app.routes.pizzas import pizzae_bp

app.register_blueprint(pizzae_bp, url_prefix='/pipshash')

#Ruta Raiz
>>>>>>> 0446d34c1c7947877db9dd3b805977db0791dfe6
@app.route('/')
def index():
    repas = Repartidores.query.all()
    lista_repas = [{"id": repa.id, "nombre": repa.nombre, "placa_moto": repa.placa_moto, "imagen": repa.imagen} for repa in repas]
    pizzas = Pizzas.query.all()
    lista_pizzas = [{"id": pizza.id, "nombre": pizza.nombre, "masa": pizza.masa, "queso": pizza.queso, "imagen": pizza.imagen} for pizza in pizzas]
    return render_template('home.html', repas=lista_repas, pizzas=lista_pizzas)