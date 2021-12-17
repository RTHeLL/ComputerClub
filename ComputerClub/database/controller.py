from flask import flash, redirect, url_for, request, abort
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
    def register_user(self, payload):
        if users_repository.create_user(payload=payload):
            flash(f'{payload.username.data} successes created!')
            return redirect(url_for('ucp.login_handler'))

    def profile_user(self, payload):
        __user = users_repository.get_user(payload=payload)
        __payload = None
        if __user is not None:
            __payload = {
                'title': __user.username,
                'user': __user
            }
        else:
            abort(404)
        return __payload
