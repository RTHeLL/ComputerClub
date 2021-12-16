from flask import Blueprint

bp = Blueprint('ucp', __name__)

from blueprints.ucp import routes
