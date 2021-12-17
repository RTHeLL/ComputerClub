from sqlalchemy.exc import SQLAlchemyError

from ComputerClub import db


def db_commit(func):
    def commit(*args, **kwargs):
        try:
            func(*args, **kwargs)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            print(e)  # todo create logger
            db.session.rollback()
            return False
    return commit
