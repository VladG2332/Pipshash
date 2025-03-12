# app/routes/pizzas.py
from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Pizzas

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
        new_pizza = Pizzas(nombre=nombre , masa=masa , queso=queso)
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
        db.session.commit()
        return redirect(url_for('pipshash.listar_pizza'))
    return render_template('pipshash/update_pizza.html', pizzas=pizzas)

@pizzae_bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_pizzas(id):
    pizzas = Pizzas.query.get(id)
    db.session.delete(pizzas)
    db.session.commit()
    return redirect(url_for('pipshash.listar_pizza'))
