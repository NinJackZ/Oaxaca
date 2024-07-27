from flask import Blueprint, render_template
from app.models import Orders,Waiter_calling, Orders_archive
from app.login import login_required
from app.extensions import db

waiter = Blueprint('waiter', __name__,
                        template_folder='templates', static_folder='static')

@waiter.route('/status-waiter/')
@login_required
def statuswaitermenu():
    return render_template("status-waiter.html")

@waiter.route('/status-waiter-inner/')
@login_required
def statuswaiterinner():
    pending = Orders.query.filter_by(status="pending")
    ready = Orders.query.filter_by(status="ready")
    tableStatus = Waiter_calling.query.filter_by(status="Called")
    try:
        orders_delivered = Orders.query.filter_by(status="delivered").first()
    except:
        return render_template("status-waiter-inner.html", orders_delivered=orders_delivered, pending=pending, ready=ready, tableStatus=tableStatus)
    
    return render_template("status-waiter-inner.html", pending=pending, ready=ready, tableStatus=tableStatus)