from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user

from werkzeug.urls import url_parse

from ComputerClub import db
from ComputerClub.models import User

from blueprints.ucp import bp
from .forms import LoginForm, RegisterForm


# Login page
@bp.route('/login', methods=['POST', 'GET'])
def login_handler():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = LoginForm()
    if form.validate_on_submit():
        _user = User.query.filter_by(username=form.username.data).first()
        if _user is None or not _user.check_password(form.password.data):
            flash(f'Invalid username or password')
            return redirect(url_for('.login_handler'))
        login_user(_user, remember=form.remember.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main')
        return redirect(next_page)
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
        _user = User(username=form.username.data,
                     email=form.email.data,
                     first_name=form.first_name.data,
                     last_name=form.last_name.data)
        _user.generate_password(form.password.data)
        db.session.add(_user)
        db.session.commit()
        flash(f'{form.username.data} successes created!')
        return redirect(url_for('ucp.login_handler'))
    return render_template('ucp/register.html', title='Sign Up', form=form)


# Password recovery todo Create recovery password page
@bp.route('/recovery', methods=['POST', 'GET'])
def recovery_handler():
    pass
