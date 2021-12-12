from ComputerClub import app, db
from ComputerClub.models import User, Computer, Room, News


@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'User': User,
            'Computer': Computer,
            'Room': Room,
            'News': News}
