from flask import Blueprint, render_template, request, redirect
from app.models import Menu
from app.login import login_required
from app.extensions import db
import os

edit_menu = Blueprint('edit_menu', __name__,
                        template_folder='templates', static_folder='static')

@edit_menu.route('/edit-menu/')
@login_required
def editmenu():
    foods = Menu.query.filter_by(type='food')
    drinks = Menu.query.filter_by(type='drink')
    return render_template('edit-menu.html', foods=foods, drinks=drinks)

@edit_menu.route('/edit-menu/delete/<int:id>/', methods=['POST'])
@login_required
def editmenu_delete(id):
    item_to_delete = Menu.query.get(id)
    db.session.delete(item_to_delete)
    db.session.commit()

    return redirect('/edit-menu/')

@edit_menu.route('/edit-menu/soldout/<int:id>/',methods=['POST'])
@login_required
def editmenu_soldout(id):
    menudb = Menu.query.get(id)
    menudb.soldout = "true"
    db.session.commit()

    return redirect('/edit-menu/')


@edit_menu.route('/edit-menu/add/', methods=['POST'])
@login_required
def editmenu_add():
    item_name = request.form['item_name']
    item_type = request.form['type']
    item_price = request.form['price']
    item_calories = request.form['calories']
    item_diet = ""
    item_image = request.files['image']

    if item_image == "":
        item_image == "placeholder.jpeg"

    if request.form.get('vegan'):
        item_diet += "Ve, "
    if request.form.get('alcohol'):
        item_diet += "18+"

    if not os.path.exists('static'):
        os.mkdir('static')
    if not os.path.exists(os.path.join('static', 'Menu_items')):
        os.mkdir(os.path.join('static', 'Menu_items'))

    try:
        item_image.save(os.path.join('static', 'Menu_items', item_image.filename))
        image_name = item_image.filename
    except:
        image_name = "placeholder.jpeg"

    item = Menu(name = item_name, type = item_type, price = item_price, cals = item_calories, diet = item_diet, soldout="false", image=image_name)
    db.session.add(item)
    db.session.commit()

    return redirect('/edit-menu/')


