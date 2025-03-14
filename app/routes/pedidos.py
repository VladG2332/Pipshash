# app/routes/pizzas.py
from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Pedidos, Orden, Repartidores, Pizzas

pedidos_bp = Blueprint('pedidos', __name__)

@pedidos_bp.route('/')
def listar_pedidos():
    pedidos = Pedidos.query.all()
    ordenes = Orden.query.all()
    repartidores = Repartidores.query.all()
    pizzas = Pizzas.query.all()
    return render_template('pedidos/listar_pedidos.html', pedidos=pedidos, ordenes=ordenes, repartidores=repartidores, pizzas=pizzas)

@pedidos_bp.route('/newpedido', methods=['GET', 'POST'])
def add_pedido():
    if request.method == 'POST':
        orden = request.form['orden']
        repartidor = request.form['repartidor']
        new_pedido = Pedidos(orden_id=orden, repartidor_id=repartidor)
        db.session.add(new_pedido)
        db.session.commit()
        return redirect(url_for('pedidos.listar_pedidos'))
    ordenes = Orden.query.all()
    repartidores = Repartidores.query.all()
    return render_template('pedidos/create_pedido.html', ordenes=ordenes, repartidores=repartidores)

# Actualizar repartidor
@pedidos_bp.route('/pedidos/update/<int:id>', methods=['GET', 'POST'])
def update_pedido(id):
    repartidores = Repartidores.query.all()
    pedido = Pedidos.query.get(id)
    if request.method == 'POST':
        pedido.orden_id = request.form['orden']
        pedido.repartidor_id = request.form['repartidor']
        db.session.commit()
        return redirect(url_for('pedidos.listar_pedidos'))
    ordenes = Orden.query.all()
    return render_template('pedidos/update_pedido.html', pedido=pedido, ordenes=ordenes, repartidores=repartidores)

@pedidos_bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_pedido(id):
    pedido = Pedidos.query.get(id)
    db.session.delete(pedido)
    db.session.commit()
    return redirect(url_for('pedidos.listar_pedidos'))

@pedidos_bp.route('/neworden', methods=['GET', 'POST'])
def add_orden():
    if request.method == 'POST':
        pizza = request.form['pizza']
        cantidad = request.form['cantidad']
        pizza_obj = Pizzas.query.get(int(pizza))
        new_orden = Orden(pizza=pizza_obj, cantidad=int(cantidad))
        print(pizza, cantidad)
        db.session.add(new_orden)
        db.session.commit()
        return redirect(url_for('pedidos.listar_pedidos'))
    pizzas = Pizzas.query.all()
    return render_template('pedidos/create_orden.html', pizzas=pizzas)

@pedidos_bp.route('/orden/update/<int:id>', methods=['GET', 'POST'])
def update_orden(id):
    orden = Orden.query.get(id)
    pizzas = Pizzas.query.all()
    if request.method == 'POST':
        orden.pizza_id = request.form['pizza']
        orden.cantidad = request.form['cantidad']
        db.session.commit()
        return redirect(url_for('pedidos.listar_pedidos'))
    return render_template('pedidos/update_orden.html', orden=orden, pizzas=pizzas)

@pedidos_bp.route('/orden/delete/<int:id>', methods=['GET', 'POST'])
def delete_orden(id):
    orden = Orden.query.get(id)
    db.session.delete(orden)
    db.session.commit()
    return redirect(url_for('pedidos.listar_pedidos'))