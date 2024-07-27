from flask import Blueprint, render_template, request, redirect
from app.extensions import db
from app.models import Orders,Menu
from app.view_orders import total_price

view_payment = Blueprint('payment', __name__,
                        template_folder='templates', static_folder='static')

@view_payment.route('/payment/<int:num>/', methods = ['POST', 'GET'])
def pay(num):
    total = total_price(num)
    if request.method == 'POST':
        
        if request.form['card-name'] != "" and request.form['card-num'] != "" and request.form['card-sort'] != "":
            return redirect('/confirm/' + str(num))
        else:
            error = 'Please Fill All Fields'
            return render_template('payment.html',total = total, num = num, error = error)
    else:
        return render_template('payment.html',total = total, num = num)