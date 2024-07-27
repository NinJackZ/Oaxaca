from flask import Blueprint, render_template
from app.models import Orders
from app.login import login_required

kitchen = Blueprint('kitchen', __name__,
                        template_folder='templates', static_folder='static')

@kitchen.route('/status-kitchen/')
@login_required
def statuskitchen():
    return render_template('status-kitchen.html')

@kitchen.route('/status-kitchen-inner/')
@login_required
def statuskitcheninner():
    orderdb = Orders.query.filter_by(status="paid")
    return render_template('status-kitchen-inner.html', orderdb=orderdb)


