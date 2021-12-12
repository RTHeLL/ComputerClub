import datetime

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
    is_superuser = db.Column(db.Boolean, default=0)

    def generate_password(self, __password):
        self.password = generate_password_hash(__password)

    def check_password(self, __password):
        return check_password_hash(self.password, __password)

    def __repr__(self):
        return f'<id: {self.id}' \
               f'username: {self.username}' \
               f'email: {self.email}>'


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
