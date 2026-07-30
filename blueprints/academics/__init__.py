from flask import Blueprint

academics_bp = Blueprint(
    "academics",
    __name__,
    url_prefix="/academics",
    template_folder="../../templates")

from . import routes