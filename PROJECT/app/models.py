from .extensions import db, login_manager
from datetime import datetime
from flask_login import UserMixin

# For the food menu table
class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    cals = db.Column(db.String(5), nullable=False)
    diet = db.Column(db.String(10))
    soldout = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(100))
    ingredients = db.Column(db.String(120))


class Admin_User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    type = db.Column(db.String(20), unique=True, nullable=False)

    username = db.Column(db.String(20), unique=True, nullable=False)

    password = db.Column(db.String(50), unique=True, nullable=False)

# For the orders table


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer)
    menu_item = db.Column(db.String(80), nullable=False)
    menu_price = db.Column(db.String(7), nullable=False)
    edit = db.Column(db.String(80))
    status = db.Column(db.String(80))
    order_time = db.Column(db.DateTime, default=datetime.utcnow().replace(microsecond=0))
    delivery_time = db.Column(db.DateTime)

# After the order is complete, it will be moved to the archive table.


class Orders_archive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer)
    menu_item = db.Column(db.String(80), nullable=False)
    menu_price = db.Column(db.String(7), nullable=False)
    edit = db.Column(db.String(80))
    status = db.Column(db.String(80))
    order_time = db.Column(db.DateTime, default=datetime.utcnow().replace(microsecond=0))

class Waiter_calling(db.Model):
    table_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(80))
