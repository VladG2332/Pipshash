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
from app.models import Repartidor

# Importar y registrar blueprints
from app.routes.repartidores import repartidores_bp

# Registrar blueprint
app.register_blueprint(repartidores_bp, url_prefix='/repartidores')

# Ruta principal
@app.route('/')
def index():
    return render_template('home.html')