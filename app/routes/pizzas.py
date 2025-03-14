# app/routes/pizzas.py
import os
from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app import db
from app.models import Pizzas

UPLOAD_FOLDER = 'app/static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}

pizzae_bp = Blueprint('pipshash', __name__)

@pizzae_bp.route('/')
def listar_pizza():
    pizzae = Pizzas.query.all()
    return render_template('pipshash/listar_pizza.html', pipshash=pizzae)

@pizzae_bp.route('/new', methods=['GET', 'POST'])
def add_pizza():
    if request.method == 'POST':
        nombre = request.form['nombre']
        masa = request.form['masa']
        queso = request.form['queso']
        
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
            new_pizza = Pizzas(nombre=nombre, masa=masa, queso=queso, imagen=filename)
            db.session.add(new_pizza)
            db.session.commit()


        return redirect(url_for('pipshash.listar_pizza'))
    return render_template('pipshash/create_pizza.html')

@pizzae_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update_pizza(id):
    pizzas = Pizzas.query.get_or_404(id)

    if request.method == 'POST':
        pizzas.nombre = request.form['nombre']
        pizzas.masa = request.form['masa']
        pizzas.queso = request.form['queso']

        # Verifica si se subió una nueva imagen
        if 'imagen' in request.files:
            file = request.files['imagen']

            if file and file.filename != '' and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))  # Guarda la nueva imagen
                
                # Borra la imagen anterior si existe
                if pizzas.imagen:
                    old_image_path = os.path.join(UPLOAD_FOLDER, pizzas.imagen)
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)

                # Asigna la nueva imagen al objeto de la pizza
                pizzas.imagen = filename

        db.session.commit()
        return redirect(url_for('pipshash.listar_pizza'))

    return render_template('pipshash/update_pizza.html', pizzas=pizzas)

@pizzae_bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_pizzas(id):
    pizzas = Pizzas.query.get(id)
    db.session.delete(pizzas)
    db.session.commit()
    return redirect(url_for('pipshash.listar_pizza'))

    # Función para validar extensiones de archivo
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS