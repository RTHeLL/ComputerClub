from flask import flash, redirect, url_for, request
from flask_login import login_user
from werkzeug.urls import url_parse

from database.repository import NewsRepository, UsersRepository

news_repository = NewsRepository()
users_repository = UsersRepository()


class Controller:
    @staticmethod
    def _preparing_payload():
        return {
            'filterField': None,
            'filterValue': None,
            'filterType': None,
            'sortField': None
        }


class NewsController(Controller):
    def get_news(self, payload=None):
        if payload is None:
            payload = super()._preparing_payload()
        return news_repository.get_all_news(payload=payload)


class UsersController(Controller):
    def login_user(self, payload):
        __user = users_repository.get_user(payload=payload)

        if __user is None or not __user.check_password(payload['password']):
            flash(f'Invalid username or password')
            return redirect(url_for('.login_handler'))
        login_user(__user, remember=payload['form'].remember.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main')
        return redirect(next_page)

    def register_user(self, payload):
        if users_repository.create_user(payload=payload):
            flash(f'{payload.username.data} successes created!')
            return redirect(url_for('ucp.login_handler'))
