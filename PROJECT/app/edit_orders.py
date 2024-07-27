from flask import Blueprint, redirect, render_template, request
from app.extensions import db
from app.models import Orders, Menu, Waiter_calling

edit_orders = Blueprint('edit_orders', __name__,
                        template_folder='templates', static_folder='static')

@edit_orders.route('/delete/<int:number>/<int:id>/')
def delete(number, id):
    order_to_delete = Orders.query.get(id)
    db.session.delete(order_to_delete)
    db.session.commit()

    return redirect('/view-order/' + str(number))


@edit_orders.route('/paid/<int:num>/')
def paid(num):
    orderdb = Orders.query.filter_by(id=num).first()
    orderdb.status = "paid"
    db.session.commit()

    return redirect('/status-waiter/')


@edit_orders.route('/cancel/<int:num>/')
def cancel(num):
    orderdb = Orders.query.filter_by(id=num).first()
    db.session.delete(orderdb)
    db.session.commit()

    return redirect('/status-waiter/')


@edit_orders.route('/cook/<int:num>/')
def cook(num):
    orderdb = Orders.query.filter_by(id=num).first()
    orderdb.status = "ready"
    db.session.commit()

    return redirect('/status-kitchen/')


@edit_orders.route('/delivered/<int:num>/')
def delivered(num):
    orderdb = Orders.query.filter_by(id=num).first()
    orderdb.status = "delivered"
    db.session.commit()
    return redirect('/status-waiter/')

@edit_orders.route('/edit/<int:num>/<int:id>/', methods = ['POST', 'GET'])
def edit(num, id):
    food = Menu.query.get(id)
    ingre = food.ingredients.split(', ')

    return render_template("edit.html", food = food, ingre = ingre, num = num)
    
@edit_orders.route('/edit-add/<int:num>/<int:id>/', methods = ['POST', 'GET'])
def edit_add(num, id):
    food = Menu.query.get(id)
    ingre = food.ingredients.split(', ')
    edit_final = ""
    if request.method == 'POST':
        for i in ingre:
            edit = request.form.get('edit ' + i)
            if edit != None:
                edit_final += request.form['edit ' + i] + " "
        orders = Orders(table_id=num, menu_item=food.name,
                            menu_price=food.price, edit=edit_final, status='pending')
        db.session.add(orders)
        db.session.commit()
        return redirect('/menu-order/' + str(num))
    else:
        return render_template("edit.html", food = food, ingre = ingre, num = num)
    
@edit_orders.route('/WaiterCalled/<int:num>/')
def waiterCalled(num):
    
    if Waiter_calling.query.filter_by(table_id=num).scalar():
        waiter = Waiter_calling.query.filter_by(table_id=num).first()
        waiter.status = "Called"
        db.session.commit()
    else:
        waiter = Waiter_calling(table_id =num, status = "Called")
        db.session.add(waiter)
        db.session.commit()
    return redirect('/')


@edit_orders.route('/WaiterCalledFin/<int:num>/')
def waiterCalledFin(num):
    waiter = Waiter_calling.query.filter_by(table_id=num).first()
    waiter.status = "Satisfied"
    db.session.commit()
    return redirect('/status-waiter/')

