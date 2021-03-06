import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)

login = LoginManager(app)
login.login_view = 'ucp.login_handler'  # for @login_required

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Blueprints
from blueprints.ucp import bp as ucp_bp

# Blueprints register
app.register_blueprint(ucp_bp, url_prefix='/ucp')

from ComputerClub import routes, models
