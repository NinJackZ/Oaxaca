from flask import Blueprint, render_template

info = Blueprint('info', __name__,
                        template_folder='templates', static_folder='static')

@info.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@info.route('/about/')
def about():
    return render_template('about.html')