from flask import Blueprint, render_template, request, redirect
from app.extensions import db
from app.models import Orders

view_orders = Blueprint('orders', __name__,
                        template_folder='templates', static_folder='static')

def total_price(num):
    orderdb = Orders.query.filter_by(table_id=num)
    orderdb = orderdb.filter(Orders.status == 'pending')
    return format(sumPrice(orderdb), '.2f')

def sumPrice(orderdb):
    total = 0
    for order in orderdb:
        total += float(order.menu_price)
    return total

@view_orders.route('/view-order/<int:num>/')
def orders(num):
    orderdb = Orders.query.filter_by(table_id=num)
    orderdb = orderdb.filter(Orders.status == 'pending')

    # count the number of items
    count = orderdb.count()
    # sum of the prices
    total = total_price(num)
    return render_template('orders.html', num=num, orderdb=orderdb, count=count, total=total)

@view_orders.route('/confirm/<int:num>/')
def confirm(num):
    orderdb = Orders.query.filter_by(table_id=num)
    orderdb = orderdb.filter(Orders.status != 'delivered')

    for order in orderdb:
        order.status = 'paid'
        db.session.commit()

    return redirect('/')
