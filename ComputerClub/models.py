import datetime
from hashlib import md5

from ComputerClub import db, login

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin


@login.user_loader
def _load_user(_user_id):
    return User.query.get(int(_user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True, index=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    balance = db.Column(db.Integer, default=0, nullable=False)
    favorite_game = db.Column(db.String(64))
    site_link = db.Column(db.String(64))
    steam = db.Column(db.String(64))
    twitter = db.Column(db.String(64))
    instagram = db.Column(db.String(64))
    facebook = db.Column(db.String(64))
    about_me = db.Column(db.String(140))
    last_session = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    is_superuser = db.Column(db.Boolean, default=0)

    def generate_password(self, __password):
        self.password = generate_password_hash(__password)

    def check_password(self, __password):
        return check_password_hash(self.password, __password)

    def get_avatar(self, __size):
        __gravatar_hash = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=mp&s={}'.format(__gravatar_hash, __size)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @property
    def get_attrs(self):
        return self.__dict__

    def __repr__(self):
        return f'<id: {self.id}' \
               f'username: {self.username}' \
               f'email: {self.email}>'


class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(64), index=True)
    content = db.Column(db.String(512))
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default=0)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship('User')

    def __repr__(self):
        return f'<Post {self.id}>'


class Computer(db.Model):
    __tablename__ = 'computers'

    id = db.Column(db.Integer, primary_key=True, index=True)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    room = db.relationship('Room')

    def __repr__(self):
        return f'<Computer {self.id}:' \
               f'Room - {self.room.name}({self.room.id})>'


class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(64), index=True)

    def __repr__(self):
        return f'<Room {self.id}:' \
               f'Room - {self.name}>'


class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.String(512))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship('User')

    def __repr__(self):
        return f'<News {self.id}:' \
               f'News - {self.title}>'
