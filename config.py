import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = 'oM8GrMGIE3ra7iNyxhCR65G3X8WYaOxcJC1G'
    SQLALCHEMY_DATABASE_URI = 'postgresql://computer_club:Snuvi7EXWTDU@localhost:5432/computer_club'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
