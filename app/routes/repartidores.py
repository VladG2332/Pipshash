from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Repartidores  # Cambio aquí

repartidores_bp = Blueprint('repartidores', __name__)

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
        
        new_repartidor = Repartidores(nombre=nombre, placa_moto=placa_moto, capacidad=capacidad)
        db.session.add(new_repartidor)
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
