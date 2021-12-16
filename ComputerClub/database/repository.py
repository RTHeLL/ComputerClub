from sqlalchemy.exc import SQLAlchemyError

from ComputerClub import db

from ComputerClub.models import News, User


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

    def create_user(self, payload):
        try:
            __user = User(username=payload.username.data,
                          email=payload.email.data,
                          first_name=payload.first_name.data,
                          last_name=payload.last_name.data)
            __user.generate_password(payload.password.data)
            db.session.add(__user)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            print(e)
            db.session.rollback()
            return False

    @staticmethod
    def __payload_definition(_payload):
        if _payload is None:
            return User.id is not None

        if 'username' in _payload:
            return User.username == _payload['username']
        elif 'email' in _payload:
            return User.email == _payload['email']

