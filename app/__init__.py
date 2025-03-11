import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv 

#Cargar las variables de entorno
load_dotenv()

#crear instancia
app =  Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Importar los modelos
from app.models import Repartidores


#Ruta Raiz
@app.route('/')
def index():
    repas = Repartidores.query.all()
    lista_repas = [{"id": repa.id, "nombre": repa.nombre, "placa_moto": repa.placa_moto, "imagen": repa.imagen} for repa in repas]
    return render_template('home.html', repas=lista_repas)