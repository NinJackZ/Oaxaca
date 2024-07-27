from flask import Blueprint, render_template, request, redirect
from app.extensions import db
from app.models import Orders,Menu

view_menu = Blueprint('menu', __name__,
                        template_folder='templates', static_folder='static')

@view_menu.route('/menu/',  methods=['POST', 'GET'])
def menu():
    foods = Menu.query.filter_by(type='food')
    drinks = Menu.query.filter_by(type='drink')
    return render_template('menu.html', foods=foods, drinks=drinks)


@view_menu.route('/menu-order/',  methods=['POST', 'GET'])
def order():
    if request.method == 'POST':
        number = request.form['num']
        return redirect('/menu-order/' + number)
    else:
        return render_template('table.html')
    
@view_menu.route('/menu-order/<int:num>/', methods=['POST', 'GET'])
def tableMenu(num):
    foods = Menu.query.filter_by(type='food')
    drinks = Menu.query.filter_by(type='drink')
    return render_template('menu-order.html', foods=foods, drinks=drinks, num=num)


@view_menu.route('/menu-order/<int:num>/<int:id>/', methods=['POST', 'GET'])
def menuAdd(num, id):
    order = Menu.query.get(id)
    orders = Orders(table_id=num, menu_item=order.name,
                            menu_price=order.price, status='pending')
    db.session.add(orders)
    db.session.commit()
    return redirect('/menu-order/' + str(num))