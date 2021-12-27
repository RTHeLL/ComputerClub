import datetime

from flask import render_template, redirect, url_for, request
from flask_login import current_user, logout_user, login_required
from werkzeug.urls import url_parse

from database.controller import UsersController, PostsController

from blueprints.ucp import bp

from ComputerClub import db

from .forms import LoginForm, RegisterForm, RecoveryForm, EditProfileForm, NewPostCreateForm

users_controller = UsersController()
posts_controller = PostsController()


# Login page
@bp.route('/login', methods=['POST', 'GET'])
def login_handler():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = LoginForm()
    if form.validate_on_submit():
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
        return users_controller.register_user(payload={'form': form})
    return render_template('ucp/register.html', title='Sign Up', form=form)


# Password recovery todo Create recovery password page
@bp.route('/recovery', methods=['POST', 'GET'])
def recovery_handler():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = RecoveryForm()
    if form.validate_on_submit():
        return redirect(url_for('main'))
    return render_template('ucp/recovery.html', title='Restore account', form=form)


@bp.route('/user/<user_id>', methods=['POST', 'GET'])
@login_required
def profile_handler(user_id):
    __payload = users_controller.profile_user(payload={'user_id': user_id})
    return render_template('ucp/profile.html', payload=__payload)


@bp.route('/user/<user_id>/edit', methods=['POST', 'GET'])
@login_required
def profile_edit_handler(user_id):
    form = EditProfileForm()
    __payload = users_controller.profile_user(payload={'user_id': user_id})
    if form.validate_on_submit():
        return users_controller.edit_profile_user(payload={
            'form': form,
            'user_id': user_id
        })
    elif request.method == 'GET':
        for field in form:
            field.data = getattr(__payload['user'], field.name, None)
    return render_template('ucp/profile.html', title='Edit Profile', form=form, payload=__payload, edit=True)


@bp.route('/user/<user_id>/add-post', methods=['POST', 'GET'])
@login_required
def profile_post_create(user_id):
    form = NewPostCreateForm()
    # __payload = posts_controller.create_post(payload={
    #     'form': form,
    #     'user_id': user_id
    # })
    if form.validate_on_submit():
        return posts_controller.create_post(payload={
            'form': form,
            'user_id': user_id
        })
    return render_template('ucp/create_post.html', title='Create new post', form=form)


@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_session = datetime.datetime.utcnow()
        db.session.commit()
