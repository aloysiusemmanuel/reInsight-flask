from flask import Blueprint

parent_bp = Blueprint(
    "parent",
    __name__,
    url_prefix="/parent-dasboard",
    template_folder="../../templates"
)

from . import routes