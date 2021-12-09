from flask import render_template

from blueprints.ucp import bp
from .forms import LoginForm, RegisterForm


# Login page
@bp.route('/login')
def login_handler():
    form = LoginForm()
    return render_template('ucp/login.html', title='Sign In', form=form)


# Register page
@bp.route('/register')
def register_handler():
    form = RegisterForm()
    return render_template('ucp/register.html', title='Sign Up', form=form)
