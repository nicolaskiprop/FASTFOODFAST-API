from flask import Blueprint
from .admin_views import Foods

admin_blueprint = Blueprint("admin", __name__)
