from ComputerClub import app, db
from ComputerClub.models import User, Computer, Room, News

from database.repository import NewsRepository, UsersRepository
from database.controller import NewsController, UsersController


@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'User': User,
            'Computer': Computer,
            'Room': Room,
            'News': News,
            'NewsRepository': NewsRepository,
            'UsersRepository': UsersRepository,
            'NewsController': NewsController,
            'UsersController': UsersController}
