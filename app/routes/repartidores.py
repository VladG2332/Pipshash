import os
from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app import db
from app.models import Repartidores  # Cambio aquí

repartidores_bp = Blueprint('repartidores', __name__)

UPLOAD_FOLDER = 'app/static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Ruta para ver todos los repartidores
@repartidores_bp.route('/')
def listar_repartidores():
    repartidores = Repartidores.query.all()
    return render_template('repartidores/listar_repartidores.html', repartidores=repartidores)

# Ruta para crear un nuevo repartidor
@repartidores_bp.route('/repartidores/new', methods=['GET', 'POST'])
def add_repartidor():
    if request.method == 'POST':
        nombre = request.form['nombre']
        placa_moto = request.form['placa_moto']
        capacidad = request.form['capacidad']

        # Verifica si se subió un archivo
        if 'imagen' not in request.files:
            return "No se ha seleccionado ningún archivo", 400

        file = request.files['imagen']

        # Si no se seleccionó un archivo, o el archivo está vacío
        if file.filename == '':
            return "No se ha seleccionado ningún archivo", 400

        # Validar tipo de archivo
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))  # Guarda la imagen en la carpeta

            # Guarda solo el nombre del archivo en la BD
            new_repa = Repartidores(nombre=nombre, placa_moto=placa_moto, capacidad=capacidad, imagen=filename)
            db.session.add(new_repa)
            db.session.commit()
        return redirect(url_for('repartidores.listar_repartidores'))

    return render_template('repartidores/create_repartidor.html')

# Actualizar repartidor
@repartidores_bp.route('/repartidores/update/<int:id>', methods=['GET', 'POST'])
def update_repartidor(id):
    repartidor = Repartidores.query.get(id)
    if request.method == 'POST':
        repartidor.nombre = request.form['nombre']
        repartidor.placa_moto = request.form['placa_moto']
        repartidor.capacidad = request.form['capacidad']
        
        db.session.commit()
        return redirect(url_for('repartidores.listar_repartidores'))
    
    return render_template('repartidores/update_repartidor.html', repartidor=repartidor)

# Eliminar repartidor
@repartidores_bp.route('/repartidores/delete/<int:id>')
def delete_repartidor(id):
    repartidor = Repartidores.query.get(id)
    if repartidor:
        db.session.delete(repartidor)
        db.session.commit()
    return redirect(url_for('repartidores.listar_repartidores'))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
