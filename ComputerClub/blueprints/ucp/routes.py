from flask import render_template, redirect, url_for
from flask_login import current_user, logout_user

from database.controller import UsersController

from blueprints.ucp import bp
from .forms import LoginForm, RegisterForm


users_controller = UsersController()


# Login page
@bp.route('/login', methods=['POST', 'GET'])
def login_handler():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = LoginForm()
    if form.validate_on_submit():
        __payload = {
            'form': form,
            'username': form.username.data,
            'password': form.password.data
        }
        return users_controller.login_user(payload=__payload)
    return render_template('ucp/login.html', title='Sign In', form=form)


# Logout page
@bp.route('/logout')
def logout_handler():
    logout_user()
    return redirect(url_for('main'))


# Register page
@bp.route('/register', methods=['POST', 'GET'])
def register_handler():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = RegisterForm()
    if form.validate_on_submit():
        return users_controller.register_user(payload=form)
    return render_template('ucp/register.html', title='Sign Up', form=form)


# Password recovery todo Create recovery password page
@bp.route('/recovery', methods=['POST', 'GET'])
def recovery_handler():
    pass
