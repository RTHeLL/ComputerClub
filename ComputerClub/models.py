from ComputerClub import db


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.String(), unique=True, index=True, )
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())

    def __init__(self, user_login, first_name, last_name):
        self.user_login = user_login
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'<id {self.id}>'

