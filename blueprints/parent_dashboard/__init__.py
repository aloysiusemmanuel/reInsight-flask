from flask import Blueprint

parent_dash_bp = Blueprint(
    "parent_dashboard",
    __name__,
    url_prefix="/parent_dashboard"
)

from . import routes