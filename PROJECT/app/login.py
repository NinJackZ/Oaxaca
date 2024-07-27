from flask import Blueprint, render_template, request, redirect, session
from flask_login import login_required, logout_user, login_user
from app.models import Admin_User
from app.extensions import login_manager
import hashlib as h
from datetime import timedelta

user_login = Blueprint('login', __name__,
                        template_folder='templates', static_folder='static')

@login_manager.user_loader
def load_user(user_id):
    return Admin_User.query.get(int(user_id))

# for hashing

def hash(input):
    b = bytearray()
    b.extend(map(ord, input))
    return h.sha3_256(b).hexdigest()

# for timeout

@user_login.before_request
def make_session_permanent():
    session.permanent = True
    user_login.permanent_session_lifetime = timedelta(minutes=30)

@user_login.route('/login/', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':  # START OF PASSWORD HANDLING SECTION
        request_username = request.form['username']
        request_password = request.form['password']
        request_password = hash(request_password)

        # Finding the request_username information for query
        user = Admin_User.query.filter_by(username=request_username).first()

        type = user.type
        uname = user.username
        pword = user.password

        if type == 'waiter':    # Scanner for type of staff member

            if request_username == uname and request_password == pword:
                login_user(user)
                return redirect('/status-waiter/')

            else:
                return 'error logging in (error code:1)'

        elif type == 'kitchen':

            if request_username == uname and request_password == pword:
                login_user(user)
                return render_template('status-kitchen.html')
            else:
                return 'error logging in (error code:2)'

        else:
            return 'no such type of user'

    else:
        return render_template('login-admin.html')

@user_login.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect('/')

