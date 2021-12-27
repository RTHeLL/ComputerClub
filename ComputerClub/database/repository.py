from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError

from ComputerClub import db

from ComputerClub.models import News, User, Posts

from decorators import db_commit


class Repository:
    pass


class NewsRepository(Repository):
    def get_all_news(self, payload):
        __news = News.query.all()
        return __news


class UsersRepository(Repository):
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

    def get_user(self, payload):
        __user = User.query\
                    .filter(self.__payload_definition(_payload=payload))\
                    .first()

        return __user

    @db_commit
    def create_user(self, payload):
        __user = User(username=payload['form'].username.data,
                      email=payload['form'].email.data,
                      first_name=payload['form'].first_name.data,
                      last_name=payload['form'].last_name.data)
        __user.generate_password(payload['form'].password.data)
        db.session.add(__user)

    @db_commit
    def edit_user(self, *args, **kwargs):
        try:
            __user = self.get_user({'user_id': args})
            __user.update(**kwargs)
            return True
        except SQLAlchemyError as e:
            print(e)  # todo add logger


class PostsRepository(Repository):
    def get_all_posts_of_user(self, user_id):
        __posts = Posts.query\
                    .filter_by(author_id=user_id) \
                    .order_by(desc(Posts.create_date))\
                    .all()
        return __posts

    @db_commit
    def create_new_post(self, payload):
        __post = Posts(title=payload['form'].title.data,
                       content=payload['form'].content.data,
                       author_id=payload['user_id'])
        db.session.add(__post)

