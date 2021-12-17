from ComputerClub import db

from ComputerClub.models import News, User

from decorators import db_commit


class Repository:
    pass


class NewsRepository(Repository):
    def get_all_news(self, payload):
        __news = News.query.all()
        return __news


class UsersRepository(Repository):
    def get_user(self, payload):
        __user = User.query\
                    .filter(self.__payload_definition(_payload=payload))\
                    .first()

        return __user

    @db_commit
    def create_user(self, payload):
        __user = User(username=payload.username.data,
                      email=payload.email.data,
                      first_name=payload.first_name.data,
                      last_name=payload.last_name.data)
        __user.generate_password(payload.password.data)
        db.session.add(__user)

    @staticmethod
    def __payload_definition(_payload):
        __query = 0
        if _payload is None:
            __query = User.id is not None

        if 'user_id' in _payload:
            __query = User.id == _payload['user_id']
        elif 'username' in _payload:
            __query = User.username == _payload['username']
        elif 'email' in _payload:
            __query = User.email == _payload['email']

        return __query
