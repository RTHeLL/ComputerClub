from flask import flash, redirect, url_for, abort

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
            flash(f'{payload["form"].username.data} successes created!')
            return redirect(url_for('ucp.login_handler'))

    def profile_user(self, payload):
        __user = users_repository.get_user(payload=payload)
        __payload = None
        if __user is not None:
            __payload = {
                'title': __user.username,
                'user': __user,
                'user_info_column': {'first_name': 'First name',
                                     'about_me': 'About me',
                                     'email': 'Email',
                                     'last_name': 'Last name',
                                     'favorite_game': 'Favorite Game'}
            }
        else:
            abort(404)
        return __payload

    def edit_profile_user(self, payload):
        if 'form' not in payload or 'user_id' not in payload:
            return False
        __form = payload['form']
        __user_id = payload['user_id']

        payload = {
            'first_name': __form.first_name.data,
            'last_name': __form.last_name.data,
            'email': __form.email.data,
            'favorite_game': __form.favorite_game.data,
            'about_me': __form.about_me.data,
            'site_link': __form.site_link.data,
            'steam': __form.steam.data,
            'twitter': __form.twitter.data,
            'instagram': __form.instagram.data,
            'facebook': __form.facebook.data
        }

        if users_repository.edit_user(__user_id, **payload):
            flash('Your changes have been saved')
            return redirect(url_for('ucp.profile_handler', user_id=__user_id))

