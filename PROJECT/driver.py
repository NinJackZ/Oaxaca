'''
@author: Team 29
@company: Team 29
'''

from flask import Flask

from app.info import info
from app.view_menu import view_menu
from app.view_orders import view_orders
from app.edit_orders import edit_orders
from app.login import user_login
from app.waiter import waiter
from app.kitchen import kitchen
from app.edit_menu import edit_menu
from app.models import Menu,Orders,Orders_archive,Admin_User,db, login_manager
from app.payment import view_payment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = 'super secret key'

app.register_blueprint(info)
app.register_blueprint(view_menu)
app.register_blueprint(view_orders)
app.register_blueprint(edit_orders)
app.register_blueprint(user_login)
app.register_blueprint(waiter)
app.register_blueprint(kitchen)
app.register_blueprint(edit_menu)
app.register_blueprint(view_payment)

db.init_app(app)
login_manager.init_app(app)

def __repr__(self):
    return '<Menu %r>' % self.id

# for resetting the datbase context
def ResetDatabase():
    with app.app_context():
        db.drop_all()
        db.create_all()

if __name__ == '__main__':
    app.run(host="0.0.0.0")
